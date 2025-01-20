import flet as ft
from ..al_quran_oquvchilariga import al_quron_oquvchilariga
from ..surah_page import surah_page
from ..menuscript import menuscript
from ..studies import studies
from ..resources import resources
from ..refusal import refusal
from ..home_page import home
import os




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

def generate_appbar_actions(page):
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
            ("Abu Mansur Motrudiy", "Abu Mansur Motrudiy"),
            ("Tavilot al-Quron", "Tavilot al-Quron"),
            ("Qo'lyozma va sharhlar", "Qo'lyozma va sharhlar"),
            ("Zamonaviy tadqiqotlar", "Zamonaviy tadqiqotlar"),
            ("Resurslar", "Resurslar"),
            ("Mutaassib oqimlarga raddiyalar", "Mutaassib oqimlarga raddiyalar")

        ]
    ]

def update_appbar(page, search):
    page.appbar = ft.AppBar(
        title=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
            adaptive=True,
            controls=[
                *generate_appbar_actions(page),
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

