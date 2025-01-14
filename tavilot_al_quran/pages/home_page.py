import flet as ft
import os
from .surah_page import surah_page
from .al_quran_oquvchilariga import al_quron_oquvchilariga
from .about_us_page import about_us_page
from .menuscript import menuscript
from .studies import studies
from .resources import resources
from .refusal import refusal
from .appbars import appbar_all, current_language

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

def home(page):
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

    three_window_moturudiy = ft.Text(value=translations[current_language]["three_window_moturudiy"], size=18, color='white', expand=True)

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
