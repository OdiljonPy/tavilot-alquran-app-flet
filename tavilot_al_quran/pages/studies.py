import flet as ft
import os
import requests
from .studies_detail import take_content_id



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

def studies(page):
    from .home_page import home
    current_language = "uz"

    page.scroll = True
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
        on_click=lambda e: home(page),
    )

    page.update()

    url = "http://176.221.28.202:8008/api/v1/studies/"
    response = requests.get(url=url)
    print(response.json())
    data_list = ft.Row(wrap=True, expand=True, scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                       adaptive=True)

    if response.status_code == 200:
        page.clean()
        datas = response.json().get('result')
        for date in datas:
            motrudiy_data = ft.OutlinedButton(
                adaptive=True,
                data=date.get('id'),
                on_click=lambda e: take_content_id(page, e.control.data),
                content=ft.Column(
                    controls=[
                        ft.Column(controls=[
                            ft.Text(),
                            ft.Image(src=os.path.abspath("assets/book_1.svg"), color="white"),
                            ft.Text(f"\n{date.get('title')}", size=20, color='white'),
                        ])
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                ),
                height=250,
                width=410,
                style=ft.ButtonStyle(
                    bgcolor=TC,
                    shape=ft.RoundedRectangleBorder(radius=14),
                ),

            )
            data_list.controls.append(motrudiy_data)
        page.update()

    divider = ft.Divider(height=30, color='white')
    page.add(divider, ft.Container(
        margin=15,
        adaptive=True,
        expand=True,
        alignment=ft.alignment.center_left,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.START,
            adaptive=True,
            controls=[
                back_button,
                ft.Text(height=70),
                data_list
            ]
        )
    )
             )