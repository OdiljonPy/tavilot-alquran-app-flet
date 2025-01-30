import flet as ft
import requests
from ..html_pdf_handler import render_description

TC = '#E9BE5F'
import os


def juz_button(list_display_juz, right_display, page, text_arabic, text_translate, text_tafsir):
    url = "http://alquran.zerodev.uz/api/v2/juz/"
    headers = {
        "Content-Type": "application/json",
        "Accept-Language": page.client_storage.get('language')
    }
    responses = requests.get(url=url, headers=headers)
    if responses.status_code == 200:
        result_lists = responses.json().get('result')

        for i in result_lists:
            list_display_juz.controls.append(ft.Container(
                margin=20,
                data=i.get('id'),
                on_click=lambda e: take_juz_id(e.control.data, right_display, page, text_arabic, text_translate,
                                               text_tafsir),
                expand=True,
                content=ft.Row(
                    controls=[
                        ft.Container(adaptive=True, content=ft.Text(i.get('number'), color='black'),
                                     shape=ft.BoxShape.CIRCLE,
                                     width=60,
                                     height=60, alignment=ft.alignment.center, border=ft.border.all(2, color=TC)),
                        ft.Column(
                            adaptive=True,
                            controls=[
                                ft.Text(expand=True, value=f"{i.get('number')}-JUZ", size=20),
                                ft.Text(f"{i.get('title')}", size=15.5, expand=True)
                            ])
                    ]
                )
            )
            )


def take_juz_id(ids, right_display, page, text_arabic, text_translate, text_tafsir):
    right_display.controls.clear()

    urls = f"http://alquran.zerodev.uz/api/v2/juz/{ids}/"

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
    juz_response = requests.get(url=urls, headers=headers)
    if juz_response.status_code == 200:
        juz_result_list = juz_response.json().get('result').get('chapters')
        right_display.controls.clear()
        if not juz_result_list:
            right_display.controls.append(
                ft.Text('Malumot topilmadi', size=40, color=TC, expand=True, text_align=ft.TextAlign.CENTER))
        else:
            for juz_i in juz_result_list:
                text_arabic.style.color = "white"
                text_arabic.style.bgcolor = TC
                text_translate.style.color = ft.colors.BLACK
                text_translate.style.bgcolor = ft.colors.GREY_200
                text_tafsir.style.color = ft.colors.BLACK
                text_tafsir.style.bgcolor = ft.colors.GREY_200
                if juz_i == 1:
                    juz_i['type_choice'] = 'Makkada'
                else:
                    juz_i['type_choice'] = 'Madinada'
                juz_n = ft.Column(
                    adaptive=True,
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value=f"{juz_i.get('name')} surasi", size=25),
                        ft.Text(
                            value=f"{juz_i.get('type_choice')} nozil bo'lgan, {juz_i.get('verse_number')} oyatdan iborat",
                            size=20)
                    ]
                )
                right_display.controls.append(juz_n)
                for juz_i_verse in juz_i.get('verses'):
                    if juz_i_verse.get('description'):
                        content = render_description(juz_i_verse.get('description'), page)
                    else:
                        content = ft.Text()
                    right_display.controls.append(ft.Column(
                        adaptive=True,
                        expand=True,
                        controls=[ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True,
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
                                ft.Text(value=f"{juz_i_verse.get('text_arabic')}", size=20,
                                        text_align=ft.TextAlign.CENTER,
                                        expand=True, width=page.window.width,
                                        font_family="Amiri"),
                                ft.Text(width=10)
                            ]),
                            ft.Row(
                                controls=[
                                    ft.Text(),
                                    ft.Text(
                                        value=f" {juz_i_verse.get('text')}",
                                        size=20,
                                        expand=True,
                                        width=page.window.width, text_align=ft.TextAlign.LEFT
                                    ),
                                    ft.Text(width=10),
                                ]
                            ),
                            content,
                            ft.Divider(color=TC)
                        ])
                    )
    else:
        right_display.controls.append(ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text("Server bilan bog'lanishda muammo kuzatildi", size=50, color=TC)
        ))
    page.update()
