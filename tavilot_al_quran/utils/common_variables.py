import flet as ft
from .validations import limit_length

TC = '#E9BE5F'

password = ft.TextField(
    label='Password',
    password=True,
    can_reveal_password=True,
    width=400,
    border_width=2,
    border_radius=10,
    border_color=TC,
    text_style=ft.TextStyle(weight="bold"),
)
