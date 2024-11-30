import time
import flet as ft
import os
import requests
from .surah_page import surah_page
from .al_quran_oquvchilariga import al_quron_oquvchilariga
from .about_us_page import about_us_page


def home(page):
    page.clean()
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.GREY_200
    page.scroll = True
    page.window_min_width = 1815
    TC = '#E9BE5F'
    page.update()


    # ----back button--------------------------------------------------------------------------------------------------------
    back_button = ft.Container(content=ft.Row(controls=[ft.Text(width=50),
                                                        ft.OutlinedButton(
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
                                                        ]
                                              )

                               )
    # -----------------------------------------------------------------------------------------------------------------------

    navbar_text1 = ft.Text('Asosiy Sahifa', color='#007577', size=20, style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color='#007577'))
    navbar_text2 = ft.Text("TA'VILOT AL-QURON O'QUVCHILARIGA", color='black', size=20, style=None)
    navbar_text3 = ft.Text('DASTUR XAQIDA', color='black', size=20, style=None)

    gesture_text1 = ft.GestureDetector(adaptive=True, content=navbar_text1, on_tap=lambda e: home(page))
    gesture_text2 = ft.GestureDetector(adaptive=True, content=navbar_text2, on_tap=lambda e: al_quron_oquvchilariga(page, navbar_text1, navbar_text2, navbar_text3, back_button))
    gesture_text3 = ft.GestureDetector(adaptive=True, content=navbar_text3, on_tap=lambda e: about_us_page(page, navbar_text1, navbar_text2, navbar_text3))


    navbar_text1.style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color='#007577')
    navbar_text1.color = '#007577'
    navbar_text2.style = None
    navbar_text2.color = 'black'
    navbar_text3.style = None
    navbar_text3.color = 'black'

    def buy_page(e):
        page.clean()
        page.add(divider, back_button, divider, buy_text, buy_things)

    def payment_page(e):
        page.clean()
        page.add(divider, back_button, text_premium, description_text)


#-----Payment Page------------------------------------------------------------------------------------------------------

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
        ft.Text('Премиум версия орқали қуйидаги ҳусусиятларга эга бӯласиз', size=30, width=600, text_align=ft.TextAlign.CENTER)
    ],
        alignment=ft.MainAxisAlignment.CENTER
    )

