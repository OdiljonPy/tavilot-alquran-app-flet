import flet as ft
import os

from .surah_page import surah_page
from .al_quran_oquvchilariga import al_quron_oquvchilariga
from .about_us_page import about_us_page
from .menuscript import menuscript
from .studies import studies
from .resources import resources
from .refusal import refusal


def home(page):
    page.clean()
    page.scroll = True
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE
    TC = '#E9BE5F'

    # ----back button--------------------------------------------------------------------------------------------------------
    back_button = ft.Container(content=ft.Row(controls=[ft.Text(width=50),
                                                        ft.OutlinedButton(
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
                                                        ]
                                              )

                               )

    # -----------------------------------------------------------------------------------------------------------------------

    def buy_page(e):
        page.clean()
        page.add(divider, back_button, divider, buy_text, buy_things)

    def payment_page(e):
        page.clean()
        page.add(divider, back_button, text_premium, description_text)

    # -----Payment Page------------------------------------------------------------------------------------------------------

    text_premium = ft.Row(controls=[ft.Container(content=ft.Row(
        controls=[
            ft.Text('Premium version', color=TC, size=60, weight='bold')
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
        alignment=ft.alignment.center,
        image_src=os.path.abspath("assets/searchbg.png"),
        width=1000,
        height=200,
        image_fit='cover',
        image_opacity=1,
        padding=50

    )
    ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    description_text = ft.Row(controls=[
        ft.Text('Премиум версия орқали қуйидаги ҳусусиятларга эга бӯласиз', size=30, width=600,
                text_align=ft.TextAlign.CENTER)
    ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # ----Buy page content---------------------------------------------------------------------------------------------------
    buy_text = ft.Text('         Xaridlar', size=30, color='black', weight='bold')

    buy_things = ft.Container(content=ft.Row(controls=[
        ft.Text(width=50),
        ft.OutlinedButton(content=ft.Column(
            controls=[
                ft.Column(controls=[
                    ft.Text('')
                ]),
                ft.Row(controls=[
                    ft.Image(src=os.path.abspath("assets/tempImageu3T1ZX1.png")),
                    ft.Text(''),
                    ft.Column(controls=[
                        ft.Text('Tafsiri Hilol', size=25, color='black'),
                        ft.Text('Шайҳ Муҳаммад Содиқ Муҳаммад Юсуф', size=18, color='black'),
                        ft.Text(''),
                        ft.Row(controls=[
                            ft.Text('240 000 sum', size=20, color='black'),
                            ft.Text(width=120),
                            ft.OutlinedButton(
                                content=ft.Text('Xarid qilish', color='white'),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=22),
                                    bgcolor=TC
                                ),
                                on_click=payment_page
                            )
                        ]),

                    ],
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                    )
                ]),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        ),
            height=200,
            width=560,
            style=ft.ButtonStyle(
                color='white',
                shape=ft.RoundedRectangleBorder(radius=15),
                bgcolor='#FFFFFF'
            ),

        ),
    ],
    ))

    # ------Main page-------------------------------------------------------------------------------------------------------

    about_us_icon = ft.IconButton(
        icon=ft.Icons.INFO,
        icon_color=TC,
        on_click=lambda e: about_us_page(page, back_button)
    )

    logout_icon = ft.IconButton(
        icon=ft.Icons.LOGOUT,
        icon_color=TC,
        on_click=lambda e: None
    )

    image = ft.Image(src=os.path.abspath("assets/Ўз.svg"))

    # Callback function to handle language selection
    def on_language_select(e):
        selected_lang_text = e.control.content.value

        if selected_lang_text == 'English':
            pass
        #     image = ft.Image(src=)
        #
        # selected_language.value = selected_lang_text[:2].upper()
        page.update()

    # PopupMenuButton with language options
    language_menu = ft.PopupMenuButton(
        content=image,
        items=[
            ft.PopupMenuItem(text="Uzb", on_click=on_language_select),
            ft.PopupMenuItem(text="ru")
        ]
    )

    # def close_anchor(e):
    #     text = f"Color {e.control.data}"
    #     print(f"closing view from {text}")
    #     anchor.close_view(text)
    #
    # def handle_change(e):
    #     print(f"handle_change e.data: {e.data}")
    #
    # def handle_submit(e):
    #     print(f"handle_submit e.data: {e.data}")
    #
    # def handle_tap(e):
    #     print(f"handle_tap")
    #     anchor.open_view()
    #
    # search = ft.SearchBar(
    #     bar_bgcolor='white',
    #     bar_border_side=ft.BorderSide(color=TC, width=1),
    #     view_elevation=4,
    #     divider_color=ft.colors.AMBER,
    #     bar_leading=ft.Icon(ft.icons.SEARCH),
    #     bar_hint_text="Nima o'qimoqchisiz?...",
    #     view_hint_text="Choose a color from the suggestions...",
    #     on_change=handle_change,
    #     on_submit=handle_submit,
    #     on_tap=handle_tap,
    #     controls=[
    #         ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
    #         for i in range(10)
    #     ],
    # )

    entrance_logo = ft.Container(
        adaptive=True,
        content=ft.Row(
            controls=[
                ft.Image(
                    color='#007577',
                    src=os.path.abspath("assets/tA'VILOT_Монтажная_область1.png"),
                    fit=ft.ImageFit.COVER,
                    width=200,
                    height=100,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        height=180,
        alignment=ft.alignment.center,
        image_src=os.path.abspath("assets/searchbg.png"),
        width=page.adaptive,
        image_fit='fitWidth',
        padding=50

    )

    divider = ft.Divider(height=30)

    three_windows = ft.Container(
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
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -1)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияii_06p_02.svg"),
                                                     height=100, color=ft.Colors.WHITE)
                                        ]
                                    ),
                                    ft.Text("\n   Abu Mansur Matrudiy", size=10, color='white', expand=True)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=200,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
                        ),
                        ft.OutlinedButton(
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
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -1)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_03.png"),
                                                     height=100, color=ft.Colors.WHITE)
                                        ]
                                    ),
                                    ft.Text("\n   TA'VILOT AL-QURON O'QUVCHILARIGA", size=10, color='white',
                                            expand=True)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=200,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
                        ),
                        ft.OutlinedButton(
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
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -1)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_04.png"),
                                                     height=100, color=ft.Colors.WHITE)
                                        ]
                                    ),
                                    ft.Text("\n   Qo'lyozma va sharhlar", size=10, color='white', expand=True)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=200,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
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
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -1)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_05.png"),
                                                     height=100, color=ft.Colors.WHITE)
                                        ]
                                    ),
                                    ft.Text("\n   Zamonaviy tadqiqotlar", size=10, color='white', expand=True)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=200,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
                        ),
                        ft.OutlinedButton(
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
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -1)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_06.png"),
                                                     height=100, color=ft.Colors.WHITE)
                                        ]
                                    ),
                                    ft.Text("\n   Resurslar: O'quv qo'llanmalari va \n   O'QUVCHILARIGA", size=10,
                                            color='white', expand=True)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=200,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
                        ),
                        ft.OutlinedButton(
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
                                        controls=[
                                            ft.Image(src=os.path.abspath("assets/book-open_1.svg"),
                                                     offset=ft.Offset(0.5, -1)),
                                            ft.Image(src=os.path.abspath(
                                                "assets/Безымянный_1_Монтажная_область_1_копияr_Монтажная_область_1.png"),
                                                     height=100, color=ft.Colors.WHITE)
                                        ]
                                    ),
                                    ft.Text("\n   Mutaassib oqimlarga raddiyalar", size=10, color='white', expand=True)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                            ),
                            height=200,
                            width=400,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor='#E9BE5F',
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
                        ),
                    ]
                )
            ]
        ),
        alignment=ft.alignment.center
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
                expand=True,
                adaptive=True,
                text=route_label,
                style=ft.ButtonStyle(
                    text_style=ft.TextStyle(size=12),
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
            adaptive=True,
            leading=ft.Image(
                color='#007577',
                src=os.path.abspath("assets/tA'VILOT_Монтажная_область1.svg")
            ),
            leading_width=100,
            actions=[
                ft.Row(
                    adaptive=True,
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=25,
                    controls=[*generate_appbar_actions(),
                              ft.Text(width=20),
                              language_menu,
                              logout_icon,
                              about_us_icon],

                ),
            ],
            bgcolor='white',
            toolbar_height=80,
        )
        page.update()

    update_appbar()
    page.add(entrance_logo, ft.Text(height=10), three_windows, ft.Text(height=10))
    page.update()
