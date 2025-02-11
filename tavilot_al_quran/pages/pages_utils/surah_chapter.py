import requests
import flet as ft
TC = '#E9BE5F'
import os
from ..html_pdf_handler import render_description
import time

def surah_chapter(page, list_display, right_display):
    url = "http://alquran.zerodev.uz/api/v2/chapters/"
    headers = {
        "Content-Type": "application/json",
        "Accept-Language": page.client_storage.get('language')
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        page.scroll = False
        result_lists = response.json().get('result')

        for i in result_lists:
            if i.get('type_choice') == 1:
                i['type_choice'] = 'Makkiy'
            else:
                i['type_choice'] = 'Madaniy'

            list_display.controls.append(ft.Container(
                margin=20,
                key=i.get('number'),
                data=i.get('id'),
                on_click=lambda e: take_id(e.control.data, right_display, page),
                content=ft.Row(
                    adaptive=True,
                    controls=[
                        ft.Container(adaptive=True, content=ft.Text(i.get('number'), color='black'),
                                     shape=ft.BoxShape.CIRCLE, width=60,
                                     height=60, alignment=ft.alignment.center, border=ft.border.all(2, color=TC)),
                        ft.Column(
                            controls=[
                                ft.Text(i.get('name'), size=20, expand=True),
                                ft.Text(f"{i.get('type_choice')}, {i.get('verse_number')} oyat", size=15.5, expand=True)
                            ]),
                        ft.Text(value=i.get('name_arabic'), size=18, text_align=ft.TextAlign.RIGHT, width=150,
                                font_family='Amiri', expand=True)
                    ])))


def take_id(ids, right_display, page, number=1):
    from ..main_page import main_page

    def scroll_to_it(item_id):
        # Find the target element
        target_element = next((control for control in right_display.controls if control.key == int(item_id)), None)
        # Scroll to the target element
        if target_element:
            # Apply highlight style
            original_bgcolor = target_element.controls[0].controls[0].bgcolor
            target_element.controls[0].controls[0].bgcolor = "yellow"
            target_element.update()

        # Function to remove highlight after a delay
        def remove_highlight():
            # Sleep for 3 seconds
            time.sleep(3)
            # Restore original background color
            target_element.controls[0].controls[0].bgcolor = original_bgcolor
            target_element.update()

        # Scroll to the target element
        right_display.scroll_to(key=f"{item_id}", duration=600, curve=ft.AnimationCurve.BOUNCE_OUT)
        remove_highlight()
        page.update()
    # -------VERSE NUMBER CHOOSER----------------------------------------------------------------------------------------
    def on_clicked(e):
        scroll_to_it(num_field.value)

    def increase(e):
        num_field.value = str(int(num_field.value) + 1)
        page.update()

    def decrease(e):
        if int(num_field.value) > 0:  # Prevent negative numbers
            num_field.value = str(int(num_field.value) - 1)
            page.update()

    num_field = ft.TextField(
        expand=True,
        value="0",
        width=100,
        max_length=4,
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=8,
        content_padding=30  # Space for buttons
    )

    number_input = ft.Stack(
        adaptive=True,
        height=35,
        controls=[
            num_field,
            ft.Column([
                ft.IconButton(ft.icons.EXPAND_LESS, on_click=increase, width=30, height=5, expand=True, adaptive=True,
                              icon_size=18, padding=0),
                ft.IconButton(ft.icons.EXPAND_MORE, on_click=decrease, width=30, height=5, expand=True, adaptive=True,
                              icon_size=18, padding=0),
            ], width=100,
                expand=True,
                spacing=0,
                run_spacing=0)
        ])

    surah_verse = ft.Container(
        margin=15,
        alignment=ft.alignment.center_right,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.END,
        controls=[
            number_input,
            ft.OutlinedButton(
                on_click=lambda e: on_clicked(e),
                width=100,
                height=38,
                text="Oyatga o'tish",
                style=ft.ButtonStyle(
                    color='white',
                    bgcolor=TC,
                    shape=ft.RoundedRectangleBorder(radius=10),
                    side=ft.BorderSide(color=TC, width=1),
                )
            )

        ]
    )
    )

    right_display.controls.clear()

    urls = f"http://alquran.zerodev.uz/api/v2/chapter/{ids}"
    if page.client_storage.get('access_token'):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {page.client_storage.get('access_token')}",
            "Accept-Language": page.client_storage.get('language')
        }
    else:
        headers = {
            "Content-Type": "application/json",
            "Accept-Language": page.client_storage.get('language')
        }

    loading = ft.ProgressRing(color=TC)
    right_display.controls.append(ft.Container(
        expand=True,
        adaptive=True,
        content=loading,
        alignment=ft.alignment.center)
    )
    page.update()

    responses = requests.get(url=urls, headers=headers)
    if responses.status_code == 200:
        result_details = responses.json().get('result').get('verses')

        def change_response(number=number):
            if number == text_arabic.data:
                page.session.set("button_number", 1)
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
                        ft.Text(value=f"{chapter_result.get('name')}", size=25),
                        ft.Text(
                            value=f"{chapter_result.get('type_choice')} nozil bo'lgan, {chapter_result.get('verse_number')} oyatdan iborat",
                            size=20)
                    ]
                )
                right_display.controls.append(chapter_n)
                for result_detail in result_details:
                    right_display.controls.append(ft.Column(
                        key=result_detail.get('number'),
                        controls=[ft.Row(
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
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
                                        width=page.window.width,
                                        text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                                ft.Text(width=10)
                            ]),
                            ft.Divider(color=TC)
                        ])
                    )
            elif number == text_translate.data:
                page.session.set("button_number", 2)
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
                        ft.Text(value=f"{chapter_result.get('name')}", size=25),
                        ft.Text(
                            value=f"{chapter_result.get('type_choice')} nozil bo'lgan, {chapter_result.get('verse_number')} oyatdan iborat",
                            size=20)
                    ]
                )
                right_display.controls.append(chapter_n)
                for result_detail in result_details:
                    right_display.controls.append(ft.Column(
                        key=result_detail.get('number'),
                        controls=[
                            ft.Row(
                                expand=True,
                                alignment=ft.MainAxisAlignment.CENTER,
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
                                            width=page.window.width,
                                            text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                                    ft.Text(width=10)
                                ]),
                            ft.Row(
                                controls=[
                                    ft.Text(),
                                    ft.Text(
                                        value=f" {result_detail.get('text')}",
                                        size=20,
                                        expand=True,
                                        width=page.window.width, text_align=ft.TextAlign.LEFT
                                    ),
                                    ft.Text(width=10),
                                ]
                            ),
                            ft.Divider(color=TC)
                        ])
                    )
            elif number == text_tafsir.data:
                page.session.set("button_number", 3)
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
                        ft.Text(value=f"{chapter_result.get('name')}", size=25),
                        ft.Text(
                            value=f"{chapter_result.get('type_choice')} nozil bo'lgan, {chapter_result.get('verse_number')} oyatdan iborat",
                            size=20)
                    ]
                )
                right_display.controls.append(chapter_n)
                for result_data in result_details:
                    if result_data.get('description'):
                        content = render_description(result_data.get('description'), page)
                        tafsir_data = ft.Column(
                            key=result_data.get('number'),
                            controls=[
                                ft.Row(
                                    expand=True,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    adaptive=True,
                                    controls=[
                                        ft.Container(
                                            image_src=os.path.abspath("assets/Union.png"),
                                            alignment=ft.alignment.center,
                                            width=50,
                                            height=50,
                                            adaptive=True,
                                            content=ft.Text(value=f"{result_data.get('number')}")
                                        ),
                                        ft.Text(value=f"{result_data.get('text_arabic')}", size=20, expand=True,
                                                width=page.window.width,
                                                text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                                        ft.Text(width=10)
                                    ]),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.START,
                                    controls=[
                                        ft.Text(),
                                        ft.Text(
                                            value=f" {result_data.get('text')}",
                                            size=20,
                                            expand=True,
                                            width=page.window.width, text_align=ft.TextAlign.LEFT
                                        ),
                                        ft.Text(width=10)
                                    ]),
                                content,
                                ft.Divider(color=TC)
                            ])
                        right_display.controls.append(tafsir_data),
                    else:
                        print("ERROR")
            page.update()  # Update the page to reflect changes

        text_arabic = ft.TextButton('Arabcha', data=1, style=ft.ButtonStyle(color='white', bgcolor=TC),
                                    on_click=lambda e: change_response(1))
        text_translate = ft.TextButton('Tarjima', data=2,
                                       style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                                       on_click=lambda e: change_response(2))

        text_tafsir = ''
        if page.client_storage.get('access_token') and page.client_storage.get('user_rate') == 2:
            text_tafsir = ft.TextButton('Tafsir', data=3,
                                        style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                                        on_click=lambda e: change_response(3))

        elif page.client_storage.get('access_token') and page.client_storage.get('user_rate') == 1:
            text_tafsir = ft.TextButton(
                content=ft.Row(controls=[
                    ft.Text('Tafsir'),
                    ft.Image(src=os.path.abspath("assets/lock.png"))
                ]
                ),
                data=3,
                style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                on_click=lambda e: None, #payment_page(page)
            )

        else:
            text_tafsir = ft.TextButton(
                content=ft.Row(controls=[
                    ft.Text('Tafsir'),
                    ft.Image(src=os.path.abspath("assets/lock.png"))
                ]
                ),
                data=3,
                style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                on_click=lambda e: main_page(page)
            )

        right_top_bar = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
            surah_verse,
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                border_radius=20,
                height=30,
                width=220,
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
        ])
        if page.session.get("button_number") == 1:
            right_display.controls.clear()
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
                    ft.Text(value=f"{chapter_result.get('name')}", size=25),
                    ft.Text(
                        value=f"{chapter_result.get('type_choice')} nozil bo'lgan, {chapter_result.get('verse_number')} oyatdan iborat",
                        size=20)
                ]
            )
            right_display.controls.append(chapter_n)
            for result_detail in result_details:
                right_display.controls.append(ft.Column(
                    key=result_detail.get('number'),
                    controls=[ft.Row(
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER,
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
                                    width=page.window.width,
                                    text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                            ft.Text(width=10)
                        ]),
                        ft.Divider(color=TC)
                    ])
                )
        elif page.session.get("button_number") == 2:
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
                    ft.Text(value=f"{chapter_result.get('name')}", size=25),
                    ft.Text(
                        value=f"{chapter_result.get('type_choice')} nozil bo'lgan, {chapter_result.get('verse_number')} oyatdan iborat",
                        size=20)
                ]
            )
            right_display.controls.append(chapter_n)
            for result_detail in result_details:
                right_display.controls.append(ft.Column(
                    key=result_detail.get('number'),
                    controls=[
                        ft.Row(
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
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
                                        width=page.window.width,
                                        text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                                ft.Text(width=10)
                            ]),
                        ft.Row(
                            controls=[
                                ft.Text(),
                                ft.Text(
                                    value=f" {result_detail.get('text')}",
                                    size=20,
                                    expand=True,
                                    width=page.window.width, text_align=ft.TextAlign.LEFT
                                ),
                                ft.Text(width=10),
                            ]
                        ),
                        ft.Divider(color=TC)
                    ])
                )
        elif page.session.get("button_number") == 3:
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
                    ft.Text(value=f"{chapter_result.get('name')}", size=25),
                    ft.Text(
                        value=f"{chapter_result.get('type_choice')} nozil bo'lgan, {chapter_result.get('verse_number')} oyatdan iborat",
                        size=20)
                ]
            )
            right_display.controls.append(chapter_n)
            for result_data in result_details:
                if result_data.get('description'):
                    content = render_description(result_data.get('description'), page)
                    tafsir_data = ft.Column(
                        key=result_data.get('number'),
                        controls=[
                            ft.Row(
                                expand=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                adaptive=True,
                                controls=[
                                    ft.Container(
                                        image_src=os.path.abspath("assets/Union.png"),
                                        alignment=ft.alignment.center,
                                        width=50,
                                        height=50,
                                        adaptive=True,
                                        content=ft.Text(value=f"{result_data.get('number')}")
                                    ),
                                    ft.Text(value=f"{result_data.get('text_arabic')}", size=20, expand=True,
                                            width=page.window.width,
                                            text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                                    ft.Text(width=10)
                                ]),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Text(),
                                    ft.Text(
                                        value=f" {result_data.get('text')}",
                                        size=20,
                                        expand=True,
                                        width=page.window.width, text_align=ft.TextAlign.LEFT
                                    ),
                                    ft.Text(width=10)
                                ]),
                            content,
                            ft.Divider(color=TC)
                        ])
                    right_display.controls.append(tafsir_data),
    else:
        right_display.controls.append(ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text("Server bilan bog'lanishda muammo kuzatildi", size=50, color=TC)
        ))
    page.update()