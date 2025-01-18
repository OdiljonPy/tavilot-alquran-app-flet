import requests
import flet as ft

TC = '#E9BE5F'
from .html_pdf_handler import render_description
import os


def surah_page_test(page):
    page.clean()
    page.scroll = False
    # from tavilot_al_quran.main import main
    from .html_pdf_handler import render_description
    # from .pages_utils.appbar_search import update_appbar
    loading = ft.ProgressRing(color=TC)
    page.add(ft.Container(
        expand=True,
        adaptive=True,
        content=loading,
        alignment=ft.alignment.center)
    )
    page.clean()
    from tavilot_al_quran.main import main
    list_display = ft.ListView(adaptive=True, spacing=10, padding=20)
    list_display_juz = ft.ListView(adaptive=True, spacing=10, padding=20)
    right_display = ft.Column(spacing=40, expand=True, adaptive=True, scroll=ft.ScrollMode.HIDDEN,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # def juz_button(e):
    #     url = "http://176.221.28.202:8008/api/v1/juz/"
    #     responses = requests.get(url=url)
    #     if responses.status_code == 200:
    #         result_lists = responses.json().get('result')
    #
    #         for i in result_lists:
    #             list_display_juz.controls.append(ft.Container(
    #                 margin=20,
    #                 data=i.get('id'),
    #                 on_click=lambda e: take_juz_id(e.control.data),
    #                 expand=True,
    #                 content=ft.Row(
    #                     controls=[
    #                         ft.Container(adaptive=True, content=ft.Text(i.get('number'), color='black'),
    #                                      shape=ft.BoxShape.CIRCLE,
    #                                      width=60,
    #                                      height=60, alignment=ft.alignment.center, border=ft.border.all(2, color=TC)),
    #                         ft.Column(
    #                             adaptive=True,
    #                             controls=[
    #                                 ft.Text(expand=True, value=f"{i.get('number')}-JUZ", size=20),
    #                                 ft.Text(f"{i.get('title')}", size=15.5, expand=True)
    #                             ])
    #                     ]
    #                 )
    #             ))
    #
    # def take_juz_id(ids):
    #     right_display.controls.clear()
    #     urls = f"http://176.221.28.202:8008/api/v1/juz/{ids}/"
    #     headers = ""
    #     if page.client_storage.get('access_token'):
    #         headers = {
    #             "Content-Type": "application/json",
    #             "Authorization": f"Bearer {page.client_storage.get('access_token')}"
    #         }
    #     else:
    #         headers = {
    #             "Content-Type": "application/json",
    #         }
    #     juz_response = requests.get(url=urls, headers=headers)
    #     if juz_response.status_code == 200:
    #         juz_result_list = juz_response.json().get('result').get('chapters')
    #
    #         right_display.controls.clear()
    #         for juz_i in juz_result_list:
    #             # right_display.controls.append(right_top_bar)
    #             text_arabic.style.color = "white"
    #             text_arabic.style.bgcolor = TC
    #             text_translate.style.color = ft.colors.BLACK
    #             text_translate.style.bgcolor = ft.colors.GREY_200
    #             text_tafsir.style.color = ft.colors.BLACK
    #             text_tafsir.style.bgcolor = ft.colors.GREY_200
    #             if juz_i == 1:
    #                 juz_i['type_choice'] = 'Makkada'
    #             else:
    #                 juz_i['type_choice'] = 'Madinada'
    #             juz_n = ft.Column(
    #                 adaptive=True,
    #                 expand=True,
    #                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #                 controls=[
    #                     ft.Text(value=f"{juz_i.get('name')} Surasi", size=25),
    #                     ft.Text(
    #                         value=f"{juz_i.get('type_choice')} Nozil Bo'lga, {juz_i.get('verse_number')} Oyatdan Iborat",
    #                         size=20)
    #                 ]
    #             )
    #             right_display.controls.append(juz_n)
    #             for juz_i_verse in juz_i.get('verses'):
    #                 if juz_i_verse.get('description'):
    #                     content = render_description(juz_i_verse.get('description'), page)
    #                 else:
    #                     content = ft.Text()
    #                 right_display.controls.append(ft.Column(
    #                     adaptive=True,
    #                     expand=True,
    #                     controls=[ft.Row(
    #                         alignment=ft.MainAxisAlignment.CENTER,
    #                         expand=True,
    #                         adaptive=True,
    #                         controls=[
    #                             ft.Container(
    #                                 image_src=os.path.abspath("assets/Union.png"),
    #                                 alignment=ft.alignment.center,
    #                                 width=50,
    #                                 height=50,
    #                                 adaptive=True,
    #                                 content=ft.Text(value=f"{juz_i_verse.get('number')}")
    #                             ),
    #                             ft.Text(value=f"{juz_i_verse.get('text_arabic')}", size=20,
    #                                     text_align=ft.TextAlign.CENTER,
    #                                     expand=True, width=page.window_width,
    #                                     font_family="Amiri"),
    #                             ft.Text(width=10)
    #                         ]),
    #                         ft.Row(
    #                             controls=[
    #                                 ft.Text(),
    #                                 ft.Text(
    #                                     value=f"{juz_i_verse.get('number')}. {juz_i_verse.get('text')}",
    #                                     size=20,
    #                                     expand=True,
    #                                     width=page.window_width, text_align=ft.TextAlign.LEFT
    #                                 ),
    #                                 ft.Text(width=10),
    #                             ]
    #                         ),
    #                         content,
    #                         ft.Divider(color=TC)
    #                     ])
    #                 )
    #     page.update()

    # ------Back connection----------------------------------------------------------------------------------------------
    url = "http://176.221.28.202:8008/api/v1/chapters/"
    response = requests.get(url=url)
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
                key=i.get('id'),
                data=i.get('id'),
                on_click=lambda e: take_id(e.control.data),
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
    else:
        print("Error")
    # --------------------------------------------------------------------------------------------------------------------
    button_number = 1
    # right_display.controls.clear()
    # urls = f"http://176.221.28.202:8008/api/v1/chapter/{1}"
    # headers = ""
    # if page.client_storage.get('access_token'):
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": f"Bearer {page.client_storage.get('access_token')}"
    #     }
    # else:
    #     headers = {
    #         "Content-Type": "application/json",
    #     }
    # responses = requests.get(url=urls, headers=headers)
    # if responses.status_code == 200:
    #     result_details = responses.json().get('result').get('verses')
    #
    #     def change_response(number=1):
    #         if number == text_arabic.data:
    #             nonlocal button_number
    #             button_number = 1
    #             right_display.controls.clear()
    #             right_display.controls.append(right_top_bar)
    #             text_arabic.style.color = "white"
    #             text_arabic.style.bgcolor = TC
    #             text_translate.style.color = ft.colors.BLACK
    #             text_translate.style.bgcolor = ft.colors.GREY_200
    #             text_tafsir.style.color = ft.colors.BLACK
    #             text_tafsir.style.bgcolor = ft.colors.GREY_200
    #             chapter_result = responses.json().get('result')
    #             if chapter_result == 1:
    #                 chapter_result['type_choice'] = 'Makkada'
    #             else:
    #                 chapter_result['type_choice'] = 'Madinada'
    #             chapter_n = ft.Column(
    #                 adaptive=True,
    #                 expand=True,
    #                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #                 controls=[
    #                     ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
    #                     ft.Text(
    #                         value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
    #                         size=20)
    #                 ]
    #             )
    #             right_display.controls.append(chapter_n)
    #             for result_detail in result_details:
    #                 right_display.controls.append(ft.Column(
    #                     key=result_detail.get('id'),
    #                     controls=[ft.Row(
    #                         expand=True,
    #                         alignment=ft.MainAxisAlignment.CENTER,
    #                         adaptive=True,
    #                         controls=[
    #                             ft.Container(
    #                                 image_src=os.path.abspath("assets/Union.png"),
    #                                 alignment=ft.alignment.center,
    #                                 width=50,
    #                                 height=50,
    #                                 adaptive=True,
    #                                 content=ft.Text(value=f"{result_detail.get('number')}")
    #                             ),
    #                             ft.Text(value=f"{result_detail.get('text_arabic')}", size=20, expand=True,
    #                                     width=page.window_width,
    #                                     text_align=ft.TextAlign.CENTER, font_family="Amiri"),
    #                             ft.Text(width=10)
    #                         ]),
    #                         ft.Divider(color=TC)
    #                     ])
    #                 )
    #         elif number == text_translate.data:
    #             button_number = 2
    #             right_display.controls.clear()
    #             right_display.controls.append(right_top_bar)
    #             text_translate.style.color = 'white'
    #             text_translate.style.bgcolor = TC
    #             text_arabic.style.color = ft.colors.BLACK
    #             text_arabic.style.bgcolor = ft.colors.GREY_200
    #             text_tafsir.style.color = ft.colors.BLACK
    #             text_tafsir.style.bgcolor = ft.colors.GREY_200
    #             chapter_result = responses.json().get('result')
    #             if chapter_result == 1:
    #                 chapter_result['type_choice'] = 'Makkada'
    #             else:
    #                 chapter_result['type_choice'] = 'Madinada'
    #             chapter_n = ft.Column(
    #                 adaptive=True,
    #                 expand=True,
    #                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #                 controls=[
    #                     ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
    #                     ft.Text(
    #                         value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
    #                         size=20)
    #                 ]
    #             )
    #             right_display.controls.append(chapter_n)
    #             for result_detail in result_details:
    #                 right_display.controls.append(ft.Column(
    #                     key=result_detail.get('id'),
    #                     controls=[
    #                         ft.Row(
    #                             expand=True,
    #                             alignment=ft.MainAxisAlignment.CENTER,
    #                             adaptive=True,
    #                             controls=[
    #                                 ft.Container(
    #                                     image_src=os.path.abspath("assets/Union.png"),
    #                                     alignment=ft.alignment.center,
    #                                     width=50,
    #                                     height=50,
    #                                     adaptive=True,
    #                                     content=ft.Text(value=f"{result_detail.get('number')}")
    #                                 ),
    #                                 ft.Text(value=f"{result_detail.get('text_arabic')}", size=20, expand=True,
    #                                         width=page.window_width,
    #                                         text_align=ft.TextAlign.CENTER, font_family="Amiri"),
    #                                 ft.Text(width=10)
    #                             ]),
    #                         ft.Row(
    #                             controls=[
    #                                 ft.Text(),
    #                                 ft.Text(
    #                                     value=f"  {result_detail.get('number')}. {result_detail.get('text')}",
    #                                     size=20,
    #                                     expand=True,
    #                                     width=page.window_width, text_align=ft.TextAlign.LEFT
    #                                 ),
    #                                 ft.Text(width=10),
    #                             ]
    #                         ),
    #                         ft.Divider(color=TC)
    #                     ])
    #                 )
    #         elif number == text_tafsir.data:
    #             button_number = 3
    #             right_display.controls.clear()
    #             right_display.controls.append(right_top_bar)
    #             text_tafsir.style.color = "white"
    #             text_tafsir.style.bgcolor = TC
    #             text_arabic.style.color = ft.colors.BLACK
    #             text_arabic.style.bgcolor = ft.colors.GREY_200
    #             text_translate.style.color = ft.colors.BLACK
    #             text_translate.style.bgcolor = ft.colors.GREY_200
    #             chapter_result = responses.json().get('result')
    #             if chapter_result == 1:
    #                 chapter_result['type_choice'] = 'Makkada'
    #             else:
    #                 chapter_result['type_choice'] = 'Madinada'
    #             chapter_n = ft.Column(
    #                 adaptive=True,
    #                 expand=True,
    #                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #                 controls=[
    #                     ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
    #                     ft.Text(
    #                         value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
    #                         size=20)
    #                 ]
    #             )
    #             right_display.controls.append(chapter_n)
    #             for result_data in result_details:
    #                 if result_data.get('description'):
    #                     content = render_description(result_data.get('description'), page)
    #                     tafsir_data = ft.Column(
    #                         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #                         key=result_data.get('id'),
    #                         controls=[
    #                             ft.Row(
    #                                 alignment=ft.MainAxisAlignment.CENTER,
    #                                 adaptive=True,
    #                                 controls=[
    #                                     ft.Container(
    #                                         image_src=os.path.abspath("assets/Union.png"),
    #                                         alignment=ft.alignment.center,
    #                                         width=50,
    #                                         height=50,
    #                                         adaptive=True,
    #                                         content=ft.Text(value=f"{result_data.get('number')}")
    #                                     ),
    #                                     ft.Text(value=f"{result_data.get('text_arabic')}", size=20,
    #                                             width=page.window_width,
    #                                             expand=True,
    #                                             text_align=ft.TextAlign.CENTER, font_family="Amiri"),
    #                                     ft.Text(width=10)
    #                                 ]),
    #                             ft.Row(
    #                                 alignment=ft.MainAxisAlignment.START,
    #                                 controls=[
    #                                     ft.Text(),
    #                                     ft.Text(
    #                                         value=f"  {result_data.get('number')}. {result_data.get('text')}",
    #                                         size=20,
    #                                         expand=True,
    #                                         width=page.window_width, text_align=ft.TextAlign.LEFT
    #                                     ),
    #                                     ft.Text(width=10)
    #                                 ]),
    #                             content,
    #                             ft.Divider(color=TC)
    #                         ])
    #                     right_display.controls.append(tafsir_data),
    #                     page.update()
    #                 else:
    #                     print("Error")
    #         page.update()  # Update the page to reflect changes
    #
    #     text_arabic = ft.TextButton('Arabcha', data=1, style=ft.ButtonStyle(color='white', bgcolor=TC),
    #                                 on_click=lambda e: change_response(1))
    #     text_translate = ft.TextButton('Tarjima', data=2,
    #                                    style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
    #                                    on_click=lambda e: change_response(2))
    #
    #     text_tafsir = ''
    #     if page.client_storage.get('access_token') and page.client_storage.get('user_rate') == 2:
    #         text_tafsir = ft.TextButton('Tafsir', data=3,
    #                                     style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
    #                                     on_click=lambda e: change_response(3))
    #
    #     elif page.client_storage.get('access_token') and page.client_storage.get('user_rate') == 1:
    #         text_tafsir = ft.TextButton(
    #             content=ft.Row(controls=[
    #                 ft.Text('Tafsir'),
    #                 ft.Image(src=os.path.abspath("assets/lock.png"))
    #             ]
    #             ),
    #             data=3,
    #             style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
    #             on_click=lambda e: None,  # payment_page(page)
    #         )
    #
    #     else:
    #         text_tafsir = ft.TextButton(
    #             content=ft.Row(controls=[
    #                 ft.Text('Tafsir'),
    #                 ft.Image(src=os.path.abspath("assets/lock.png"))
    #             ]
    #             ),
    #             data=3,
    #             style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
    #             on_click=lambda e: main(page)
    #         )
    #
    #     right_top_bar = ft.Container(
    #         expand=True,
    #         alignment=ft.alignment.center,
    #         border_radius=20,
    #         height=30,
    #         width=275,
    #         bgcolor=ft.colors.GREY_200,
    #         adaptive=True,
    #         content=ft.Row(
    #             alignment=ft.MainAxisAlignment.CENTER,
    #             adaptive=True,
    #             controls=[
    #                 text_arabic,
    #                 text_translate,
    #                 text_tafsir
    #             ]
    #         )
    #     )
    #     right_display.controls.append(right_top_bar)
    #     chapter_result = responses.json().get('result')
    #     if chapter_result == 1:
    #         chapter_result['type_choice'] = 'Makkada'
    #     else:
    #         chapter_result['type_choice'] = 'Madinada'
    #     chapter_n = ft.Column(
    #         adaptive=True,
    #         expand=True,
    #         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #         controls=[
    #             ft.Text(value=f"{chapter_result.get('name')} Surasi", size=25),
    #             ft.Text(
    #                 value=f"{chapter_result.get('type_choice')} Nozil Bo'lga, {chapter_result.get('verse_number')} Oyatdan Iborat",
    #                 size=20)
    #         ]
    #     )
    #     right_display.controls.append(chapter_n)
    #     for result_detail in result_details:
    #         right_display.controls.append(ft.Column(
    #             key=result_detail.get('id'),
    #             controls=[ft.Row(
    #                 expand=True,
    #                 alignment=ft.MainAxisAlignment.CENTER,
    #                 adaptive=True,
    #                 controls=[
    #                     ft.Container(
    #                         image_src=os.path.abspath("assets/Union.png"),
    #                         alignment=ft.alignment.center,
    #                         width=50,
    #                         height=50,
    #                         adaptive=True,
    #                         content=ft.Text(value=f"{result_detail.get('number')}")
    #                     ),
    #                     ft.Text(value=f"{result_detail.get('text_arabic')}", size=20, expand=True,
    #                             width=page.window_width,
    #                             text_align=ft.TextAlign.CENTER, font_family="Amiri"),
    #                     ft.Text(width=10)
    #                 ]),
    #                 ft.Divider(color=TC)
    #             ])
    #         )
    #
    # else:
    #     print("Error")
    # page.update()

    # ------Default page-------------------------------------------------------------------------------------------------

    def take_id(ids, number=1):
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
                    nonlocal button_number
                    button_number = 1
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
                    button_number = 2
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
                    button_number = 3
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
                    on_click=lambda e: None,  # payment_page(page)
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
                    on_click=lambda e: main(page)
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
            if button_number == 1:
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
            elif button_number == 2:
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
            elif button_number == 3:
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
            # juz_button(e)
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
                            # button3
                        ]
                    ),
                    list_view
                ],
            ),
            # divider,
            ft.Container(
                bgcolor='white',
                expand=True,
                width=page.window_width,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=page.window_width,
                    adaptive=True,
                    controls=[
                        # ft.Text(height=50),
                        right_display
                    ]
                )
            )
        ],
        spacing=0
    )

    page.add(side_bar)
    page.update()
