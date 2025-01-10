import flet as ft
import os
import requests
from .menuscript_detail import take_content_id

def menuscript(page, back_button):
    TC = '#E9BE5F'
    page.clean()

    loading = ft.ProgressRing()

    page.add(ft.Container(
        content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center))

    page.update()

    url = "http://176.221.28.202:8008/api/v1/manuscript/"
    response = requests.get(url=url)
    print(response.json())
    data_list = ft.Row(wrap=True, expand=True, scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START)

    if response.status_code == 200:
        page.clean()
        datas = response.json().get('result')
        for date in datas:
            motrudiy_data = ft.OutlinedButton(
                data=date.get('id'),
                on_click=lambda e: take_content_id(page, back_button, e.control.data),
                content=ft.Column(
                                    controls=[
                                        ft.Column(controls=[
                                            ft.Text(),
                                            ft.Image(src=os.path.abspath("assets/book_1.svg"), color="white"),
                                            ft.Text(f"\n{date.get('title')}", size=22, color='white'),
                                        ])
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                                ),
                                    height=240,
                                    width=560,
                                    style=ft.ButtonStyle(
                                        bgcolor=TC,
                                        shape=ft.RoundedRectangleBorder(radius=14),
                                    ),

                                )
            data_list.controls.append(motrudiy_data)
        page.update()


    divider = ft.Divider(height=30, color='white')
    page.add(divider, back_button, ft.Container(alignment=ft.alignment.center, content=data_list))
