import time
import asyncio
import flet as ft
import os

from utils.validations import limit_length
import requests
from pages.home_page import home


def main(page: ft.Page):
    TC = '#E9BE5F'
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
    time.sleep(2)
    page.clean()
    page.adaptive = True
    page.expand = True
    page.window_min_width = 1250
    page.window_min_height = 800
    page.theme_mode = ft.ThemeMode.LIGHT

    #------Enter without registration button----------------------------------------------------------------------------

    enter_button = ft.Row(
        alignment=ft.MainAxisAlignment.END,
        controls=[
            ft.OutlinedButton(
                text="Dasturga kirish",
                on_click=lambda e: home(page),
                # Link the button to validation
                width=200,
                height=60,
                style=ft.ButtonStyle(
                    color='white',
                    bgcolor=TC,
                    shape=ft.RoundedRectangleBorder(radius=8),
                )
            ),
            ft.Text()
        ]
    )

    # -----Registration page---------------------------------------------------------------------------------------------

    register_result = ft.Text(color='red', size=15)

    def registration_response(phone, passw):
        url = "http://alquran.zerodev.uz/api/v1/auth/register/"
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
        if response.status_code == 201:
            otp_key = response.json().get('result').get('otp_key')
            go_to_otp_page(page, otp_key, phone_input)
        elif response.json().get('error_code') == 6:
            register_result.value = 'User already exist'
            phone_input.border_color = 'red'
        elif response.json().get('error_code') == 1:
            register_result.value = 'Too many attmepts! Try later.'
            phone_input.border_color = 'red'
        else:
            register_result.value = 'Invalid phone number'
            phone_input.border_color = 'red'
        page.update()


    def on_password_change(p, phone):
        print(p, phone)
        if p.value and phone.value:
            continue_button_login.disabled = False
            continue_button_registration.disabled = False
        page.update()

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

    password = ft.TextField(
        on_change=lambda e: on_password_change(password, phone_input),
        label='Password',
        password=True,
        can_reveal_password=True,
        width=400,
        border_width=2,
        border_radius=10,
        border_color=TC,
        text_style=ft.TextStyle(weight="bold"),
    )

    continue_button_registration = ft.OutlinedButton(
        disabled=True,
        text="Davom etish",
        on_click=lambda e: registration_response(phone_input, password),
        # Link the button to validation
        width=400,
        height=60,
        style=ft.ButtonStyle(
            color='white',
            bgcolor=TC,
            shape=ft.RoundedRectangleBorder(radius=8),
        )
    )

    def registration_page(e):
        page.clean()
        TC = '#E9BE5F'

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
                    register_result,
                    ft.Text(),
                    continue_button_registration,
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

    # -----Login page---------------------------------------------------------------------------------------------

    # result = ft.Text(value="", color="red")
    TC = '#E9BE5F'
    login_result = ft.Text(value="", color="red")

    continue_button_login = ft.OutlinedButton(
        disabled=True,
        text="Davom etish",
        on_click=lambda e: login_response(phone_input, password),
        width=400,
        height=60,
        style=ft.ButtonStyle(
            color='white',
            bgcolor=TC,
            shape=ft.RoundedRectangleBorder(radius=8),
        )
    )

    def login_response(phone, passw):
        url = "http://alquran.zerodev.uz/api/v1/auth/login/"
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
        if response.status_code == 200:
            page.clean()
            loading = ft.ProgressRing()
            page.add(ft.Container(
                expand=True,
                adaptive=True,
                content=loading,
                alignment=ft.alignment.center))
            time.sleep(0.6)
            page.client_storage.set('access_token', response.json().get('result').get('access_token'))
            page.update()
            home(page)
        elif response.json().get('error_code') == 5:
            phone_input.border_color = 'red'
            login_result.value = "User with this phone number does not exist"
        else:
            phone_input.border_color = 'red'
            password.border_color = 'red'
            login_result.value = 'Phone number or password is invalid'
        page.update()

    # Create a Column for all the fields on the left side

    content_column = ft.Column(
        adaptive=True,
        controls=[
            ft.Text(value="  TA'VILOT \nAL-QURON \n", color=TC, style="displayLarge"),
            ft.Text(value="Assalomu alaykum! \nTelefon raqam va parolingizni kiriting\n", width=400, weight='bold',
                    style="titleLarge"),
            phone_input,
            password,
            login_result,
            ft.Text(),
            continue_button_login,
            ft.OutlinedButton(
                text="Ro'yxatdan o'tish",
                on_click=registration_page,
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
                    width=650,
                    height=800,
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

    # ---OTP page--------------------------------------------------------------------------------------------------------

    # Create six text fields
    text_fields = [ft.TextField(width=57, text_align=ft.TextAlign.CENTER) for _ in range(6)]

    # Function to automatically move focus to next or previous field
    def on_change(e):
        # Get the current field index
        current_index = text_fields.index(e.control)
        # If the input is a number and the field has more than one digit, clear extra digits
        if e.control.value.isdigit() and len(e.control.value) > 1:
            e.control.value = e.control.value[0]  # Keep only the first digit
            e.control.update()
        # If the input is a number and the field has exactly one digit, move to the next field
        if e.control.value.isdigit() and len(e.control.value) == 1:
            next_field_index = current_index + 1
            if next_field_index < len(text_fields):
                text_fields[next_field_index].focus()
        # If the input is cleared, move to the previous field
        elif e.control.value == "":
            prev_field_index = current_index - 1
            if prev_field_index >= 0:
                text_fields[prev_field_index].focus()

    # Function to collect all numbers into one variable
    def collect_otp():
        otp = "".join(field.value for field in text_fields if field.value.isdigit())
        print(f"Collected OTP: {otp}")
        return otp

    # Attach the on_change event to each text field
    for text_field in text_fields:
        text_field.on_change = on_change
    # Add text fields to a row to display them in a horizontal line
    row = ft.Row(adaptive=True, controls=text_fields)
    print(row.controls)

    # -----OTP Countdown------------------------------------------------------------------------------------------------
    class Countdown(ft.Text):
        def __init__(self, seconds, button_to_enable=None):
            super().__init__()
            self.seconds = seconds
            self.button_to_enable = button_to_enable

        def did_mount(self):
            self.running = True
            self.page.run_task(self.update_timer)

        def will_unmount(self):
            self.running = False

        async def update_timer(self):
            while self.seconds >= 0 and self.running:
                mins, secs = divmod(self.seconds, 60)
                self.value = "{:2d}:{:02d}".format(mins, secs)
                self.update()
                await asyncio.sleep(1)
                self.seconds -= 1

            if self.button_to_enable:
                self.button_to_enable.disabled = False
                self.button_to_enable.content.color = TC
                self.button_to_enable.style.side = ft.BorderSide(color=TC, width=1)
                self.button_to_enable.update()

    # -------------------------------------------------------------------------------------------------------------------

    otp_result = ft.Text(value='\nParolni kiriting', color=TC, size=20, text_align=ft.TextAlign.LEFT,
                                    width=400)

    resend_button = ft.OutlinedButton(
        disabled=True,
        content=ft.Text('Qaytadan yuborish!', color="grey"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            side=ft.BorderSide(color='grey', width=1)
        )
    )

    def otp_verify(key_otp):
        url = "http://alquran.zerodev.uz/api/v1/auth/verify/"
        headers = {
            "Content-Type": "application/json",
        }
        print(collect_otp())
        data = {
            'otp_code': collect_otp(),
            'otp_key': key_otp
        }
        print(data)
        response = requests.post(url=url, json=data, headers=headers)
        print(response)
        if response.status_code == 200:
            main(page)
        else:
            otp_result.value = 'Parolni xato kiritdingiz'
            otp_result.color = 'red'
        page.update()

    def go_to_otp_page(page, otp, phone_number):
        page.clean()
        page.add(ft.Container(
            adaptive=True,
            content=ft.Row(
                adaptive=True,
                controls=[
                    ft.Column(
                        adaptive=True,
                        controls=[
                            ft.Text(value="  TA'VILOT \nAL-QURON \n", color=TC, style="displayLarge"),
                            ft.Text(value=f"Parol ushbu raqamga jonatildi \n+998{phone_number.value}", width=400,
                                    weight='bold',
                                    style="titleLarge"),
                            otp_result,
                            ft.Text(),
                            ft.Row(
                                spacing=218,
                                controls=[
                                    Countdown(5, button_to_enable=resend_button),
                                    resend_button,
                                ]
                            ),
                            row,
                            ft.Text(),
                            ft.OutlinedButton(
                                text="Davom etish",
                                on_click=lambda e: otp_verify(otp),
                                # Link the button to validation
                                width=400,
                                height=60,
                                style=ft.ButtonStyle(
                                    color='white',
                                    bgcolor=TC,
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                )
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
            alignment=ft.alignment.center,  # Center the entire row in the middle of the page
            expand=True,  # Make the container expand to fill the page
        ))

    # ------------------------------------------------------------------------------------------------------------------
    # Add the centered container to the page
    page.add(enter_button, centered_container)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
