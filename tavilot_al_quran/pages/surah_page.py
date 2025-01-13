import flet as ft
import requests
import os

TC = '#E9BE5F'


def surah_page(page, back_button):
    page.clean()

    loading = ft.ProgressRing()

    page.add(ft.Container(
        content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center))

    page.update()
    divider = ft.Container(
                adaptive=True,
                bgcolor=TC,  # The line's color
                width=5,  # Thickness of the line
                height=page.window_width,  # Match the height of the containers
            )

    def on_resize(event):
        divider.height = page.window_width
        page.update()

    # Attach resize event handler
    page.on_resize = on_resize

    list_display = ft.ListView(adaptive=True, spacing=10, padding=20)
    list_display_juz = ft.ListView(adaptive=True, spacing=10, padding=20)
    right_display_juz = ft.Column(spacing=40, expand=True, adaptive=True, scroll=ft.ScrollMode.HIDDEN,
                                  horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    right_display = ft.Column(spacing=40, expand=True, adaptive=True, scroll=ft.ScrollMode.HIDDEN,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    # -------Back connection juz----------------------------------------------------------------------------------------

    url = "http://alquran.zerodev.uz/api/v1/juz/"
    responses = requests.get(url=url)
    if responses.status_code == 200:
        result_lists = responses.json().get('result')

        for i in result_lists:
            list_display_juz.controls.append(ft.Container(
                data=i.get('id'),
                on_click=lambda e: take_juz_id(e.control.data),
                expand=True,
                content=ft.Row(
                    controls=[
                        ft.Container(adaptive=True, content=ft.Text(i.get('number'), color='black'), shape=ft.BoxShape.CIRCLE,
                                     width=60,
                                     height=60, alignment=ft.alignment.center, border=ft.border.all(2, color=TC)),
                        ft.Column(
                            adaptive=True,
                            controls=[
                            ft.Text(expand=True, value=f"{i.get('number')}-JUZ", size=20),
                            ft.Text(f"{i.get('title')}", size=10, expand=True)
                        ])
                    ]
                )
            ))

    def take_juz_id(ids):
        right_display.controls.clear()
        urls = f"http://alquran.zerodev.uz/api/v1/juz/{ids}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {page.client_storage.get('access_token')}'
        }
        juz_response = requests.get(url=urls, headers=headers)
        if juz_response.status_code == 200:
            juz_result_list = juz_response.json().get('result').get('chapters')

            for juz_i in juz_result_list:
                for juz_i_verse in juz_i.get('verses'):
                    right_display_juz.controls.append(ft.Column(controls=[ft.Row(
                        adaptive=True,
                        controls=[
                            ft.Container(
                                image_src=os.path.abspath("assets/Union.png"),
                                alignment=ft.alignment.center,
                                width=50,
                                height=50,
                                adaptive=True,
                                content=ft.Text(value=f"{juz_i_verse.get('number')}")
                            ),
                            ft.Text(value=f"{juz_i_verse.get('text_arabic')}", size=20, expand=True,
                                    width=page.window_width, text_align=ft.TextAlign.RIGHT, rtl=True, font_family="Amiri"),
                            ft.Text(width=10)
                        ]),
                        ft.Row(
                            controls=[
                                ft.Text(
                                    value=f"{juz_i_verse.get('number')}.{juz_i_verse.get('text')}",
                                    size=20,
                                    expand=True,
                                    width=page.window_width, text_align=ft.TextAlign.RIGHT
                                ),
                                ft.Text(width=10),
                            ]
                        ),
                        ft.Divider(color=TC)
                    ])
                    )

    # ------Back connection----------------------------------------------------------------------------------------------
    url = "http://alquran.zerodev.uz/api/v1/chapters/"
    response = requests.get(url=url)
    if response.status_code == 200:
        page.clean()
        result_lists = response.json().get('result')

        for i in result_lists:
            if i.get('type_choice') == 1:
                i['type_choice'] = 'Makkiy'
            else:
                i['type_choice'] = 'Madaniy'

            list_display.controls.append(ft.Container(
                data=i.get('id'),
                on_click=lambda e: take_id(e.control.data),
                content=ft.Row(
                    adaptive=True,
                    controls=[
                    ft.Container(adaptive=True, content=ft.Text(i.get('id'), color='black'), shape=ft.BoxShape.CIRCLE, width=60,
                                 height=60, alignment=ft.alignment.center, border=ft.border.all(2, color=TC)),
                    ft.Column(
                        controls=[
                        ft.Text(i.get('name'), size=20, expand=True),
                        ft.Text(f"{i.get('type_choice')}, {i.get('verse_number')} oyat", size=10, expand=True)
                    ]),
                    ft.Text(value=i.get('name_arabic'), size=15, text_align=ft.TextAlign.RIGHT, width=150, font_family='Amiri', expand=True)
                ])))
    else:
        print('Error')

    # --------------------------------------------------------------------------------------------------------------------
    def take_id(ids):
        right_display.controls.clear()
        urls = f"http://alquran.zerodev.uz/api/v1/chapter/{ids}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {page.client_storage.get('access_token')}'
        }
        responses = requests.get(url=urls, headers=headers)
        if responses.status_code == 200:
            result_details = responses.json().get('result').get('verses')
            print(result_details)

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
                    chapter_result = responses.json().get('result')
                    if chapter_result == 1:
                        chapter_result['type_choice'] = 'Makkada'
                    else:
                        chapter_result['type_choice'] = 'Madinada'
                    chapter_n = ft.Column(
                        adaptive=True,
                        expand=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                            ft.Text(
                                value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                                size=20)
                        ]
                    )
                    right_display.controls.append(chapter_n)
                    for result_detail in result_details:
                        right_display.controls.append(ft.Column(controls=[ft.Row(
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
                                ft.Text(value=f"{result_detail.get('text_arabic')}", size=20, expand=True,
                                        width=page.window_width, text_align=ft.TextAlign.RIGHT, rtl=True, font_family="Amiri"),
                                ft.Text(width=10)
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
                    chapter_result = responses.json().get('result')
                    if chapter_result == 1:
                        chapter_result['type_choice'] = 'Makkada'
                    else:
                        chapter_result['type_choice'] = 'Madinada'
                    chapter_n = ft.Column(
                        adaptive=True,
                        expand=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                            ft.Text(
                                value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                                size=20)
                        ]
                    )
                    right_display.controls.append(chapter_n)
                    for result_detail in result_details:
                        right_display.controls.append(ft.Column(
                            controls=[
                                ft.Row(
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
                                        ft.Text(value=f"{result_detail.get('text_arabic')}", size=20, expand=True,
                                                width=page.window_width, text_align=ft.TextAlign.RIGHT, rtl=True, font_family="Amiri"),
                                        ft.Text(width=10)
                                    ]),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            value=f"{result_detail.get('number')}.{result_detail.get('text')}",
                                            size=20,
                                            expand=True,
                                            width=page.window_width, text_align=ft.TextAlign.RIGHT
                                        ),
                                        ft.Text(width=10),
                                    ]
                                ),
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
                    chapter_result = responses.json().get('result')
                    if chapter_result == 1:
                        chapter_result['type_choice'] = 'Makkada'
                    else:
                        chapter_result['type_choice'] = 'Madinada'
                    chapter_n = ft.Column(
                        adaptive=True,
                        expand=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                            ft.Text(
                                value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                                size=20)
                        ]
                    )
                    right_display.controls.append(chapter_n)
                    for result_detail in result_details:
                        right_display.controls.append(ft.Column(controls=[ft.Row(
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
                                ft.Text(value=f"{result_detail.get('text_arabic')}", size=20, expand=True,
                                        width=page.window_width, text_align=ft.TextAlign.RIGHT, rtl=True, font_family="Amiri"),
                                ft.Text(width=10)
                            ]),
                            ft.Row(controls=[ft.Text(
                                value=f"{result_detail.get('number')}.{result_detail.get('text')}",
                                size=20,
                                expand=True,
                                width=page.window_width, text_align=ft.TextAlign.RIGHT
                            ),
                                ft.Text(width=10)
                            ]),
                            ft.Row(controls=[ft.Text(
                                value=f"{result_detail.get('description')}",
                                size=20,
                                expand=True,
                                width=page.window_width,
                                text_align=ft.TextAlign.RIGHT
                            ),
                                ft.Text(width=10)
                            ]),
                            ft.Divider(color=TC)
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
                width=245,
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
            chapter_result = responses.json().get('result')
            if chapter_result == 1:
                chapter_result['type_choice'] = 'Makkada'
            else:
                chapter_result['type_choice'] = 'Madinada'
            chapter_n = ft.Column(
                adaptive=True,
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                    ft.Text(
                        value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                        size=20)
                ]
            )
            right_display.controls.append(chapter_n)
            for result_detail in result_details:
                right_display.controls.append(ft.Column(controls=[ft.Row(
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
                        ft.Text(),
                        ft.Text(value=f"{result_detail.get('text_arabic')}", size=20, expand=True,
                                width=page.window_width, text_align=ft.TextAlign.RIGHT, rtl=True, font_family="Amiri"),
                        ft.Text(width=10)
                    ]),
                    ft.Divider(color=TC)
                ])
                )
        else:
            print("Error")
        page.update()

    # -----Close button logic---------------------------------------------------------------------------------------------
    button3 = ft.TextButton(
        text='< Yopish',
        data='button3',
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=ft.colors.BLACK),
        on_click=lambda e: toggle_widgets(e)
    )

    is_cleaned = True

    column_data = [button3]
    response_data = response
    if response_data.status_code == 200:
        response_list = response_data.json().get('result')
        for response_detail in response_list:
            column_data.append(ft.Container(adaptive=True, content=ft.Text(response_detail.get('id'), color='black'), shape=ft.BoxShape.CIRCLE, width=60,
                         height=60, alignment=ft.alignment.center, border=ft.border.all(2, color=TC)))

    # Function to toggle widgets
    def toggle_widgets(e):
        nonlocal is_cleaned
        if is_cleaned:
            button3.text="Ochish >"
            button3.style=ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=TC)
            side_bar.controls[0].controls=column_data
            side_bar.controls[0].width=100
        else:
            button3.text="< Yopish"
            button3.style=ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=ft.colors.BLACK)
            side_bar.controls[0].width = 350
            side_bar.controls[0].controls=[ft.Row(
                spacing=20,
                adaptive=True,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    button1,
                    button2,
                    button3
                ]
            ),
            list_view
            ]
        is_cleaned = not is_cleaned  # Toggle the state
        page.update()



    # Initialize default colors
    button1_color = TC
    button2_color = ft.colors.BLACK

    # Define ListView
    list_view = ft.ListView(expand=1, spacing=10)
    list_view.controls = list_display.controls

    # Button click handler
    def button_click(e):
        nonlocal button1_color, button2_color

        # Update text colors and ListView content based on which button was clicked
        if e.control.data == "button1":
            button1_color = TC
            button2_color = ft.colors.BLACK
            list_view.controls = list_display.controls
        elif e.control.data == "button2":
            button1_color = ft.colors.BLACK
            button2_color = TC
            list_view.controls = list_display_juz.controls

        # Refresh UI
        button1.style = ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=button1_color)
        button2.style = ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=button2_color)
        page.update()

    # Define TextButtons
    button1 = ft.TextButton(
        "Surah",
        data="button1",
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=button1_color),
        on_click=lambda e: button_click(e),

    )

    button2 = ft.TextButton(
        "Juz",
        data="button2",
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=button2_color),
        on_click=lambda e: button_click(e),

    )


    side_bar = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True,
        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                adaptive=True,
                width=350,
                controls=[
                    ft.Row(
                        spacing=20,
                        adaptive=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            button1,
                            button2,
                            button3
                        ]
                    ),
                    list_view
                ],
            ),
            divider,
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
        spacing=0
    )
    page.add(side_bar)
    page.update()



