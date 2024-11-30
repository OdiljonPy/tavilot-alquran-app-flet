import flet as ft
import requests
import os


def registration_response(phone, passw, page):
    url = "https://alquran.zerodev.uz/api/v1/auth/register/"
    headers = {
        "Content-Type": "application/json",
    }
    phone_number = f'+998{phone.value}'
    data = {
        "phone_number": phone_number,
        'password': passw.value
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.json())
    otp_key = response.json().get('result')
    if response.status_code == 200:
        pass

    else:
        print('Error')
    page.update()


def registration_page(page):
    page.clean()
    from ..main import main
    from tavilot_al_quran.utils.common_variables import password
    from tavilot_al_quran.utils.validations import limit_length
    TC = '#E9BE5F'

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
    # Create a Column for all the fields on the left side
    registration = ft.Container(content=ft.Row(
        adaptive=True,
        controls=[ft.Column(
            adaptive=True,
            controls=[
                ft.Text(value="  TA'VILOT \nAL-QURON \n", color=TC, style="displayLarge"),
                ft.Text(value="Assalomu alaykum! \nDavom etish uchun ro'yxatdan o'ting\n", width=400, weight='bold',
                        style="titleLarge"),
                phone_input,
                password,
                ft.Text(),
                ft.OutlinedButton(
                    text="Davom etish",
                    on_click=lambda e: registration_response(phone_input, password, page),
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
                    text="Parol orqali kirish",
                    on_click=lambda e: main(page),
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
        ),
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
    ),
        adaptive=True,
        expand=True,
        alignment=ft.alignment.center
    )
    page.add(registration)
