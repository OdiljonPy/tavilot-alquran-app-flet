import re
import binascii
import requests
import os
import pyhtml2md
import flet as ft
import pymupdf
from PIL import Image
from io import BytesIO
import base64


def extract_base64_and_save_images(api_html_response):
    """Process base64 images and save them."""
    expression = r'(data:image/png;base64,[A-Za-z0-9+/=]+)'
    matches = re.findall(expression, api_html_response)

    image_files = []
    parts = []
    last_end = 0

    # Extract base64 images and text
    for index, base64_data in enumerate(matches):
        start = api_html_response.find(base64_data, last_end) - len("data:image/png;base64,")
        end = start + len(base64_data) + len("data:image/png;base64,")

        # Extract text before the image
        if start > last_end:
            text_content = api_html_response[last_end:start].strip()
            parts.append({"type": "text", "content": text_content})

        try:
            base64_string = base64_data.split(",")[1]
            image_data = base64.b64decode(base64_string, validate=True)

            image_filename = os.path.join(os.getcwd(), f"output_image_{index}.png")
            with open(image_filename, "wb") as image_file:
                image_file.write(image_data)

            image_files.append(image_filename)
            parts.append({"type": "image", "content": image_filename})
        except binascii.Error:
            parts.append({"type": "text", "content": "[Invalid Image]"})

        last_end = end

    if last_end < len(api_html_response):
        text_content = api_html_response[last_end:].strip()
        parts.append({"type": "text", "content": text_content})

    return parts, "Images processed and saved."


def extract_and_process_videos(api_html_response):
    """Extract video content from HTML response."""
    # Regular expression to match any .mp4 URL
    video_expression = r'https?://[^"]+\.mp4'

    video_matches = re.findall(video_expression, api_html_response)

    video_files = []
    for video_url in video_matches:
        video_files.append(video_url)

    print(video_files)  # For debugging, to check the extracted video URLs

    return video_files


def render_content(container, parts, video_files):
    """Render text and images alternately based on extracted parts."""
    arabic_pattern = r'[\u0600-\u06FF]+'

    video_index = 0  # Track the video index to match video URLs with the actual video components

    for part in parts:
        if part["type"] == "text":
            # Convert HTML content to Markdown
            markdown_content = pyhtml2md.convert(part["content"])

            # Split the content into lines to detect and process Arabic text line by line
            lines = markdown_content.splitlines()
            for line in lines:
                # Check if the line contains a video URL
                video_urls = re.findall(r'https?://[^"]+\.mp4', line)
                if video_urls:
                    # Render video for each video URL found
                    for video_url in video_urls:
                        if video_index < len(video_files):
                            container.controls.append(ft.Video(
                                playlist=[
                                    ft.VideoMedia(
                                        resource=video_files[video_index]
                                    )
                                ],
                                playlist_mode=ft.PlaylistMode.LOOP,
                                fill_color=ft.colors.LIGHT_BLUE,
                                # aspect_ratio=16 / 9,
                                volume=100,
                                autoplay=False,
                                muted=False,
                                show_controls=True,
                                expand=True,
                                width=400,
                                height=400
                            ))
                            video_index += 1
                else:
                    # Render non-video content as text
                    if re.search(arabic_pattern, line):
                        # Render Arabic text with a custom font using ft.Text
                        container.controls.append(
                            ft.Text(line, style=ft.TextStyle(font_family='Amiri'), text_align=ft.TextAlign.CENTER, size=30)
                        )
                    else:
                        # Render non-Arabic content as Markdown
                        if line.strip():
                            container.controls.append(ft.Markdown(line))

        elif part["type"] == "image":
            container.controls.append(ft.Image(src=part["content"], width=200, height=200, expand=True))

    # Update the container to reflect changes
    container.update()


def about_us_page(page, back_button):
    page.clean()

    # Show a loading indicator
    loading = ft.ProgressRing()
    page.add(ft.Container(
        content=ft.Column(controls=[ft.Text("Loading...", height=480), loading],
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

        prev_button = ft.ElevatedButton("Previous Page", on_click=go_to_previous_page, disabled=True)
        next_button = ft.ElevatedButton("Next Page", on_click=go_to_next_page, disabled=True)

        def on_fetch_pdf(e):
            api_url = requests.get(url="http://176.221.28.202:8008/api/v1/moturudiy/5/").json().get('result').get('file')  # Replace with your API endpoint
            load_pdf_from_api(api_url)

        fetch_button = ft.ElevatedButton("Fetch PDF from API", on_click=on_fetch_pdf)

        page.add(content_container, ft.Column(
            [
                ft.Column(
                    [
                        fetch_button,
                        current_page_image,
                        ft.Row([prev_button, next_button], alignment=ft.MainAxisAlignment.CENTER),
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row([prev_button, next_button], alignment=ft.MainAxisAlignment.CENTER),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
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
