import flet as ft
import os
import requests
from .html_pdf_handler import extract_base64_and_save_images, extract_and_process_videos, render_content
from .pdf_page import pdf_page

def take_content_id(page, back_button, ids):
    page.scroll = True
    page.clean()

    loading = ft.ProgressRing()

    page.add(ft.Container(
        content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center))

    page.update()
    url = f"http://176.221.28.202:8008/api/v1/resources/{ids}/"
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
            height=page.window.height,
            margin=30,
            image_src=os.path.abspath("assets/searchbg.png"),
            image_fit="cover",
            alignment=ft.alignment.center,
            content=ft.Container(
                alignment=ft.alignment.center,
                scale=ft.Scale(scale_x=0.9),
                bgcolor='white',
                content=ft.Column(
                    scale=ft.Scale(scale_x=0.9),
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(controls=[back_button], alignment=ft.MainAxisAlignment.START),
                        ft.Text(result, text_align=ft.TextAlign.CENTER, size=30)
                    ]
                )
            )
        )

        def on_resize(event):
            content_container.height = page.window.height
            page.update()
        page.on_resize = on_resize

        page.add(content_container)
        # Render the extracted parts (text, images, videos)
        render_content(content_container.content.content, parts, video_files)
        if response.json().get('result').get('file'):
            pdf = ft.Container(
                adaptive=True,
                alignment=ft.alignment.center,
                content=ft.Image(src=os.path.abspath("assets/pdf.png"), width=100, height=100, expand=True),
                on_click=lambda e: pdf_page(page, response.json().get('result').get('file'), back_button)
            )

            content_container.content.content.controls.append(pdf)


        page.update()