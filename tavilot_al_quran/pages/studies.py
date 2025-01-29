import flet as ft
import os
import requests
from .studies_detail import take_content_id

def studies(page):
    from .home_page import home
    from .about_us_page import about_us_page
    from .resources import resources
    from .refusal import refusal
    from .surah_page import surah_page
    from .menuscript import menuscript
    from .al_quran_oquvchilariga import al_quron_oquvchilariga
    from .pages_utils.appbar_search import update_appbar

    page.scroll = False
    page.clean()
    TC = '#E9BE5F'
    loading = ft.ProgressRing(color=TC)
    page.add(ft.Container(
        expand=True,
        adaptive=True,
        content=loading,
        alignment=ft.alignment.center)
    )

    # -------Translation of the page-------------------------------------------------------------------------------------
    import json
    # Function to load JSON translation files
    def load_translation(lang):
        with open(f"locales/translations.json", "r", encoding="utf-8") as f:
            return json.load(f).get(lang)

    def change_language(e):
        page.client_storage.set('language', e)
        new_translation = load_translation(e)
        back_button_text.value = new_translation.get('back_button_text')
        abu_mansur_motrudiy.value = new_translation.get('abu_mansur_motrudiy')
        appbar_tavilot.value = new_translation.get('appbar_tavilot')
        appbar_menuscript.value = new_translation.get('appbar_menuscript')
        appbar_studies.value = new_translation.get('appbar_studies')
        appbar_resources.value = new_translation.get('appbar_resources')
        appbar_refusal.value = new_translation.get('appbar_refusal')
        studies(page)

    if page.client_storage.get('language'):
        current_translation = load_translation(page.client_storage.get('language'))
    else:
        current_translation = load_translation("uz")

    back_button_text = ft.Text(current_translation.get('back_button_text'), color='black')
    abu_mansur_motrudiy = ft.Text(current_translation.get('abu_mansur_motrudiy'))
    appbar_tavilot = ft.Text(current_translation.get('appbar_tavilot'))
    appbar_menuscript = ft.Text(current_translation.get('appbar_menuscript'))
    appbar_studies = ft.Text(current_translation.get('appbar_studies'))
    appbar_resources = ft.Text(current_translation.get('appbar_resources'))
    appbar_refusal = ft.Text(current_translation.get('appbar_refusal'))
    back_button = ft.OutlinedButton(
        content=ft.Row(controls=[
            ft.Icon(ft.icons.ARROW_BACK, color='black', size=20),
            back_button_text
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

    page.update()

    url = "http://alquran.zerodev.uz/api/v2/studies/"
    headers = {
        "Content-Type": "application/json",
        "Accept-Language": page.client_storage.get('language')
    }
    response = requests.get(url=url, headers=headers)
    data_list = ft.Row(wrap=True, expand=True, scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                       adaptive=True)

    if response.status_code == 200:
        page.clean()
        page.scroll = True
        datas = response.json().get('result')
        for date in datas:
            motrudiy_data = ft.OutlinedButton(
                adaptive=True,
                data=date.get('id'),
                on_click=lambda e: take_content_id(page, e.control.data),
                content=ft.Column(
                    controls=[
                        ft.Column(
                            scale=ft.Scale(scale_x=0.9, scale_y=0.9),
                            controls=[
                            ft.Text(),
                            ft.Image(src=os.path.abspath("assets/book_1.svg"), color="white"),
                            ft.Text(f"\n{date.get('title')}", size=20, color='white'),
                        ])
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                ),
                height=250,
                width=410,
                style=ft.ButtonStyle(
                    bgcolor=TC,
                    shape=ft.RoundedRectangleBorder(radius=14),
                ),

            )
            data_list.controls.append(motrudiy_data)
        page.update()

    divider = ft.Divider(height=30, color='white')
    page.add(divider, ft.Container(
        margin=15,
        adaptive=True,
        expand=True,
        alignment=ft.alignment.center_left,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.START,
            adaptive=True,
            controls=[
                back_button,
                ft.Text(height=70),
                data_list
            ]
        )
    )
             )

    about_us_icon = ft.IconButton(
        icon=ft.Icons.INFO,
        icon_color=TC,
        on_click=lambda e: about_us_page(page, back_button)
    )

    def handle_close(e):
        page.close(dlg_modal)

    def handle_out(page):
        page.close(dlg_modal)
        page.update()
        from .main_page import main_page
        page.appbar = None
        page.client_storage.clear()
        main_page(page)

    def handle_click(e):
        page.open(dlg_modal)

    dlg_modal = ft.AlertDialog(
        actions_alignment=ft.MainAxisAlignment.CENTER,
        adaptive=True,
        modal=True,
        content=ft.Text("Haqiqatdan ham hisobingizdan\nchiqmoqchimisiz?", text_align=ft.TextAlign.CENTER),
        actions=[
            ft.OutlinedButton(
                text="Ha",
                on_click=lambda e: handle_out(page),
                # Link the button to validation
                width=100,
                height=50,
                style=ft.ButtonStyle(
                    color='white',
                    bgcolor=TC,
                    shape=ft.RoundedRectangleBorder(radius=8),
                )
            ),
            ft.OutlinedButton(
                text="Yo'q",
                on_click=handle_close,
                # Link the button to validation
                width=100,
                height=50,
                style=ft.ButtonStyle(
                    color=TC,
                    bgcolor='white',
                    shape=ft.RoundedRectangleBorder(radius=8),
                )
            ),
        ],
    )

    logout_icon = ft.IconButton(
        icon=ft.Icons.LOGOUT,
        icon_color=TC,
        on_click=lambda e: handle_click(e)
    )

    image = ft.Image(src=os.path.abspath("assets/Ўз.svg"))

    # PopupMenuButton with language options
    language_menu = ft.PopupMenuButton(
        content=image,
        items=[
            ft.PopupMenuItem(text="Uzbekcha", data="uz",
                             on_click=lambda e: change_language(e.control.data)),
            ft.PopupMenuItem(text="Kirilcha", data="kr",
                             on_click=lambda e: change_language(e.control.data)),
        ]
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
                routes[route](page)  # Call the corresponding route function
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
                    padding=0,
                    text_style=ft.TextStyle(size=15),
                    color='#007577' if route == active_route else ft.colors.BLACK,
                ),
                on_click=lambda e, r=route: navigate(e, r)
            )
            for route, route_label in [
                ("Abu Mansur Motrudiy", abu_mansur_motrudiy.value),
                ("Tavilot al-Quron", appbar_tavilot.value),
                ("Qo'lyozma va sharhlar", appbar_menuscript.value),
                ("Zamonaviy tadqiqotlar", appbar_studies.value),
                ("Resurslar", appbar_resources.value),
                ("Mutaassib oqimlarga raddiyalar", appbar_refusal.value)

            ]
        ]

    def fetch_data(query):
        url = f"http://alquran.zerodev.uz/api/v2/studies/?q={query}"
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
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json().get("result", [])
        else:
            print("ERROR")
        return []

    def handle_submit(e):
        search.close_view(e.data)
        query = e.data.strip()

        if not query:
            search.controls.clear()
            search.update()
            return

        search_data = fetch_data(query)

        search.controls.clear()

        for search_detail in search_data:
            item_id = search_detail.get('id')

            # Pass both item_id and chapter_id as default arguments to the lambda function
            list_tile = ft.ListTile(
                key=item_id,
                data=search_detail.get('id'),
                on_click=lambda e: take_content_id(page, ids=e.control.data),
                title=ft.Text(
                    search_detail.get('title')
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
    page.update()