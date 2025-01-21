import requests
import flet as ft
from .html_pdf_handler import extract_base64_and_save_images, extract_and_process_videos, render_content

def about_us_page(page, back_button):
    TC = '#E9BE5F'
    page.clean()
    page.scroll = False
    # Show a loading indicator
    loading = ft.ProgressRing(color=TC)
    page.add(ft.Container(
        expand=True,
        adaptive=True,
        content=loading,
        alignment=ft.alignment.center)
    )
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
        page.scroll = True

        # Container to hold the rendered content
        content_container = ft.Container(
            margin=40,
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
        page.add(content_container)

        # Render the extracted parts (text, images, videos)
        render_content(content_container.content, parts, video_files, page)

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
