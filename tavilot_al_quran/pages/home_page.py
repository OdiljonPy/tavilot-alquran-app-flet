import flet as ft
import os
from .surah_page import surah_page
from .al_quran_oquvchilariga import al_quron_oquvchilariga
from .about_us_page import about_us_page
from .menuscript import menuscript
from .studies import studies
from .resources import resources
from .refusal import refusal
from .appbars import appbar_all

def home(page):
    page.scroll = False
    page.clean()
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE
    TC = '#E9BE5F'

    # ----back button--------------------------------------------------------------------------------------------------------
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

    # ------Main page---------------------------------------------------------------------------------------------------

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
                                    ft.Text("\n   Abu Mansur Matrudiy", size=18, color='white', expand=True)
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
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
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
                                    ft.Text("\n   TA'VILOT AL-QURON", size=18, color='white', expand=True)
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
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
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
                                    ft.Text("\n   Qo'lyozma va sharhlar", size=18, color='white', expand=True)
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
                                    ft.Text("\n   Zamonaviy tadqiqotlar", size=18, color='white', expand=True)
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
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
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
                                    ft.Text("\n   Resurslar: O'quv qo'llanmalari va \n   ilmiy manba'lar", size=18,
                                            color='white', expand=True)
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
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
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
                                    ft.Text("\n   Mutaassib oqimlarga raddiyalar", size=18, color='white', expand=True)
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
                            on_click=lambda e: al_quron_oquvchilariga(page, back_button)
                        ),
                    ]
                )
            ]
        ),
        alignment=ft.alignment.center
    )

    appbar_all(page)
    page.add(entrance_logo, three_windows)
    page.update()
