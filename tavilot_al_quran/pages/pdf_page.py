import flet as ft
import pymupdf
from PIL import Image
from io import BytesIO
import base64
import requests


def pdf_page(page, pdf_file, back_button):
    page.scroll = False
    TC = '#E9BE5F'
    page.clean()
    loading = ft.ProgressRing(color=TC)
    page.add(ft.Container(
        expand=True,
        adaptive=True,
        content=loading,
        alignment=ft.alignment.center)
    )
    page.update()
    pdf_document = None
    current_page_index = 0
    total_pages = 0

    current_page_image = ft.Image(fit=ft.ImageFit.CONTAIN, width=700)

    # Function to load PDF from API response

    def load_pdf_from_api(pdf):
        nonlocal pdf_document, current_page_index, total_pages
        try:
            pdf_bytes = BytesIO(pdf)  # Load PDF as bytes
            pdf_document = pymupdf.open(stream=pdf_bytes, filetype="pdf")

            total_pages = pdf_document.page_count
            current_page_index = 0
            render_page()

        except Exception as e:
            current_page_image.src_base64 = ""
            page.snack_bar = ft.SnackBar(ft.Text(f"Error loading PDF: {e}"))
            page.snack_bar.open = True
            page.update()

    # Function to render a specific page
    def render_page():
        nonlocal current_page_index
        if pdf_document:
            try:
                # Define a higher resolution scale (e.g., 2.0 for 200%, 3.0 for 300%)
                zoom_x = 2.0  # Horizontal scaling factor
                zoom_y = 2.0  # Vertical scaling factor
                matrix = pymupdf.Matrix(zoom_x, zoom_y)

                # Render the page with the specified scaling
                page_obj = pdf_document.load_page(current_page_index)
                pixmap = page_obj.get_pixmap(matrix=matrix)
                image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

                buffer = BytesIO()
                image.save(buffer, format="PNG")
                buffer.seek(0)
                current_page_image.src_base64 = base64.b64encode(buffer.read()).decode("utf-8")

                prev_button.disabled = current_page_index == 0
                next_button.disabled = current_page_index == total_pages - 1
                page.update()
            except Exception as e:
                current_page_image.src_base64 = ""
                page.snack_bar = ft.SnackBar(ft.Text(f"Error rendering page: {e}"))
                page.snack_bar.open = True
                page.update()

    # Button actions for navigation
    def go_to_previous_page(e):
        nonlocal current_page_index
        if current_page_index > 0:
            current_page_index -= 1
            render_page()

    def go_to_next_page(e):
        nonlocal current_page_index
        if current_page_index < total_pages - 1:
            current_page_index += 1
            render_page()

    # Only create the buttons once
    prev_button = ft.ElevatedButton("Previous Page", on_click=go_to_previous_page, disabled=True, bgcolor=TC,
                                    color='white')
    next_button = ft.ElevatedButton("Next Page", on_click=go_to_next_page, disabled=True, bgcolor=TC, color='white')

    load_pdf_from_api(requests.get(pdf_file).content)
    page.update()
    page.clean()
    page.scroll = True


    page.add(ft.InteractiveViewer(
        expand=True,
        min_scale=0.1,
        max_scale=5,
        content=ft.Container(
            margin=10,
            adaptive=True,
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Column(
                adaptive=True,
                expand=True,
                controls=[
                    ft.Row(
                        adaptive=True,
                        alignment=ft.MainAxisAlignment.START,
                        controls=[back_button],
                    ),
                    current_page_image,
                    ft.Row(
                        spacing=20,
                        adaptive=True,
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            prev_button, next_button
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )))
