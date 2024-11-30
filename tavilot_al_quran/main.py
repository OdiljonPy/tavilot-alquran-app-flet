import time
import flet as ft
import os
from utils.validations import limit_length
import requests
from utils.common_variables import password
from pages.register_page import registration_page
from pages.home_page import home


def main(page: ft.Page):
    page.expand = True
    page.padding = 0
    page.clean()
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Column(
        adaptive=True,
        height=page.window_height,
        width=page.window_width,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("TA'VILOT\nAL-QURAN", size=100, text_align=ft.TextAlign.CENTER, color="#E9BE5F")
        ]
    )
    ))

    time.sleep(4)

    page.clean()
    page.adaptive = True
    page.window_min_width = 1250
    page.window_min_height = 800
    page.theme_mode = ft.ThemeMode.LIGHT

    # result = ft.Text(value="", color="red")
    TC = '#E9BE5F'
    result = ft.Text(value="", color="red")

    phone_input = ft.TextField(
        label='Phone number',
        prefix_text="+998 ",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=400,
        on_change=lambda e: limit_length(phone_input, page),
        border_width=2,
        border_radius=10,
        border_color=TC,
        text_style=ft.TextStyle(weight="bold")
    )

    def login_response(phone, passw, result_):
        page.clean()
        loading = ft.ProgressRing()
        page.add(ft.Container(
            content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
            alignment=ft.alignment.center))

        url = "https://alquran.zerodev.uz/api/v1/auth/login/"
        headers = {
            "Content-Type": "application/json",
        }
        phone_number = f'+998{phone.value}'
        data = {
            "phone_number": phone_number,
            'password': passw.value
        }
        response = requests.post(url=url, json=data, headers=headers)
        print(response.json())
        page.client_storage.set('access_token', response.json().get('result').get('access_token'))
        page.update()

        if response.status_code == 200:
            home(page)
        else:
            main(page)
        page.update()

    # Create a Column for all the fields on the left side

    content_column = ft.Column(
        adaptive=True,
        controls=[
            ft.Text(value="  TA'VILOT \nAL-QURON \n", color=TC, style="displayLarge"),
            ft.Text(value="Assalomu alaykum! \nDavom etish uchun ro'yxatdan o'ting\n", width=400, weight='bold',
                    style="titleLarge"),
            phone_input,
            password,
            result,
            ft.Text(),
            ft.OutlinedButton(
                text="Davom etish",
                on_click=lambda e: login_response(phone_input, password, result),
                # Link the button to validation
                width=400,
                height=60,
                style=ft.ButtonStyle(
                    color='white',
                    bgcolor=TC,
                    shape=ft.RoundedRectangleBorder(radius=8),
                )
            ),
            ft.OutlinedButton(
                text="Ro'yxatdan o'tish",
                on_click=lambda e: registration_page(page),
                # Link the button to validation
                width=400,
                height=60,
                style=ft.ButtonStyle(
                    color='white',
                    bgcolor=TC,
                    shape=ft.RoundedRectangleBorder(radius=8),

                ),
            ),

        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    # Define a Row that contains the content column and the image with rounded borders
    layout_with_image = ft.Row(
        adaptive=True,
        controls=[
            content_column,
            ft.Container(
                content=ft.Image(
                    src=os.path.abspath("assets/tavilot_book.png"),
                    width=700,
                    height=900,
                    fit=ft.ImageFit.COVER,
                    border_radius=100
                ),
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  # Enable anti-aliasing for smoother edges
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,  # Spread content and image to left and right
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Wrap layout_with_image in a Container to center it on the page
    centered_container = ft.Container(
        adaptive=True,
        content=layout_with_image,
        alignment=ft.alignment.center,  # Center the entire row in the middle of the page
        expand=True,  # Make the container expand to fill the page
    )

    # Add the centered container to the page
    page.add(centered_container)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
