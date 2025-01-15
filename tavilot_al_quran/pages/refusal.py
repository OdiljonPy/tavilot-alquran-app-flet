import flet as ft
import os
import requests
from .refusal_detail import take_content_id



translations = {
    "uz": {
        "back_button_text": "Orqaga qaytish",
        "three_window_moturudiy": "\n   Abu Mansur Matrudiy",
    },
    "kr": {
        "back_button_text": "Оркага кайтиш",
        "three_window_moturudiy": "\n   Абу Мансур Мотрудий",
    }
}

def refusal(page):
    from .home_page import home
    from .about_us_page import about_us_page
    from .resources import resources
    from .refusal import refusal
    from .surah_page import surah_page
    from .menuscript import menuscript
    from .al_quran_oquvchilariga import al_quron_oquvchilariga
    from .studies import studies
    current_language = "uz"

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


    page.update()

    url = "http://176.221.28.202:8008/api/v1/refusal/"
    response = requests.get(url=url)
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
                        ft.Column(controls=[
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
        from tavilot_al_quran.main import main
        page.appbar = None
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
            ft.PopupMenuItem(text="Uzbekcha", data="uz", on_click=None),#language_selected),
            ft.PopupMenuItem(text="Kirilcha", data="kr", on_click=None)#language_selected),
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

    update_appbar()
    page.update()

