import os

from .html_pdf_handler import extract_and_process_videos, extract_base64_and_save_images, render_content
from .pdf_page import pdf_page
import flet as ft
import requests


translations = {
    "uz": {
        "back_button_text": "Orqaga qaytish",
        "three_window_moturudiy": "\n   Abu Mansur Matrudiy",
    },
    "kr": {
        "back_button_text": "Оркага кайтиш",
        "three_window_moturudiy": "\n   Абу Мансур Мотрудий",
    }
}


def take_content_id(page, ids):
    from .al_quran_oquvchilariga import al_quron_oquvchilariga
    current_language = "uz"

    page.scroll = False
    page.clean()
    TC = '#E9BE5F'

    loading = ft.ProgressRing(color=TC)
    page.add(ft.Container(
        expand=True,
        adaptive=True,
        content=loading,
        alignment=ft.alignment.center)
    )

    back_button_text = ft.Text(value=translations[current_language]["back_button_text"], color='black')


    back_button = ft.OutlinedButton(
        content=ft.Row(controls=[
            ft.Icon(ft.icons.ARROW_BACK, color='black', size=20),
            back_button_text
        ]),
        height=40,
        width=170,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(color=TC, width=1),
            bgcolor='white'

        ),
        adaptive=True,
        on_click=lambda e: al_quron_oquvchilariga(page),
    )

    page.update()
    url = f"http://alquran.zerodev.uz/api/v2/moturudiy/{ids}/"
    response = requests.get(url=url)
    response_data = response.json().get('result').get('description')

    # Process HTML to handle base64 images and videos
    parts, result = extract_base64_and_save_images(response_data)
    video_files = extract_and_process_videos(response_data)

    if response.status_code == 200:
        page.clean()
        page.scroll = True
        # Container to hold the rendered content
        content_container = ft.Container(
            height=page.window.height,
            scale=ft.Scale(scale_x=0.96),
            image_src=os.path.abspath("assets/searchbg.png"),
            image_fit="cover",
            alignment=ft.alignment.center,
            content=ft.Container(
                alignment=ft.alignment.center,
                scale=ft.Scale(scale_x=0.9),
                bgcolor='white',
                content=ft.Column(
                    scale=ft.Scale(scale_x=0.96),
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
        render_content(content_container.content.content, parts, video_files, page)
        if response.json().get('result').get('file'):
            pdf = ft.Container(
                adaptive=True,
                alignment=ft.alignment.center,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(src=os.path.abspath("assets/pdf.png"), width=240, height=160, expand=True),
                        ft.Text(response.json().get('result').get('file_name'), text_align=ft.TextAlign.CENTER, size=30, color=TC)
                        ]
                ),
                on_click=lambda e: pdf_page(page, response.json().get('result').get('file'), back_button)
            )

            content_container.content.content.controls.append(pdf)

        page.update()
