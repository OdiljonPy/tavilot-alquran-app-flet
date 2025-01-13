import flet as ft
import os
import requests
from .menuscript_detail import take_content_id

def menuscript(page, back_button):
    page.scroll = True
    page.clean()
    TC = '#E9BE5F'
    loading = ft.ProgressRing()

    page.add(ft.Container(
        content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center))

    page.update()

    url = "http://176.221.28.202:8008/api/v1/manuscript/"
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
                on_click=lambda e: take_content_id(page, back_button, e.control.data),
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