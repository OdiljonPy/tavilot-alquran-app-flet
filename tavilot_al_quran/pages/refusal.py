import flet as ft
import os
import requests

def refusal(page):
    from .refusal_detail import take_content_id
    from .home_page import home
    from .about_us_page import about_us_page
    from .resources import resources
    from .surah_page import surah_page
    from .menuscript import menuscript
    from .al_quran_oquvchilariga import al_quron_oquvchilariga
    from .studies import studies
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
        refusal(page)

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

    url = "http://alquran.zerodev.uz/api/v2/refusal/"
    headers = {
        "Content-Type": "application/json",
        "Accept-Language": page.client_storage.get('language')
    }
    response = requests.get(url=url, headers=headers)
    data_list = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Row(wrap=True, expand=True, scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                       adaptive=True))

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
            data_list.content.controls.append(motrudiy_data)
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
                ft.Row(controls=[back_button], expand=True, scale=ft.Scale(scale_x=0.95)),
                ft.Text(height=70),
                data_list
            ]
        )
    )
             )

    update_appbar(page, func_page=lambda e: refusal(page))
    page.update()
