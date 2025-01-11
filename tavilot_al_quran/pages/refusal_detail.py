import flet as ft
import os
import requests
from .html_pdf_handler import extract_and_process_videos, extract_base64_and_save_images, render_content

def take_content_id(page, back_button, ids):
    page.clean()

    loading = ft.ProgressRing()

    page.add(ft.Container(
        content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center))

    page.update()
    url = f"http://176.221.28.202:8008/api/v1/refusal/{ids}/"
    response = requests.get(url=url)
    print(response.json())
    response_data = response.json().get('result').get('description')
    print(response_data)
    # Process HTML to handle base64 images and videos
    parts, result = extract_base64_and_save_images(response_data)
    video_files = extract_and_process_videos(response_data)

    if response.status_code == 200:
        page.clean()
        # Container to hold the rendered content
        content_container = ft.Container(
            margin=50,
            image_src=os.path.abspath("assets/searchbg.png"),
            image_fit="cover",
            alignment=ft.alignment.center,
            content=ft.Container(
                alignment=ft.alignment.center,
                scale=ft.Scale(scale_x=0.9),
                bgcolor='white',
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        back_button,
                        ft.Text(result, text_align=ft.TextAlign.CENTER, size=30)
                    ]
                )
            )
        )

        page.add(content_container)
        # Render the extracted parts (text, images, videos)
        render_content(content_container.content.content, parts, video_files)
