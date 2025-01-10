import flet as ft
import requests
# from fletify import FletifyHTML
from .htmp_parser import FletifyHTML
def about_us_page(page, back_button):
    page.clean()

    loading = ft.ProgressRing()

    page.add(ft.Container(
        content=ft.Column(controls=[ft.Text(height=480), loading], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center))

    page.update()

    url = "http://176.221.28.202:8008/api/v1/about/"
    response = requests.get(url=url)
    print(response.json().get('result').get('description'))
    cleaned_data = FletifyHTML(response.json().get('result').get('description')).get_flet()
    print(cleaned_data)
    # print(cleaned_data.Alignment)

    if response.status_code == 200:
        page.clean()
        about_result = cleaned_data
        page.update()
    else:
        about_result = None
        page.update()
    page.add(ft.Row(controls=[about_result], alignment=ft.MainAxisAlignment.CENTER))
# ft.Container(alignment=ft.alignment.center)