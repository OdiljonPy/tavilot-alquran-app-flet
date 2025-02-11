import flet as ft
from ..al_quran_oquvchilariga import al_quron_oquvchilariga
from ..surah_page import surah_page
from ..menuscript import menuscript
from ..studies import studies
from ..resources import resources
from ..refusal import refusal
from ..home_page import home
import os
from ..about_us_page import about_us_page

routes = {
        "Abu Mansur Motrudiy": al_quron_oquvchilariga,
        "Tavilot al-Quron": surah_page,
        "Qo'lyozma va sharhlar": menuscript,
        "Zamonaviy tadqiqotlar": studies,
        "Resurslar": resources,
        "Mutaassib oqimlarga raddiyalar": refusal
    }

active_route = None

def navigate(e, route, page):
    global active_route
    if route != active_route:
        active_route = route
        # update_appbar(page)  # Refresh the AppBar with updated colors
        if route in routes:
            routes[route](page)  # Call the corresponding route function
        else:
            page.add(ft.Text("404 - Page Not Found", size=20))
            page.update()


TC = '#E9BE5F'

def update_appbar(page, search=None):


    # -------Translation of the page-------------------------------------------------------------------------------------
    import json
    # Function to load JSON translation files
    def load_translation(lang):
        with open(f"locales/translations.json", "r", encoding="utf-8") as f:
            return json.load(f).get(lang)

    def change_language(e):
        page.client_storage.set('language', e)
        new_translation = load_translation(e)
        # moturudiy_text.value = new_translation.get("three_window_moturudiy")
        # al_quron_text.value = new_translation.get("al_quron_text")
        # menuscript_text.value = new_translation.get('menuscript_text')
        # studies_text.value = new_translation.get('studies_text')
        # resources_text.value = new_translation.get('resources_text')
        # refusal_text.value = new_translation.get('refusal_text')
        abu_mansur_motrudiy.value = new_translation.get('abu_mansur_motrudiy')
        appbar_tavilot.value = new_translation.get('appbar_tavilot')
        appbar_menuscript.value = new_translation.get('appbar_menuscript')
        appbar_studies.value = new_translation.get('appbar_studies')
        appbar_resources.value = new_translation.get('appbar_resources')
        appbar_refusal.value = new_translation.get('appbar_refusal')
        update_appbar(page, search)
        page.update()

    if page.client_storage.get('language'):
        current_translation = load_translation(page.client_storage.get('language'))
    else:
        current_translation = load_translation("uz")

    abu_mansur_motrudiy = ft.Text(current_translation.get('abu_mansur_motrudiy'))
    appbar_tavilot = ft.Text(current_translation.get('appbar_tavilot'))
    appbar_menuscript = ft.Text(current_translation.get('appbar_menuscript'))
    appbar_studies = ft.Text(current_translation.get('appbar_studies'))
    appbar_resources = ft.Text(current_translation.get('appbar_resources'))
    appbar_refusal = ft.Text(current_translation.get('appbar_refusal'))
    #-------------------------------------------------------------------------------------------------------------------

    about_us_icon = ft.IconButton(
        icon=ft.Icons.INFO,
        icon_color=TC,
        on_click=lambda e: about_us_page(page)
    )

    def handle_close(e):
        page.close(dlg_modal)

    def handle_out(page):
        page.close(dlg_modal)
        page.update()
        from ..main_page import main_page
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
                on_click=lambda e, r=route: navigate(e, r, page)
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

    if search:
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
            leading_width=100,
            leading=ft.Container(
                on_click=lambda e: home(page),
                content=ft.Image(
                    expand=True,
                    color='#007577',
                    src=os.path.abspath("assets/tA'VILOT_Монтажная_область1.svg")
                )),
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
    else:
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
            leading_width=100,
            leading=ft.Container(
                on_click=lambda e: home(page),
                content=ft.Image(
                    expand=True,
                    color='#007577',
                    src=os.path.abspath("assets/tA'VILOT_Монтажная_область1.svg")
                )),
            actions=[
                ft.Row(
                    adaptive=True,
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,  # Reduced spacing to allow more room for items
                    controls=[
                        language_menu,
                        logout_icon,
                        about_us_icon,
                    ],
                ),
            ],
            bgcolor='white',
            toolbar_height=80,
        )