# ----Buy page content---------------------------------------------------------------------------------------------------
    buy_text = text = ft.Text('         Xaridlar', size=30, color='black', weight='bold')

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




    # ------Main page--------------------------------------------------------------------------------------------------------

    desktop_size = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Image(src=os.path.abspath("assets/maximize-3.png")),
                controls=[
                    ft.Text('hi')
                ],
                width=38,
                height=50
            )
        ]
    )

    hatchup_menu = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Image(src=os.path.abspath("assets/archive-minus.svg")),
                controls=[
                    ft.Text('hi')
                ],
                width=38,
                height=50
            )
        ]
    )

    oyat_menu = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Image(src=os.path.abspath("assets/note-2.svg")),
                controls=[
                    ft.Text('hi')
                ],
                width=38,
                height=50
            )
        ]
    )

    # PopupMenuButton with font options
    font_menu = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Image(src=os.path.abspath("assets/smallcaps.svg")),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Arial"), on_click=None
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Courier New"), on_click=None
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Times New Roman"), on_click=None
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Verdana"), on_click=None
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Georgia"), on_click=None
                    ),

                ],
                width=38,
                height=50
            )
        ]
    )

    image = ft.Image(src=os.path.abspath("assets/Ўз.svg"))

    # Callback function to handle language selection
    def on_language_select(e):
        selected_lang_text = e.control.content.value

        if selected_lang_text == 'English':
            pass
        #     image = ft.Image(src=)
        #
        # selected_language.value = selected_lang_text[:2].upper()
        page.update()

    # PopupMenuButton with language options
    language_menu = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=image,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("English"), on_click=on_language_select
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Uzbek"), on_click=on_language_select
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Russian"), on_click=on_language_select
                    ),
                ],
                width=38,
                height=50
            )
        ]
    )
    # Function to toggle theme
    is_light_mode = True

    # Function to handle theme toggle and change background color
    def change_theme(e):
        nonlocal is_light_mode
        if e.control == light_button:
            page.theme_mode = ft.ThemeMode.LIGHT
            is_light_mode = True
            light_button.bgcolor = TC  # Active background color for light mode
            dark_button.bgcolor = ft.colors.TRANSPARENT  # Inactive background color for dark mode
        elif e.control == dark_button:
            page.theme_mode = ft.ThemeMode.DARK
            is_light_mode = False
            dark_button.bgcolor = TC  # Active background color for dark mode
            light_button.bgcolor = ft.colors.TRANSPARENT  # Inactive background color for light mode
        page.update()  # Update the page to reflect changes

    # Create a switch for toggling themes
    light_button = ft.IconButton(ft.icons.LIGHT_MODE, on_click=change_theme, bgcolor=TC)
    dark_button = ft.IconButton(ft.icons.DARK_MODE, on_click=change_theme)

    theme_switcher = ft.Container(
        content=ft.Row(
            controls=[light_button, dark_button],
            spacing=0
        ),
        bgcolor='#FFFFFF',
        border_radius=20
    )


    def close_anchor(e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        anchor.close_view(text)

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        print(f"handle_tap")
        anchor.open_view()

    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_leading=ft.Icon(ft.icons.SEARCH),
        bar_hint_text="Nima o'qimoqchisiz?...",
        view_hint_text="Choose a color from the suggestions...",
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=[
            ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
            for i in range(10)
        ],
    )

    new_one = ft.Container(content=ft.Row(
        controls=[
            anchor
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
        alignment=ft.alignment.center,
        image_src=os.path.abspath("assets/searchbg.png"),
        width=page.adaptive,
        height=250,
        image_fit='cover',
        padding=50

    )

    divider = ft.Divider(height=30, color='white')

    three_windows = ft.Container(
        adaptive=True,
        content=ft.Row(
            spacing=40,
            adaptive=True,
            controls=[
                ft.OutlinedButton(
                    adaptive=True,
                    content=ft.Column(
                        adaptive=True,
                        controls=[
                            ft.Column(
                                adaptive=True,
                                controls=[
                                    ft.Text('')
                                ]
                            ),
                            ft.Row(
                                adaptive=True,
                                controls=[
                                    ft.Image(src=os.path.abspath("assets/book-open_1.svg"))
                                ]
                            ),
                            ft.Column(
                                adaptive=True,
                                controls=[
                                    ft.Text("\nTA'VILOT AL-QURON \nO'QUVCHILARIGA", size=25, color='white')
                                ]
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                    ),
                    height=200,
                    width=550,
                    style=ft.ButtonStyle(
                        color='white',
                        bgcolor='#E9BE5F',
                        shape=ft.RoundedRectangleBorder(radius=20),
                    ),
                    on_click=lambda e: al_quron_oquvchilariga(page, navbar_text1, navbar_text2, navbar_text3, back_button)

                ),

                ft.OutlinedButton(
                    adaptive=True,
                    content=ft.Column(
                        adaptive=True,
                        controls=[
                            ft.Column(
                                adaptive=True,
                                controls=[
                                    ft.Text('')
                                ]),
                            ft.Row(
                                adaptive=True,
                                controls=[
                                    ft.Image(src=os.path.abspath("assets/shopping-bag_1.svg"))
                                ]),
                            ft.Column(
                                adaptive=True,
                                controls=[
                                    ft.Text('\nXARIDLAR', size=25, color='black')
                                ])
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                    ),
                    height=200,
                    width=550,
                    style=ft.ButtonStyle(
                        color='white',
                        bgcolor='#E9BE5F',
                        shape=ft.RoundedRectangleBorder(radius=20),
                    ),
                    on_click=buy_page
                ),

                ft.OutlinedButton(
                    adaptive=True,
                    content=ft.Column(
                        adaptive=True,
                        controls=[
                            ft.Column(
                                adaptive=True,
                                controls=[
                                    ft.Text('')
                                ]),
                            ft.Row(
                                adaptive=True,
                                controls=[
                                    ft.Image(src=os.path.abspath("assets/info_1.svg"))
                                ]),
                            ft.Column(
                                adaptive=True,
                                controls=[
                                    ft.Text('\nDASTUR XAKIDA', size=25, color='black')
                                ])
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                    ),
                    height=200,
                    width=550,
                    style=ft.ButtonStyle(
                        color='white',
                        bgcolor='#E9BE5F',
                        shape=ft.RoundedRectangleBorder(radius=20),
                    ),
                    on_click=lambda e: about_us_page(page, navbar_text1, navbar_text2, navbar_text3)
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    text = ft.Text('            Suralar', size=30, color='black', weight='bold')

    gv = ft.Row(wrap=True, expand=True, alignment=ft.MainAxisAlignment.CENTER)

    # API request
    url = "https://alquran.zerodev.uz/api/v1/chapters/"
    response = requests.get(url)

    if response.status_code == 200:
        result_lists = response.json().get("result")

        for surah in result_lists:
            type_choice = "Makkiy" if surah.get("type_choice") == 1 else "Madaniy"
            gv.controls.append(ft.OutlinedButton(content=ft.Column(
                controls=[
                    ft.Column(controls=[
                        ft.Text('')
                    ]),
                    ft.Row(controls=[
                        ft.Container(content=ft.Text(surah.get('id')), image_src=os.path.abspath("assets/Star1.png"), width=40, height=40, alignment=ft.alignment.center),
                        ft.Container(content=ft.Row(controls=[
                            ft.Text(f"{surah.get('name')} \n{type_choice}, {surah.get('verse_number')} OYAT", size=25, color='black'),
                            ft.Text(f"{surah.get('name_arabic')} \n{surah.get('verse_number')} oyat", size=20, color='black', text_align=ft.TextAlign.RIGHT)
                        ],
                            spacing=100
                        )
                        )
                    ]
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
            ),
                height=120,
                width=580,
                style=ft.ButtonStyle(
                    color='white',
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
                on_click=lambda e: surah_page(page),

            ),
            )
    else:
        print("Error retrieving data")

    page.appbar = ft.AppBar(
        adaptive=True,
        leading=ft.Image(src=os.path.abspath("assets/maturidiy_logo.png")),
        leading_width=100,
        actions=[
            gesture_text1,
            ft.Text(width=45),
            gesture_text2,
            ft.Text(width=30),
            gesture_text3,
            ft.Text(width=250),
            theme_switcher,
            ft.Text(width=100),
            language_menu,
            ft.Text(width=30),
            font_menu,
            ft.Text(width=30),
            oyat_menu,
            ft.Text(width=30),
            hatchup_menu,
            ft.Text(width=30),
            desktop_size
        ],
        bgcolor='white',
        toolbar_height=77,
    )
    page.add(new_one, three_windows, divider, text, ft.Container(gv, alignment=ft.alignment.center))
    page.update()