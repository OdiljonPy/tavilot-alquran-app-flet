import flet as ft
import os


def payment_page(page, back_button):
    TC = '#E9BE5F'
    page.clean()

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

    def payment_request(e):
        if e.control == click_button:
            click_button.style.side = ft.BorderSide(color=TC, width=3)
            payme_button.style.side = ft.BorderSide(color='white', width=3)

        elif e.control == payme_button:
            payme_button.style.side= ft.BorderSide(color=TC, width=3)
            click_button.style.side = ft.BorderSide(color='white', width=3)

        page.update()

    click_button = ft.OutlinedButton(
        data=1,
        width=100,
        height=100,
        on_click=payment_request,
        style=ft.ButtonStyle(side=ft.BorderSide(color=TC, width=3),
                             shape=ft.RoundedRectangleBorder(radius=8)),
        content=ft.Image(src=os.path.abspath("assets/click_icon.png"))
    )

    payme_button = ft.OutlinedButton(
        data=2,
        width=100,
        height=100,
        on_click=payment_request,
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



    page.update()

    page.add(text_premium, description_text, payment_text)
