import flet as ft
import os
from .al_quran_oquvchilariga import al_quron_oquvchilariga
from .about_us_page import about_us_page
from .menuscript import menuscript
from .studies import studies
from .resources import resources
from .refusal import refusal
from .surah_page import surah_page



translations = {
    "uz": {
        "back_button_text": "Orqaga qaytish",
        "three_window_moturudiy": "\n   Abu Mansur Matrudiy",
        "al_quron_text": "\n   Ta'vilot Al-Quron",
        'menuscript_text': "\n   Qo'lyozma va sharhlar",
        "studies_text": "\n   Zamonaviy tadqiqotlar",
        "resources_text": "\n   Resurslar: O'quv qo'llanmalari va ilmiy manba'lar",
        "refusal_text": "\n   Mutaassib oqimlarga raddiyalar",
        "abu_mansur_motrudiy": "Abu Mansur Motrudiy"
    },
    "kr": {
        "back_button_text": "Оркага кайтиш",
        "three_window_moturudiy": "\n   Абу Мансур Мотрудий",
        "al_quron_text": "\n   Тавилот Ал-Курон",
        'menuscript_text': "\n   Колйозма ва шархлар",
        "studies_text": "\n   Замонавий тадкикотлар",
        "resources_text": "\n   Ресурслар: Окув колланмалари ва \n   илмий манбалар",
        "refusal_text": "\n   Муттаасиб окимларга раддийалар",
        "abu_mansur_motrudiy": "Абу Мансур Мотрудий"
    }
}

def home(page):
    current_language = "uz"

    page.scroll = False
    page.clean()
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE
    TC = '#E9BE5F'

    # ----back button--------------------------------------------------------------------------------------------------------
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

    # ------Main page---------------------------------------------------------------------------------------------------

    entrance_logo = ft.Container(
        adaptive=True,
        content=ft.Row(
            controls=[
                ft.Image(
                    color='#007577',
                    src=os.path.abspath("assets/tA'VILOT_Монтажная_область1.png"),
                    fit=ft.ImageFit.COVER,
                    width=320,
                    height=200,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        height=220,
        alignment=ft.alignment.center,
        image_src=os.path.abspath("assets/searchbg.png"),
        width=page.adaptive,
        image_fit='fitWidth',
        padding=50

    )

    three_window_moturudiy = ft.Text(value=translations[current_language]["three_window_moturudiy"], size=page.window_width * 0.017, color='white', expand=True)
    al_quron_text = ft.Text(value=translations[current_language]["al_quron_text"], size=page.window_width * 0.017, color='white', expand=True)
    menuscript_text = ft.Text(value=translations[current_language]["refusal_text"], size=page.window_width * 0.017, color='white', expand=True)
    studies_text = ft.Text(value=translations[current_language]["studies_text"], size=page.window_width * 0.017, color='white', expand=True)
    resources_text = ft.Text(value=translations[current_language]["resources_text"], size=page.window_width * 0.014,
                                            color='white', expand=True)
    refusal_text = ft.Text(value=translations[current_language]["refusal_text"], size=page.window_width * 0.017, color='white', expand=True)
    abu_mansur_motrudiy = ft.Text(value=translations[current_language]["abu_mansur_motrudiy"])




    three_windows = ft.Container(
        margin=30,
        expand=True,
        adaptive=True,
        content=ft.Column(
            adaptive=True,
            expand=True,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    run_spacing=10,
                    spacing=10,
                    adaptive=True,
                    controls=[
                        ft.OutlinedButton(
                            expand=True,
                            adaptive=True,
                            content=ft.Column(
                                expand=True,
                                adaptive=True,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        height=110,
                                        spacing=20,
                                        adaptive=True,
                                        expand=True,
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -0.2)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияii_06p_02.svg"),
                                                height=100, color=ft.Colors.WHITE, offset=ft.Offset(0, 0.2))
                                        ]
                                    ),
                                    three_window_moturudiy
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=300,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: al_quron_oquvchilariga(page)
                        ),
                        ft.OutlinedButton(
                            expand=True,
                            adaptive=True,
                            content=ft.Column(
                                expand=True,
                                adaptive=True,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        height=110,
                                        spacing=20,
                                        adaptive=True,
                                        expand=True,
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -0.2)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_03.png"),
                                                height=100, color=ft.Colors.WHITE, offset=ft.Offset(0, 0.2))
                                        ]
                                    ),
                                    al_quron_text
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=300,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: surah_page(page)
                        ),
                        ft.OutlinedButton(
                            expand=True,
                            adaptive=True,
                            content=ft.Column(
                                expand=True,
                                adaptive=True,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        height=110,
                                        spacing=20,
                                        adaptive=True,
                                        expand=True,
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -0.2)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_04.png"),
                                                height=100, color=ft.Colors.WHITE, offset=ft.Offset(0, 0.2))
                                        ]
                                    ),
                                    menuscript_text
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=300,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: menuscript(page)
                        ),
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    run_spacing=10,
                    spacing=10,
                    adaptive=True,
                    controls=[
                        ft.OutlinedButton(
                            expand=True,
                            adaptive=True,
                            content=ft.Column(
                                expand=True,
                                adaptive=True,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        height=110,
                                        spacing=20,
                                        adaptive=True,
                                        expand=True,
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -0.2)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_05.png"),
                                                height=100, color=ft.Colors.WHITE, offset=ft.Offset(0, 0.2))
                                        ]
                                    ),
                                    studies_text
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=300,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: studies(page)
                        ),
                        ft.OutlinedButton(
                            expand=True,
                            adaptive=True,
                            content=ft.Column(
                                expand=True,
                                adaptive=True,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        height=110,
                                        spacing=20,
                                        adaptive=True,
                                        expand=True,
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -0.2)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_06.png"),
                                                height=100, color=ft.Colors.WHITE, offset=ft.Offset(0, 0.2))
                                        ]
                                    ),
                                    resources_text
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=300,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: resources(page)
                        ),
                        ft.OutlinedButton(
                            expand=True,
                            adaptive=True,
                            content=ft.Column(
                                expand=True,
                                adaptive=True,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        height=110,
                                        spacing=20,
                                        adaptive=True,
                                        expand=True,
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -0.2)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_Монтажная_область_1.png"),
                                                height=100, color=ft.Colors.WHITE, offset=ft.Offset(0, 0.2))
                                        ]
                                    ),
                                    refusal_text
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=300,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: refusal(page)
                        ),
                    ]
                )
            ]
        ),
        alignment=ft.alignment.center
    )


    # Function to update the UI text
    def update_ui(language):
        back_button.value = translations[language]["back_button_text"]
        three_window_moturudiy.value = translations[language]['three_window_moturudiy']
        al_quron_text.value = translations[language]['al_quron_text']
        refusal_text.value = translations[language]['refusal_text']
        studies_text.value = translations[language]['studies_text']
        resources_text.value = translations[language]['resources_text']
        refusal_text.value = translations[language]['refusal_text']
        abu_mansur_motrudiy.value = translations[current_language]['abu_mansur_motrudiy']
        update_appbar()
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

    def on_resize(e):
        # Update text size based on window width
        three_window_moturudiy.size = page.window_width * 0.017
        al_quron_text.size = page.window_width * 0.017
        menuscript_text.size = page.window_width * 0.017
        studies_text.size = page.window_width * 0.017
        resources_text.size = page.window_width * 0.014
        refusal_text.size = page.window_width * 0.017
        abu_mansur_motrudiy.size = page.window_width * 0.017

        page.update()

    # Attach event listener
    page.on_resize = on_resize

    update_appbar()
    page.add(entrance_logo, three_windows)
    page.update()
