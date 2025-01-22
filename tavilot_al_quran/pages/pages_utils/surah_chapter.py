import requests
import flet as ft
TC = '#E9BE5F'
import os
from ..html_pdf_handler import render_description

def surah_chapter(page, list_display, right_display):
    url = "http://176.221.28.202:8008/api/v1/chapters/"
    response = requests.get(url=url)
    if response.status_code == 200:
        page.clean()
        page.scroll = False
        result_lists = response.json().get('result')

        for i in result_lists:
            if i.get('type_choice') == 1:
                i['type_choice'] = 'Makkiy'
            else:
                i['type_choice'] = 'Madaniy'

            list_display.controls.append(ft.Container(
                margin=20,
                key=i.get('id'),
                data=i.get('id'),
                on_click=lambda e: take_id(e.control.data, right_display, page),
                content=ft.Row(
                    adaptive=True,
                    controls=[
                        ft.Container(adaptive=True, content=ft.Text(i.get('id'), color='black'),
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
    right_display.controls.clear()
    urls = f"http://176.221.28.202:8008/api/v1/chapter/{ids}"
    headers = ""
    if page.client_storage.get('access_token'):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {page.client_storage.get('access_token')}"
        }
    else:
        headers = {
            "Content-Type": "application/json",
        }
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
                        ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                        ft.Text(
                            value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                            size=20)
                    ]
                )
                right_display.controls.append(chapter_n)
                for result_detail in result_details:
                    right_display.controls.append(ft.Column(
                        key=result_detail.get('id'),
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
                                        width=page.window_width,
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
                        ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                        ft.Text(
                            value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                            size=20)
                    ]
                )
                right_display.controls.append(chapter_n)
                for result_detail in result_details:
                    right_display.controls.append(ft.Column(
                        key=result_detail.get('id'),
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
                                            width=page.window_width,
                                            text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                                    ft.Text(width=10)
                                ]),
                            ft.Row(
                                controls=[
                                    ft.Text(),
                                    ft.Text(
                                        value=f"  {result_detail.get('number')}. {result_detail.get('text')}",
                                        size=20,
                                        expand=True,
                                        width=page.window_width, text_align=ft.TextAlign.LEFT
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
                        ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                        ft.Text(
                            value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                            size=20)
                    ]
                )
                right_display.controls.append(chapter_n)
                for result_data in result_details:
                    if result_data.get('description'):
                        content = render_description(result_data.get('description'), page)
                        tafsir_data = ft.Column(
                            key=result_data.get('id'),
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
                                                width=page.window_width,
                                                text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                                        ft.Text(width=10)
                                    ]),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.START,
                                    controls=[
                                        ft.Text(),
                                        ft.Text(
                                            value=f"  {result_data.get('number')}. {result_data.get('text')}",
                                            size=20,
                                            expand=True,
                                            width=page.window_width, text_align=ft.TextAlign.LEFT
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

        right_top_bar = ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            border_radius=20,
            height=30,
            width=275,
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
                    ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                    ft.Text(
                        value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                        size=20)
                ]
            )
            right_display.controls.append(chapter_n)
            for result_detail in result_details:
                right_display.controls.append(ft.Column(
                    key=result_detail.get('id'),
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
                                    width=page.window_width,
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
                    ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                    ft.Text(
                        value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                        size=20)
                ]
            )
            right_display.controls.append(chapter_n)
            for result_detail in result_details:
                right_display.controls.append(ft.Column(
                    key=result_detail.get('id'),
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
                                        width=page.window_width,
                                        text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                                ft.Text(width=10)
                            ]),
                        ft.Row(
                            controls=[
                                ft.Text(),
                                ft.Text(
                                    value=f"  {result_detail.get('number')}. {result_detail.get('text')}",
                                    size=20,
                                    expand=True,
                                    width=page.window_width, text_align=ft.TextAlign.LEFT
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
                    ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
                    ft.Text(
                        value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
                        size=20)
                ]
            )
            right_display.controls.append(chapter_n)
            for result_data in result_details:
                if result_data.get('description'):
                    content = render_description(result_data.get('description'), page)
                    tafsir_data = ft.Column(
                        key=result_data.get('id'),
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
                                            width=page.window_width,
                                            text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                                    ft.Text(width=10)
                                ]),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Text(),
                                    ft.Text(
                                        value=f"  {result_data.get('number')}. {result_data.get('text')}",
                                        size=20,
                                        expand=True,
                                        width=page.window_width, text_align=ft.TextAlign.LEFT
                                    ),
                                    ft.Text(width=10)
                                ]),
                            content,
                            ft.Divider(color=TC)
                        ])
                    right_display.controls.append(tafsir_data),
    else:
        print("ERROR")
    page.update()