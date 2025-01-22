import time
import flet as ft
import requests
import os
from .pages_utils.surah_juz import juz_button, take_juz_id
TC = '#E9BE5F'
from .pages_utils.surah_chapter import surah_chapter, take_id
from .html_pdf_handler import render_description
from .payment_page import payment_page


def surah_page(page):
    page.clean()
    page.scroll = False
    from .main_page import main_page
    from .pages_utils.appbar_search import update_appbar
    loading = ft.ProgressRing(color=TC)
    page.add(ft.Container(
        expand=True,
        adaptive=True,
        content=loading,
        alignment=ft.alignment.center)
    )

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
    right_display = ft.Column(spacing=40, expand=True, adaptive=True, scroll=ft.ScrollMode.HIDDEN,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    page.session.set("button_number", 1)
    #------Buttons------------------------------------------------------------------------------------------------------

    text_arabic = ft.TextButton('Arabcha', data=1, style=ft.ButtonStyle(color='white', bgcolor=TC),
                                on_click=lambda e: change_response(1))
    text_translate = ft.TextButton('Tarjima', data=2,
                                   style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                                   on_click=lambda e: change_response(2))

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
            on_click=lambda e: payment_page(page)
        )

    else:
        # pass
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

    #-------------------------------------------------------------------------------------------------------------------
    surah_chapter(page, list_display, right_display)


    right_display.controls.clear()
    urls = f"http://176.221.28.202:8008/api/v1/chapter/{1}"
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

        def change_response(number=1):
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
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            key=result_data.get('id'),
                            controls=[
                                ft.Row(
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
                                        ft.Text(value=f"{result_data.get('text_arabic')}", size=20,
                                                width=page.window_width,
                                                expand=True,
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
            page.update()  # Update the page to reflect changes


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
        right_display.controls.append(right_top_bar)
        chapter_result_d = responses.json().get('result')
        if chapter_result_d == 1:
            chapter_result_d['type_choice'] = 'Makkada'
        else:
            chapter_result_d['type_choice'] = 'Madinada'
        chapter_n_d = ft.Column(
            adaptive=True,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value=f"{chapter_result_d.get('name')} Surasi", size=25),
                ft.Text(
                    value=f"{chapter_result_d.get('type_choice')} Nozil Bo'lga, {chapter_result_d.get('verse_number')} Oyatdan Iborat",
                    size=20)
            ]
        )
        right_display.controls.append(chapter_n_d)
        for result_detail_d in result_details:
            right_display.controls.append(ft.Column(
                key=result_detail_d.get('id'),
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
                            content=ft.Text(value=f"{result_detail_d.get('number')}")
                        ),
                        ft.Text(value=f"{result_detail_d.get('text_arabic')}", size=20, expand=True,
                                width=page.window_width,
                                text_align=ft.TextAlign.CENTER, font_family="Amiri"),
                        ft.Text(width=10)
                    ]),
                    ft.Divider(color=TC)
                ])
            )

    page.update()


    # -----Close button logic---------------------------------------------------------------------------------------------
    list_button_number = 1

    button3 = ft.TextButton(
        text='< Yopish',
        data='button3',
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=TC),
        on_click=lambda e: toggle_widgets(e)
    )

    is_cleaned = True
    column_data = ft.Column(controls=[button3], adaptive=True, spacing=10, scroll=ft.ScrollMode.ALWAYS, expand=True, height=page.adaptive)
    def close_open_button():
        if list_button_number == 1:
            url = "http://176.221.28.202:8008/api/v1/chapters/"
            response_data = requests.get(url=url)
            if response_data.status_code == 200:
                response_list = response_data.json().get('result')
                column_data.controls.clear()
                column_data.controls.append(button3)
                for response_detail in response_list:
                    column_data.controls.append(
                        ft.Container(
                            data=response_detail.get('id'),
                            on_click=lambda e: take_id(e.control.data, right_display, page),
                            adaptive=True, content=ft.Text(response_detail.get('id'), color='black'),
                                     shape=ft.BoxShape.CIRCLE, width=60,
                                     height=60, alignment=ft.alignment.center,
                                     border=ft.border.all(2, color=TC)))

        elif list_button_number == 2:
            url = "http://176.221.28.202:8008/api/v1/juz/"
            response_data = requests.get(url=url)
            if response_data.status_code == 200:
                result_lists = response_data.json().get('result')
                column_data.controls.clear()
                column_data.controls.append(button3)
                for response_detail in result_lists:
                    column_data.controls.append(ft.Container(
                        data=response_detail.get('id'),
                        on_click=lambda e: take_juz_id(e.control.data, right_display, page, text_arabic, text_translate, text_tafsir),
                        adaptive=True, content=ft.Text(response_detail.get('number'), color='black'),
                                 shape=ft.BoxShape.CIRCLE,
                                 width=60,
                                 height=60, alignment=ft.alignment.center, border=ft.border.all(2, color=TC)))
        page.update()


    # Function to toggle widgets
    def toggle_widgets(e):
        nonlocal is_cleaned
        if is_cleaned:
            close_open_button()
            button3.text = "Ochish >"
            button3.style = ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=TC)
            side_bar.controls[0].controls = column_data.controls
            side_bar.controls[0].width = 100
        else:
            button3.text = "< Yopish"
            button3.style = ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=TC)
            side_bar.controls[0].width = 350
            side_bar.controls[0].controls = [ft.Row(
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
        nonlocal button1_color, button2_color, list_button_number

        # Update text colors and ListView content based on which button was clicked
        if e.control.data == "button1":
            list_button_number = 1
            button1_color = TC
            button2_color = ft.colors.BLACK
            list_view.controls = list_display.controls
        elif e.control.data == "button2":
            list_button_number = 2
            button1_color = ft.colors.BLACK
            button2_color = TC
            juz_button(list_display_juz, right_display, page, text_arabic, text_translate, text_tafsir)
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
                        right_display
                    ]
                )
            )
        ],
        spacing=0
    )


    def fetch_data(query):
        url = f"http://176.221.28.202:8008/api/v1/search/?q={query}&search_type={page.session.get("button_number")}"
        if page.client_storage.get('access_token'):
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {page.client_storage.get('access_token')}"
            }
        else:
            headers = {
                "Content-Type": "application/json",
            }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json().get("result", [])
        else:
            print("ERROR")
        return []


    def scroll_to_item(item_id, chapter_id):

        # Perform the necessary actions (e.g., highlight or take some action with chapter_id)
        take_id(chapter_id, number=page.session.get("button_number"), right_display=right_display, page=page)

        # Find the target element
        target_element = next((control for control in right_display.controls if control.key == item_id), None)

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
        right_display.scroll_to(key=f"{item_id}", duration=700, curve=ft.AnimationCurve.BOUNCE_OUT)
        remove_highlight()
        page.update()

    def handle_submit(e):
        search.close_view(e.data)
        query = e.data.strip()

        if not query:
            search.controls.clear()
            search.update()
            return

        search_data = fetch_data(query)

        search.controls.clear()

        def create_on_click_handler(item_id, chapter_id):
            return lambda e: scroll_to_item(item_id, chapter_id)

        for search_detail in search_data:
            item_id = search_detail.get('id')
            chapter_id = search_detail.get('chapter_id')

            # Pass both item_id and chapter_id as default arguments to the lambda function
            list_tile = ft.ListTile(
                key=item_id,
                on_click=create_on_click_handler(item_id, chapter_id),
                title=ft.Text(
                    f"{search_detail.get('chapter_name')}, {search_detail.get('number')} - oyat"
                )
            )
            search.controls.append(list_tile)

        search.open_view()
        search.update()  # Refresh the UI with the new data

    search = ft.SearchBar(
        width=180,
        height=50,
        expand=True,
        bar_bgcolor="white",
        bar_border_side=ft.BorderSide(color=ft.colors.BLUE, width=1),
        divider_color=ft.colors.AMBER,
        bar_leading=ft.Icon(ft.icons.SEARCH),
        bar_hint_text="Nima o'qimoqchisiz?...",
        view_hint_text="Searching...",
        on_submit=handle_submit,  # Trigger search when user submits the query
        controls=[],  # Start with an empty control list
    )
    update_appbar(page, search)
    page.clean()
    page.add(side_bar)
    page.update()
