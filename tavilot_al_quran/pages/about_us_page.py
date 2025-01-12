import requests
import flet as ft
import pymupdf
from PIL import Image
from io import BytesIO
import base64
from .html_pdf_handler import extract_base64_and_save_images, extract_and_process_videos, render_content

def about_us_page(page, back_button):
    page.clean()
    page.scroll = True
    # Show a loading indicator
    loading = ft.ProgressRing()
    page.add(ft.Container(
        content=ft.Column(controls=[loading],
                          alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        expand=True
    ))
    page.update()

    # API call to fetch the "about" page data
    url = "http://176.221.28.202:8008/api/v1/about/"
    response = requests.get(url=url)

    if response.status_code == 200:
        data = response.json().get("result", {}).get("description", "")
        api_html_response = data

        # Process HTML to handle base64 images and videos
        parts, result = extract_base64_and_save_images(api_html_response)
        video_files = extract_and_process_videos(api_html_response)

        # Clear the page content after the data is loaded
        page.clean()

        # Container to hold the rendered content
        content_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(result, text_align=ft.TextAlign.CENTER, size=30),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            expand=True
        )

        pdf_document = None
        current_page_index = 0
        total_pages = 0

        current_page_image = ft.Image(fit=ft.ImageFit.CONTAIN, width=700)

        # Function to load PDF from API response
        def load_pdf_from_api(api_url):
            nonlocal pdf_document, current_page_index, total_pages
            try:
                # Fetch PDF from API
                response = requests.get(api_url)
                if response.status_code == 200:
                    pdf_bytes = BytesIO(response.content)  # Load PDF as bytes
                    pdf_document = pymupdf.open(stream=pdf_bytes, filetype="pdf")

                    total_pages = pdf_document.page_count
                    current_page_index = 0
                    render_page()
                else:
                    raise ValueError(f"Failed to fetch PDF. Status code: {response.status_code}")
            except Exception as e:
                current_page_image.src_base64 = ""
                page.snack_bar = ft.SnackBar(ft.Text(f"Error loading PDF: {e}"))
                page.snack_bar.open = True
                page.update()

        # Function to render a specific page
        def render_page():
            nonlocal current_page_index
            if pdf_document:
                try:
                    page_obj = pdf_document.load_page(current_page_index)
                    pixmap = page_obj.get_pixmap()
                    image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

                    buffer = BytesIO()
                    image.save(buffer, format="PNG")
                    buffer.seek(0)
                    current_page_image.src_base64 = base64.b64encode(buffer.read()).decode("utf-8")

                    prev_button.disabled = current_page_index == 0
                    next_button.disabled = current_page_index == total_pages - 1
                    page.update()
                except Exception as e:
                    current_page_image.src_base64 = ""
                    page.snack_bar = ft.SnackBar(ft.Text(f"Error rendering page: {e}"))
                    page.snack_bar.open = True
                    page.update()

        # Button actions for navigation
        def go_to_previous_page(e):
            nonlocal current_page_index
            if current_page_index > 0:
                current_page_index -= 1
                render_page()

        def go_to_next_page(e):
            nonlocal current_page_index
            if current_page_index < total_pages - 1:
                current_page_index += 1
                render_page()

        # Only create the buttons once
        prev_button = ft.ElevatedButton("Previous Page", on_click=go_to_previous_page, disabled=True)
        next_button = ft.ElevatedButton("Next Page", on_click=go_to_next_page, disabled=True)

        # Automatically fetch PDF when the app starts
        def fetch_pdf_on_start():
            api_url = requests.get(url="http://176.221.28.202:8008/api/v1/moturudiy/5/").json().get('result').get(
                'file')  # Replace with your API endpoint
            load_pdf_from_api(api_url)

        # Call the fetch function when the page is initialized
        fetch_pdf_on_start()

        page.update()

        page.add(content_container, ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
            controls=[
                current_page_image,
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        prev_button, next_button
                    ]
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        ))

        # Render the extracted parts (text, images, videos)
        render_content(content_container.content, parts, video_files)

    else:
        # Show an error message if the API call fails
        page.clean()
        error_message = ft.Text("Failed to load content.", text_align=ft.TextAlign.CENTER)
        page.add(ft.Container(
            content=error_message,
            alignment=ft.alignment.center,
            expand=True
        ))

    page.update()
