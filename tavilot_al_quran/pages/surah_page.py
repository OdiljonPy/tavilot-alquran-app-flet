import flet as ft
import requests

TC = '#E9BE5F'


def surah_page(page):
    page.clean()
    page.scroll = False
    list_display = ft.ListView(expand=1, spacing=10, padding=20, adaptive=True)
    right_display = ft.ListView(expand=1, spacing=10, padding=20, adaptive=True)
    #------Back connection----------------------------------------------------------------------------------------------
    url = "https://alquran.zerodev.uz/api/v1/chapters/"
    response = requests.get(url=url)
    if response.status_code == 200:
        result_lists = response.json().get('result')
        print(result_lists)

        for i in result_lists:
            if i.get('type_choice') == 1:
                i['type_choice'] = 'Makkiy'
            else:
                i['type_choice'] = 'Madaniy'

            list_display.controls.append(ft.Container(content=ft.Row(controls=[
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

    #--------------------------------------------------------------------------------------------------------------------

    url = f"https://alquran.zerodev.uz/api/v1/chapter/{1}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {page.client_storage.get('access_token')}'
    }
    response = requests.get(url=url, headers=headers)
    print(response)
    if response.status_code == 200:
        result_details = response.json().get('result')
        print(result_details)
        for result_detail in result_details:
            right_display.controls.append(ft.Container(content=ft.Row(controls=[
                # ft.Image(src=)
            ])))
    else:
        print("Error")
    #-------------------------------------------------------------------------------------------------------------------

    def change_response(e):
        if e.control == text_arabic:
            text_arabic.style.color = "white"
            text_arabic.style.bgcolor = TC
            text_translate.style.color = ft.colors.BLACK
            text_translate.style.bgcolor = ft.colors.WHITE
            text_tafsir.style.color = ft.colors.BLACK
            text_tafsir.style.bgcolor = ft.colors.WHITE
        elif e.control == text_translate:
            text_translate.style.color = 'white'
            text_translate.style.bgcolor = TC
            text_arabic.style.color = ft.colors.BLACK
            text_arabic.style.bgcolor = ft.colors.WHITE
            text_tafsir.style.color = ft.colors.BLACK
            text_tafsir.style.bgcolor = ft.colors.WHITE
        elif e.control == text_tafsir:
            text_tafsir.style.color = "white"
            text_tafsir.style.bgcolor = TC
            text_arabic.style.color = ft.colors.BLACK
            text_arabic.style.bgcolor = ft.colors.WHITE
            text_translate.style.color = ft.colors.BLACK
            text_translate.style.bgcolor = ft.colors.WHITE
        page.update()  # Update the page to reflect changes


    text_arabic = ft.TextButton('Arabcha', style=ft.ButtonStyle(color='white', bgcolor=TC), on_click=change_response)
    text_translate = ft.TextButton('Tarjima', style=ft.ButtonStyle(color='black', bgcolor='white'), on_click=change_response)
    text_tafsir = ft.TextButton('Tafsir', style=ft.ButtonStyle(color='black', bgcolor='white'), on_click=change_response)

    right_top_bar = ft.Container(
        border_radius=20,
        height=30,
        bgcolor='white',
        alignment=ft.alignment.top_center,
        adaptive=True,
        content=ft.Row(
            adaptive=True,
            controls=[
                text_arabic,
                text_translate,
                text_tafsir
            ]
        )
    )

    left_container = ft.Container(
        adaptive=True,
        content=ft.Column(
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
    )

    side_bar = ft.Row(
        adaptive=True,
        controls=[
            left_container,
            ft.Column(
                adaptive=True,
                controls=[
                    ft.Container(
                        adaptive=True,
                        bgcolor=TC,  # The line's color
                        width=5,  # Thickness of the line
                        height=3000,  # Match the height of the containers
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Center the button inside the line
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,  # No space between the line and the button
            ),
            ft.Text(width=500),
            ft.Column(
                controls=[
                    right_top_bar,
                    right_display

                ]
            )
        ],
        height=page.window_height,
        spacing=0
    )
    page.add(side_bar)
    page.update()
