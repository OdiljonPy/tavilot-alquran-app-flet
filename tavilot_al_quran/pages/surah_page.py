import flet as ft
import requests
import os
from .html_pdf_handler import extract_base64_and_save_images, extract_and_process_videos, render_content
from .al_quran_oquvchilariga import al_quron_oquvchilariga
from .menuscript import menuscript
from .studies import studies
from .refusal import refusal
from .resources import resources
from .about_us_page import about_us_page
from .payment_page import payment_page


TC = '#E9BE5F'


def surah_page(page, back_button):
    page.clean()
    from .home_page import home
    loading = ft.ProgressRing(color=TC)
    page.add(ft.Container(
        expand=True,
        adaptive=True,
        content=loading,
        alignment=ft.alignment.center)
    )

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
    right_display = ft.Column(spacing=40, expand=True, adaptive=True, scroll=ft.ScrollMode.HIDDEN,
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    # -------Back connection juz----------------------------------------------------------------------------------------

    url = "http://176.221.28.202:8008/api/v1/juz/"
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
                        ft.Container(adaptive=True, content=ft.Text(i.get('number'), color='black'),
                                     shape=ft.BoxShape.CIRCLE,
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
        print("IN JUZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
        right_display.controls.clear()
        urls = f"http://176.221.28.202:8008/api/v1/juz/{ids}/"
        headers = {
            "Content-Type": "application/json",
        }
        juz_response = requests.get(url=urls, headers=headers)
        if juz_response.status_code == 200:
            juz_result_list = juz_response.json().get('result').get('chapters')
            print(juz_result_list, "JUZ IS HEREREREEEEEEEEEEEEE")

            for juz_i in juz_result_list:
                for juz_i_verse in juz_i.get('verses'):
                    print(juz_i_verse)
                    right_display.controls.append(ft.Column(
                        adaptive=True,
                        expand=True,
                        controls=[ft.Row(
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
                                ft.Text(value=f"{juz_i_verse.get('text_arabic')}", size=20, expand=True,
                                        width=page.window_width, text_align=ft.TextAlign.RIGHT, rtl=True,
                                        font_family="Amiri"),
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
        page.update()

    # ------Back connection----------------------------------------------------------------------------------------------
    url = "http://176.221.28.202:8008/api/v1/chapters/"
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
                                ft.Text(f"{i.get('type_choice')}, {i.get('verse_number')} oyat", size=10, expand=True)
                            ]),
                        ft.Text(value=i.get('name_arabic'), size=15, text_align=ft.TextAlign.RIGHT, width=150,
                                font_family='Amiri', expand=True)
                    ])))
    else:
        print('Error')

    # --------------------------------------------------------------------------------------------------------------------
    global parts, result, video_files, tafsir_data

    def take_id(ids):
        right_display.controls.clear()
        urls = f"http://176.221.28.202:8008/api/v1/chapter/{ids}"
        headers = {
            "Content-Type": "application/json",
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
                        right_display.controls.append(ft.Column(
                            key=result_detail.get('id'),
                            controls=[ft.Row(
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
                                        width=page.window_width, text_align=ft.TextAlign.RIGHT, rtl=True,
                                        font_family="Amiri"),
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
                            key=result_detail.get('id'),
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
                                                width=page.window_width, text_align=ft.TextAlign.RIGHT, rtl=True,
                                                font_family="Amiri"),
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
                        if result_detail.get('description'):

                            parts, result = extract_base64_and_save_images(result_detail.get('description'))
                            video_files = extract_and_process_videos(result_detail.get('description'))
                            tafsir_data = ft.Column(
                                key=result_detail.get('id'),
                                controls=[ft.Row(
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
                                            width=page.window_width, text_align=ft.TextAlign.RIGHT, rtl=True,
                                            font_family="Amiri"),
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
                                    value=f"{result}",
                                    size=20,
                                    expand=True,
                                    width=page.window_width,
                                    text_align=ft.TextAlign.RIGHT
                                ),
                                    ft.Text(width=10)
                                ]),
                                ft.Divider(color=TC)
                            ])
                            right_display.controls.append(tafsir_data),
                        else:
                            print("Tafsir not found")
                page.update()  # Update the page to reflect changes

            text_arabic = ft.TextButton('Arabcha', data=1, style=ft.ButtonStyle(color='white', bgcolor=TC),
                                        on_click=change_response)
            text_translate = ft.TextButton('Tarjima', data=2,
                                           style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                                           on_click=change_response)

            text_tafsir = ''
            if page.client_storage.get('access_token') and page.client_storage.get('user_rate') == 2:
                text_tafsir = ft.TextButton('Tafsir', data=3,
                                            style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                                            on_click=change_response)
            else:
                text_tafsir = ft.TextButton(
                    content=ft.Row(controls=[
                        ft.Text('Tafsir'),
                        ft.Image(src=os.path.abspath("assets/lock.png"))
                    ]
                    ),
                    data=3,
                    style=ft.ButtonStyle(color='black', bgcolor=ft.colors.GREY_200),
                    on_click=lambda e: payment_page(page, back_button)
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
            column_data.append(ft.Container(adaptive=True, content=ft.Text(response_detail.get('id'), color='black'),
                                            shape=ft.BoxShape.CIRCLE, width=60,
                                            height=60, alignment=ft.alignment.center,
                                            border=ft.border.all(2, color=TC)))

    # Function to toggle widgets
    def toggle_widgets(e):
        nonlocal is_cleaned
        if is_cleaned:
            button3.text = "Ochish >"
            button3.style = ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=TC)
            side_bar.controls[0].controls = column_data
            side_bar.controls[0].width = 100
        else:
            button3.text = "< Yopish"
            button3.style = ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=ft.colors.BLACK)
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
    back_button = ft.OutlinedButton(
        content=ft.Row(controls=[
            ft.Icon(ft.icons.ARROW_BACK, color='black', size=20),
            ft.Text('Orqaga qaytish', color='black')
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

    def fetch_data(query):
        url = f"http://176.221.28.202:8008/api/v1/search/?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("result", [])
        else:
            print(f"API Error: {response.status_code}")
        return []

    # Dictionary to store created elements by their keys
    # Dictionary to store created elements by their keys
    elements_by_key = {}

    def scroll_to_item(item_id):

        # # Find the element in the dictionary
        # target_element = elements_by_key.get(item_id)
        #
        # if target_element:
        #     # Save the original background color
        #     original_bgcolor = target_element.controls[0].bgcolor
        #
        #     # Set the highlight color
        #     target_element.controls.controls.controls[0].bgcolor = "yellow"
        #     target_element.update()  # Update the UI to reflect the highlight
        #
        #     # # After a delay, reset the background color to the original
        #     # def reset_bgcolor():
        #     #     target_element.bgcolor = original_bgcolor
        #     #     target_element.update()
        #     #
        #     # # Set a timeout to reset the background color after 2 seconds
        #     # page.set_timeout(reset_bgcolor, 2000)

        # Scroll to the target element
        right_display.scroll_to(key=f"{item_id}", duration=700, curve=ft.AnimationCurve.BOUNCE_OUT)
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
        elements_by_key.clear()  # Clear the tracking dictionary

        for search_detail in search_data:
            item_id = search_detail.get('id')
            list_tile = ft.ListTile(
                key=item_id,
                on_click=lambda e, id=item_id: scroll_to_item(id),
                title=ft.Text(
                    f"{search_detail.get('chapter_name')}, {search_detail.get('number')} - oyat"
                )
            )
            # Add the created element to the dictionary
            elements_by_key[item_id] = right_display
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

    routes = {
        "Abu Mansur Motrudiy": al_quron_oquvchilariga,
        "Tavilot al-Quron": surah_page,
        "Qo'lyozma va sharhlar": menuscript,
        "Zamonaviy tadqiqotlar": studies,
        "Resurslar": resources,
        "Mutaassib oqimlarga raddiyalar": refusal
    }

    active_route = None

    def navigate(e, route):
        nonlocal active_route
        if route != active_route:
            active_route = route
            update_appbar()  # Refresh the AppBar with updated colors
            if route in routes:
                routes[route](page, back_button)  # Call the corresponding route function
            else:
                page.clean()
                page.add(ft.Text("404 - Page Not Found", size=20))
                page.update()

    def generate_appbar_actions():
        return [
            ft.TextButton(
                adaptive=True,
                expand=True,
                text=route_label,
                style=ft.ButtonStyle(
                    text_style=ft.TextStyle(size=15),
                    color='#007577' if route == active_route else ft.colors.BLACK,
                ),
                on_click=lambda e, r=route: navigate(e, r)
            )
            for route, route_label in [
                ("Abu Mansur Motrudiy", "Abu Mansur Motrudiy"),
                ("Tavilot al-Quron", "Tavilot al-Quron"),
                ("Qo'lyozma va sharhlar", "Qo'lyozma va sharhlar"),
                ("Zamonaviy tadqiqotlar", "Zamonaviy tadqiqotlar"),
                ("Resurslar", "Resurslar"),
                ("Mutaassib oqimlarga raddiyalar", "Mutaassib oqimlarga raddiyalar")

            ]
        ]

    def update_appbar():
        page.appbar = ft.AppBar(
            title=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
                adaptive=True,
                controls=[
                    *generate_appbar_actions(),
                ]
            ),
            center_title=True,
            adaptive=True,
            leading=ft.Image(
                expand=True,
                color='#007577',
                src=os.path.abspath("assets/tA'VILOT_Монтажная_область1.svg")
            ),
            actions=[
                ft.Row(
                    adaptive=True,
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,  # Reduced spacing to allow more room for items
                    controls=[
                        search
                    ],
                ),
            ],
            bgcolor='white',
            toolbar_height=80,
        )
        page.update()

    update_appbar()
    page.add(side_bar)
    # Render the extracted parts (text, images, videos)
    render_content(tafsir_data, parts, video_files)
    page.update()
