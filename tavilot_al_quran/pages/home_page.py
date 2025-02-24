import flet as ft
import os
from .al_quran_oquvchilariga import al_quron_oquvchilariga
from .menuscript import menuscript
from .studies import studies
from .resources import resources
from .refusal import refusal
from .surah_page import surah_page


def home(page):
    page.scroll = False
    page.clean()
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE
    TC = '#E9BE5F'
    from .pages_utils.appbar_search import update_appbar

    # -------Translation of the page-------------------------------------------------------------------------------------
    import json
    # Function to load JSON translation files
    def load_translation(lang):
        with open(f"locales/translations.json", "r", encoding="utf-8") as f:
            return json.load(f).get(lang)

    def change_language(e):
        page.client_storage.set('language', e)
        new_translation = load_translation(e)
        moturudiy_text.value = new_translation.get("three_window_moturudiy")
        al_quron_text.value = new_translation.get("al_quron_text")
        menuscript_text.value = new_translation.get('menuscript_text')
        studies_text.value = new_translation.get('studies_text')
        resources_text.value = new_translation.get('resources_text')
        refusal_text.value = new_translation.get('refusal_text')
        abu_mansur_motrudiy.value = new_translation.get('abu_mansur_motrudiy')
        appbar_tavilot.value = new_translation.get('appbar_tavilot')
        appbar_menuscript.value = new_translation.get('appbar_menuscript')
        appbar_studies.value = new_translation.get('appbar_studies')
        appbar_resources.value = new_translation.get('appbar_resources')
        appbar_refusal.value = new_translation.get('appbar_refusal')
        update_appbar(page)
        page.update()

    if page.client_storage.get('language'):
        current_translation = load_translation(page.client_storage.get('language'))
    else:
        current_translation = load_translation("uz")

    back_button_text = ft.Text(current_translation.get('back_button_text'), color='black'),
    moturudiy_text = ft.Text(current_translation.get('three_window_moturudiy'), size=page.window.width * 0.017,
                             color='white', expand=True)
    al_quron_text = ft.Text(current_translation.get('al_quron_text'), size=page.window.width * 0.017, color='white',
                            expand=True)
    menuscript_text = ft.Text(current_translation.get('menuscript_text'), size=page.window.width * 0.017, color='white',
                              expand=True)
    studies_text = ft.Text(current_translation.get('studies_text'), size=page.window.width * 0.017, color='white',
                           expand=True)
    resources_text = ft.Text(current_translation.get('resources_text'), size=page.window.width * 0.017,
                              color='white', expand=True, overflow=ft.TextOverflow.ELLIPSIS, no_wrap=True)
    refusal_text = ft.Text(current_translation.get('refusal_text'), size=page.window.width * 0.017,
                            color='white', expand=True)
    abu_mansur_motrudiy = ft.Text(current_translation.get('abu_mansur_motrudiy'))
    appbar_tavilot = ft.Text(current_translation.get('appbar_tavilot'))
    appbar_menuscript = ft.Text(current_translation.get('appbar_menuscript'))
    appbar_studies = ft.Text(current_translation.get('appbar_studies'))
    appbar_resources = ft.Text(current_translation.get('appbar_resources'))
    appbar_refusal = ft.Text(current_translation.get('appbar_refusal'))
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
        image=ft.DecorationImage(
            src=os.path.abspath("assets/searchbg.png"),
            fit=ft.ImageFit.FIT_WIDTH,
        ),
        width=page.adaptive,
        padding=50

    )

    three_windows = ft.Container(
        margin=10,
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
                                    moturudiy_text,
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

    def on_resize(e):
        moturudiy_text.size = page.window.width * 0.017
        al_quron_text.size = page.window.width * 0.017
        menuscript_text.size = page.window.width * 0.017
        studies_text.size = page.window.width * 0.017
        resources_text.size = page.window.width * 0.017
        refusal_text.size = page.window.width * 0.017
        abu_mansur_motrudiy.size = page.window.width * 0.017

        page.update()

    # Attach event listener
    page.on_resized = on_resize

    update_appbar(page)
    page.add(entrance_logo, three_windows)
    page.update()
