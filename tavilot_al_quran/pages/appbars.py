import flet as ft
from .al_quran_oquvchilariga import al_quron_oquvchilariga
from .menuscript import menuscript
from .studies import studies
from .refusal import refusal
from .resources import resources
import os
from .about_us_page import about_us_page
import requests

translations = {
    "uz": {
        "back_button_text": "Orqaga qaytish",
        "switch_language": "Switch Language",
    },
    "kr": {
        "back_button_text": "Оркага кайтиш",
        "switch_language": "Сменить язык",
    }
}

# Default language
current_language = "uz"


def appbar_all(page):
    TC = '#E9BE5F'
    from .home_page import home
    from .surah_page import surah_page

    # Function to update the UI text
    def update_ui(language):
        back_button.value = translations[language]["back_button_text"]
        # switch_language_label.value = translations[language]["switch_language"]
        page.update()

    # Popup menu button selection
    def language_selected(e):
        global current_language
        current_language = e.control.data
        update_ui(current_language)

    back_button_text = ft.Text(value=translations[current_language]["back_button_text"], color='black')

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
        from tavilot_al_quran.main import main
        page.appbar=None
        page.client_storage.clear()
        main(page)

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
            ft.PopupMenuItem(text="Uzbekcha", data="uz", on_click=language_selected),
            ft.PopupMenuItem(text="Kirilcha", data="kr", on_click=language_selected),
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
            # leading_width=,
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
        page.update()


    update_appbar()


def appbar_search(page):
    TC = '#E9BE5F'
    from .home_page import home
    from .surah_page import surah_page

