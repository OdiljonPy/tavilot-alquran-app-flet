import flet as ft
import requests
import os

TC = '#E9BE5F'


def surah_page(page):
    page.clean()
    page.scroll = False
    list_display = ft.ListView(expand=True, spacing=10, padding=20, adaptive=True)
    right_display = ft.ListView(expand=True, spacing=10, padding=20, adaptive=True)
    # ------Back connection----------------------------------------------------------------------------------------------
    url = "https://alquran.zerodev.uz/api/v1/chapters/"
    response = requests.get(url=url)
    if response.status_code == 200:
        result_lists = response.json().get('result')

        for i in result_lists:
            if i.get('type_choice') == 1:
                i['type_choice'] = 'Makkiy'
            else:
                i['type_choice'] = 'Madaniy'

            list_display.controls.append(ft.Container(
                data=i.get('id'),
                on_click=lambda e: take_id(e.control.data),
                expand=True,
                content=ft.Row(controls=[
                    ft.Container(content=ft.Text(i.get('id'), color='black'), shape=ft.BoxShape.CIRCLE, width=60,
                                 height=60, alignment=ft.alignment.center, border=ft.border.all(2, color=TC)),
                    ft.Column(controls=[
                        ft.Text(i.get('name'), size=20),
                        ft.Text(f"{i.get('type_choice')}, {i.get('verse_number')} oyat", size=10)
                    ]),
                    ft.Text(i.get('name_arabic'), size=15, text_align=ft.TextAlign.RIGHT, width=150)
                ])))
    else:
        print('Error')

    # --------------------------------------------------------------------------------------------------------------------
    def take_id(ids):
        right_display.controls.clear()
        urls = f"https://alquran.zerodev.uz/api/v1/chapter/{ids}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {page.client_storage.get('access_token')}'
        }
        responses = requests.get(url=urls, headers=headers)
        if responses.status_code == 200:
            result_details = responses.json().get('result').get('verses')

            def change_response(e):
                if e.control == text_arabic:
                    right_display.controls.clear()
                    right_display.controls.append(right_top_bar)
                    text_arabic.style.color = "white"
                    text_arabic.style.bgcolor = TC
                    text_translate.style.color = ft.colors.BLACK
                    text_translate.style.bgcolor = ft.colors.GREY_200
                    text_tafsir.style.color = ft.colors.BLACK
                    text_tafsir.style.bgcolor = ft.colors.GREY_200
                    for result_detail in result_details:
                        right_display.controls.append(ft.Column(controls=[ft.Row(
                            wrap=True,
                            alignment=ft.MainAxisAlignment.END,
                            adaptive=True,
                            controls=[
                                ft.Container(
                                    image_src=os.path.abspath("assets/Union.png"),
                                    alignment=ft.alignment.center,
                                    width=50,
                                    height=50,
                                    adaptive=True,
                                    content=ft.Text(value=f"{result_detail.get('number')}")
                                ),
                                ft.Text(value=f"{result_detail.get('text_arabic')}", size=20),
                            ]),
                            ft.Divider(color=TC)
                        ])
                        )
                elif e.control == text_translate:
                    right_display.controls.clear()
                    right_display.controls.append(right_top_bar)
                    text_translate.style.color = 'white'
                    text_translate.style.bgcolor = TC
                    text_arabic.style.color = ft.colors.BLACK
                    text_arabic.style.bgcolor = ft.colors.GREY_200
                    text_tafsir.style.color = ft.colors.BLACK
                    text_tafsir.style.bgcolor = ft.colors.GREY_200
                    for result_detail in result_details:
                        right_display.controls.append(ft.Column(controls=[ft.Row(
                            wrap=True,
                            alignment=ft.MainAxisAlignment.END,
                            adaptive=True,
                            controls=[
                                ft.Container(
                                    image_src=os.path.abspath("assets/Union.png"),
                                    alignment=ft.alignment.center,
                                    width=50,
                                    height=50,
                                    adaptive=True,
                                    content=ft.Text(value=f"{result_detail.get('number')}")
                                ),
                                ft.Text(value=f"{result_detail.get('text_arabic')}", size=20),
                            ]),
                            ft.Divider(color=TC)
                        ])
                        )
                elif e.control == text_tafsir:
                    right_display.controls.clear()
                    right_display.controls.append(right_top_bar)
                    text_tafsir.style.color = "white"
                    text_tafsir.style.bgcolor = TC
                    text_arabic.style.color = ft.colors.BLACK
                    text_arabic.style.bgcolor = ft.colors.GREY_200
                    text_translate.style.color = ft.colors.BLACK
                    text_translate.style.bgcolor = ft.colors.GREY_200
                    for result_detail in result_details:
                        right_display.controls.append(ft.Column(controls=[ft.Row(
                            wrap=True,
                            alignment=ft.MainAxisAlignment.END,
                            adaptive=True,
                            controls=[
                                ft.Container(
                                    image_src=os.path.abspath("assets/Union.png"),
                                    alignment=ft.alignment.center,
                                    width=50,
                                    height=50,
                                    adaptive=True,
                                    content=ft.Text(value=f"{result_detail.get('number')}")
                                ),
                                ft.Text(value=f"{result_detail.get('text_arabic')}", size=20),
                            ]),
                            # ft.Divider(color=TC)
                        ])
                        )
                page.update()  # Update the page to reflect changes

            text_arabic = ft.TextButton('Arabcha', data=1, style=ft.ButtonStyle(color='white', bgcolor=TC),
                                        on_click=change_response)
            text_translate = ft.TextButton('Tarjima', data=2,
                                           style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                                           on_click=change_response)
            text_tafsir = ft.TextButton('Tafsir', data=3,
                                        style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                                        on_click=change_response)
            right_top_bar = ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                border_radius=20,
                height=30,
                width=225,
                bgcolor=ft.colors.GREY_200,
                adaptive=True,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    adaptive=True,
                    controls=[
                        text_arabic,
                        text_translate,
                        text_tafsir
                    ]
                )
            )
            right_display.controls.append(right_top_bar)
            for result_detail in result_details:
                right_display.controls.append(ft.Column(controls=[ft.Row(
                    wrap=True,
                    alignment=ft.MainAxisAlignment.END,
                    adaptive=True,
                    controls=[
                        ft.Container(
                            image_src=os.path.abspath("assets/Union.png"),
                            alignment=ft.alignment.center,
                            width=50,
                            height=50,
                            adaptive=True,
                            content=ft.Text(value=f"{result_detail.get('number')}")
                        ),
                        ft.Text(value=f"{result_detail.get('text_arabic')}", size=20),
                    ]),
                    ft.Divider(color=TC)
                ])
                )

        else:
            print("Error")
        page.update()

    # -------------------------------------------------------------------------------------------------------------------

    side_bar = ft.Row(
        expand=True,
        adaptive=True,
        controls=[
            ft.Container(
                height=page.window_height,
                adaptive=True,
                content=ft.Column(
                    height=page.window_height,
                    expand=True,
                    adaptive=True,
                    controls=[
                        ft.Row(controls=[
                            ft.Text('Suralar', size=23),
                            ft.Text('Juzlar', size=23),
                            ft.Text('Xatchup', size=23)
                        ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=40
                        ),
                        ft.Text(),
                        list_display
                    ]

                ),
                bgcolor='#FFFFFF',
                width=350,
            ),
            ft.Column(
                adaptive=True,
                controls=[
                    ft.Container(
                        expand=True,
                        adaptive=True,
                        bgcolor=TC,  # The line's color
                        width=5,  # Thickness of the line
                        height=page.window_height,  # Match the height of the containers
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Center the button inside the line
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,  # No space between the line and the button
            ),
            ft.Container(
                bgcolor='white',
                expand=True,
                width=page.window_width,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=page.window_width,
                    adaptive=True,
                    controls=[
                        ft.Text(height=50),
                        right_display

                    ]
                )
            )
        ],
        height=page.window_height,
        spacing=0
    )
    page.add(side_bar)
    page.update()
