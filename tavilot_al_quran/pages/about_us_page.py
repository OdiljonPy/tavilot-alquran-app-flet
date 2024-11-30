import flet as ft
import time
import requests


def about_us_page(page, navbar_text1, navbar_text2, navbar_text3):
    page.clean()
    loading = ft.ProgressRing()
    page.add(ft.Container(
        content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center))

    time.sleep(0.7)

    page.clean()
    navbar_text3.style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color='#007577')
    navbar_text3.color = '#007577'
    navbar_text1.style = None
    navbar_text1.color = 'black'
    navbar_text2.style = None
    navbar_text2.color = 'black'
    page.update()

    about_result = ft.Text(value='')
    container = ft.Container(content=ft.Column(controls=[about_result], scroll=ft.ScrollMode.ALWAYS),
                             alignment=ft.alignment.center)

    page.update()
    url = "https://alquran.zerodev.uz/api/v1/about/"
    response = requests.get(url=url)
    if response.status_code == 200:
        about_result.value = response.json().get('result').get('description')
        page.update()
    else:
        about_result.value = None
        page.update()
    page.add(container)
