import flet as ft
from pages.main_page import main_page
import os

def main(page: ft.Page):
    font_path = os.path.join(os.path.dirname(__file__), "fonts", "Amiri-Regular.ttf")
    font_page_trajan = os.path.join(os.path.dirname(__file__), "fonts", "Trajan.ttf")

    page.theme = ft.Theme(
        font_family="Amiri"
    )

    page.fonts = {
        "Amiri": font_path,
        "Trajan": font_page_trajan
    }

    main_page(page)


if __name__ == "__main__":
    ft.app(target=main)
