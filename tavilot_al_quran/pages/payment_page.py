import flet as ft
import os
import webbrowser
import requests
import base64



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


def payment_page(page):
    from .home_page import home
    current_language = "uz"

    TC = '#E9BE5F'
    page.clean()

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


    text_premium = ft.Row(
        adaptive=True,
        controls=[ft.Container(
            expand=True,
            adaptive=True,
            alignment=ft.alignment.center,
            margin=40,
            content=ft.Row(
                controls=[
                    ft.Text('Premium version', color=TC, size=40, weight='bold')
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            image_src=os.path.abspath("assets/searchbg.png"),
            width=1000,
            height=200,
            image_fit='cover',
            image_opacity=0.5,
            padding=50

        )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    description_text = ft.Row(controls=[
        ft.Text('Премиум версия орқали қуйидаги ҳусусиятларга эга бӯласиз', size=15, expand=True,
                text_align=ft.TextAlign.CENTER)
    ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    url = ''
    def payment_request(e, urls):
        if e.control == click_button:
            click_button.style.side = ft.BorderSide(color=TC, width=3)
            payme_button.style.side = ft.BorderSide(color='white', width=3)
            nonlocal url
            url = urls

        elif e.control == payme_button:
            payme_button.style.side = ft.BorderSide(color=TC, width=3)
            click_button.style.side = ft.BorderSide(color='white', width=3)
            url = urls

        page.update()

    payment_url = 'http://176.221.28.202:8008/api/v1/auth/check/subscription/'

    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {page.client_storage.get('access_token')}'
    }

    response = requests.get(url=payment_url, headers=headers)

    if response.status_code == 200:
        amount = response.json()
        user_id = response.json().get('user_id')
        url=f"https://my.click.uz/services/pay?service_id=39892&merchant_id=32039&amount={amount.get('prays_click')}&transaction_param={user_id}"
        click_url = f"https://my.click.uz/services/pay?service_id=39892&merchant_id=32039&amount={amount.get('prays_click')}&transaction_param={user_id}"
        data=f'm=6746cfafd33fb8548ceca73e;ac.user_id={user_id};a={amount.get('prays_payme')}'
        encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        payme_url = f'https://checkout.paycom.uz/{encoded_data}'


    click_button = ft.OutlinedButton(
        data=1,
        width=90,
        height=90,
        on_click=lambda e: payment_request(e, click_url),
        style=ft.ButtonStyle(side=ft.BorderSide(color=TC, width=3),
                             shape=ft.RoundedRectangleBorder(radius=8)),
        content=ft.Image(src=os.path.abspath("assets/click_icon.png"))
    )

    payme_button = ft.OutlinedButton(
        data=2,
        width=90,
        height=90,
        on_click=lambda e: payment_request(e, payme_url),
        style=ft.ButtonStyle(side=ft.BorderSide(color='white', width=3),
                             shape=ft.RoundedRectangleBorder(radius=8)),
        content=ft.Image(src=os.path.abspath("assets/payme_icon.png"))
    )

    payment_text = ft.Row(controls=[
        ft.Text("To'lov uchun o'zingizga qulay bo'lgan ilovani tanlang", size=15,
                text_align=ft.TextAlign.CENTER),
        click_button,
        payme_button
    ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    def redirect_to_pay(url):
        print(url)
        webbrowser.open(url)

    pay_button = ft.Container(
        adaptive=True,
        alignment=ft.alignment.center,
        content=ft.OutlinedButton(
            on_click=lambda e: redirect_to_pay(url),
            width=700,
            height=60,
            adaptive=True,
            expand=True,
            content=ft.Text(value='Xarid qilish', text_align=ft.TextAlign.CENTER, color=TC),
            style=ft.ButtonStyle(
                side=ft.BorderSide(color=TC, width=3),
                shape=ft.RoundedRectangleBorder(radius=8)),
        ))

    page.update()

    page.add(text_premium, description_text, payment_text, ft.Text(height=40), pay_button)
