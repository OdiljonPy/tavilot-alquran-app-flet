import os
from .html_pdf_handler import extract_and_process_videos, extract_base64_and_save_images, render_content
from .pdf_page import pdf_page
import flet as ft
import requests

def take_content_id(page, back_button, ids):
    page.clean()

    loading = ft.ProgressRing()

    page.add(
        ft.Container(
            expand=True,
            content=ft.Column(
                expand=True,
                controls=[loading],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )
    )

    page.update()
    url = f"http://176.221.28.202:8008/api/v1/moturudiy/{ids}/"
    response = requests.get(url=url)
    print(response.json())
    response_data = response.json().get('result').get('description')
    print(response_data)

    # Process HTML to handle base64 images and videos
    parts, result = extract_base64_and_save_images(response_data)
    video_files = extract_and_process_videos(response_data)

    if response.status_code == 200:
        page.clean()
        page.scroll = True
        # Container to hold the rendered content
        content_container = ft.Container(
            height=page.window.height,
            adaptive=True,
            margin=30,
            image_src=os.path.abspath("assets/searchbg.png"),
            image_fit="cover",
            alignment=ft.alignment.center,
            content=ft.Container(
                adaptive=True,
                alignment=ft.alignment.center,
                scale=ft.Scale(scale_x=0.9),
                bgcolor='white',
                content=ft.Column(
                    scale=ft.Scale(scale_x=0.9),
                    adaptive=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(controls=[back_button], alignment=ft.MainAxisAlignment.START),
                        ft.Row(
                            adaptive=True,
                            wrap=True,
                            controls=[
                                ft.Text(result, size=10),
                            ]
                        )
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
