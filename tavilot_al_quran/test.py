import flet as ft
import requests


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    def login_response(e):
        # page.clean()
        # loading = ft.ProgressRing()
        # page.add(ft.Container(
        #     content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
        #     alignment=ft.alignment.center))

        url = "https://alquran.zerodev.uz/api/v1/auth/login/"
        headers = {
            "Content-Type": "application/json",
        }
        # phone_number = f'+998{phone.value}'
        data = {
            "phone_number": "+998903924787",
            'password': "1"
        }
        response = requests.post(url=url, json=data, headers=headers)
        print(response.json())
        page.client_storage.set('access_token', response.json().get('result').get('access_token'))
        page.update()

        print(page.client_storage.get('access_token'))

        url = "https://alquran.zerodev.uz/api/v1/auth/me/"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {page.client_storage.get('access_token')}'
        }
        response_me = requests.get(url=url, headers=headers)
        print(response_me.json())

    page.add(ft.TextButton('Click for login', on_click=login_response))



ft.app(target=main)
