import flet as ft
import os
import requests
from .htmp_parser import FletifyHTML


def take_content_id(page, back_button, ids):
    page.clean()

    loading = ft.ProgressRing()

    page.add(ft.Container(
        content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center))

    page.update()
    url = f"http://176.221.28.202:8008/api/v1/resources/{ids}/"
    response = requests.get(url=url)
    print(response.json())
    response_data = FletifyHTML(response.json().get('result').get('description')).get_flet()
    print(response_data)

    if response.status_code == 200:
        page.clean()

        detail_content = ft.Container(
            margin=50,
            image_src=os.path.abspath("assets/searchbg.png"),
            image_fit="cover",
            alignment=ft.alignment.center,
            content=ft.Container(
                scale=ft.Scale(scale_x=0.9),
                bgcolor='white',
                content=ft.Column(
                    controls=[
                        back_button,
                        response_data
                    ]
                )
            )
        )
        page.add(detail_content)
