import flet as ft
import os


def al_quron_oquvchilariga(page, navbar_text1, navbar_text2, navbar_text3, back_button):
    page.clean()
    navbar_text2.style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color='#007577')
    navbar_text2.color = '#007577'
    navbar_text1.style = None
    navbar_text1.color = 'black'
    navbar_text3.style = None
    navbar_text3.color = 'black'
    page.update()
    TC = '#E9BE5F'

    text1 = ft.Text(value='         TAVILOT AL-QURON OQUVCHILARIGA', style='headlineLarge', color=TC)

    oquvchilarga = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(controls=[ft.Text(width=50),
                                 ft.OutlinedButton(content=ft.Column(
                                     controls=[
                                         ft.Column(controls=[
                                             ft.Text(),
                                             ft.Image(src=os.path.abspath("assets/book_1.svg")),
                                             ft.Text('\nIMOM MOTRUDIY', size=22),
                                             ft.Text(
                                                 'Имом Мотрудий таълимотлари ва \nунинг илмий меъроси ҳақидаги \nбатафсил маълумотлар',
                                                 size=18)
                                         ])
                                     ],
                                     horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                                 ),
                                     height=240,
                                     width=560,
                                     style=ft.ButtonStyle(
                                         shape=ft.RoundedRectangleBorder(radius=14),
                                     ),

                                 ),
                                 ft.Divider(),
                                 ft.Divider(),

                                 ft.OutlinedButton(content=ft.Column(
                                     controls=[
                                         ft.Column(controls=[
                                             ft.Text(),
                                             ft.Image(src=os.path.abspath("assets/book_1.svg")),
                                             ft.Text('\nIMOM MOTRUDIY', size=22),
                                             ft.Text(
                                                 'Имом Мотрудий таълимотлари ва \nунинг илмий меъроси ҳақидаги \nбатафсил маълумотлар',
                                                 size=18)
                                         ])
                                     ],
                                     horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                                 ),
                                     height=240,
                                     width=560,
                                     style=ft.ButtonStyle(
                                         shape=ft.RoundedRectangleBorder(radius=14),
                                     ),

                                 ),
                                 ft.Divider(),
                                 ft.Divider(),

                                 ft.OutlinedButton(content=ft.Column(
                                     controls=[
                                         ft.Column(controls=[
                                             ft.Text(),
                                             ft.Image(src=os.path.abspath("assets/book_1.svg")),
                                             ft.Text('\nIMOM MOTRUDIY', size=22),
                                             ft.Text(
                                                 'Имом Мотрудий таълимотлари ва \nунинг илмий меъроси ҳақидаги \nбатафсил маълумотлар',
                                                 size=18)
                                         ])
                                     ],
                                     horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                                 ),
                                     height=240,
                                     width=560,
                                     style=ft.ButtonStyle(
                                         shape=ft.RoundedRectangleBorder(radius=14),
                                     ),

                                 ),
                                 ]
                       ),
                ft.Row(controls=[
                    ft.Text(width=50),
                    ft.OutlinedButton(content=ft.Column(
                        controls=[
                            ft.Column(controls=[
                                ft.Text(),
                                ft.Image(src=os.path.abspath("assets/book_1.svg")),
                                ft.Text('\nIMOM MOTRUDIY', size=22),
                                ft.Text(
                                    'Имом Мотрудий таълимотлари ва \nунинг илмий меъроси ҳақидаги \nбатафсил маълумотлар',
                                    size=18)
                            ])
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                    ),
                        height=240,
                        width=560,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=14),
                        ),

                    ),
                    ft.Divider(),
                    ft.Divider(),

                    ft.OutlinedButton(content=ft.Column(
                        controls=[
                            ft.Column(controls=[
                                ft.Text(),
                                ft.Image(src=os.path.abspath("assets/book_1.svg")),
                                ft.Text('\nIMOM MOTRUDIY', size=22),
                                ft.Text(
                                    'Имом Мотрудий таълимотлари ва \nунинг илмий меъроси ҳақидаги \nбатафсил маълумотлар',
                                    size=18)
                            ])
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                    ),
                        height=240,
                        width=560,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=14),
                        ),

                    ),
                    ft.Divider(),
                    ft.Divider(),

                    ft.OutlinedButton(content=ft.Column(
                        controls=[
                            ft.Column(controls=[
                                ft.Text(),
                                ft.Image(src=os.path.abspath("assets/book_1.svg")),
                                ft.Text('\nIMOM MOTRUDIY', size=22),
                                ft.Text(
                                    'Имом Мотрудий таълимотлари ва \nунинг илмий меъроси ҳақидаги \nбатафсил маълумотлар',
                                    size=18)
                            ])
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                    ),
                        height=240,
                        width=560,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=14),
                        ),

                    ),
                ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER

        ),
        alignment=ft.alignment.center
    )
    divider = ft.Divider(height=30, color='white')
    div = ft.Column(controls=[ft.Text(height=150)])

    page.add(divider, back_button, div, text1, oquvchilarga)
