import time
import flet as ft
import requests
import os



def surah_page(page):
    pass
    # page.clean()
    # page.scroll = False
    # from tavilot_al_quran.main import main
    # from .html_pdf_handler import render_description
    # from .pages_utils.appbar_search import update_appbar
    # loading = ft.ProgressRing(color=TC)
    # page.add(ft.Container(
    #     expand=True,
    #     adaptive=True,
    #     content=loading,
    #     alignment=ft.alignment.center)
    # )
    #
    # divider = ft.Container(
    #     adaptive=True,
    #     bgcolor=TC,  # The line's color
    #     width=5,  # Thickness of the line
    #     height=page.window_width,  # Match the height of the containers
    # )
    #
    # def on_resize(event):
    #     divider.height = page.window_width
    #     page.update()
    #
    # # Attach resize event handler
    # page.on_resize = on_resize
    #
    #
    # # -------Back connection juz----------------------------------------------------------------------------------------
    #
    #
    # # -----Close button logic---------------------------------------------------------------------------------------------
    # button3 = ft.TextButton(
    #     text='< Yopish',
    #     data='button3',
    #     style=ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=TC),
    #     on_click=lambda e: toggle_widgets(e)
    # )
    # page.clean()
    #
    # is_cleaned = True
    #
    # column_data = [button3]
    # response_data = response
    # if response_data.status_code == 200:
    #     response_list = response_data.json().get('result')
    #     for response_detail in response_list:
    #         column_data.append(ft.Container(adaptive=True, content=ft.Text(response_detail.get('id'), color='black'),
    #                                         shape=ft.BoxShape.CIRCLE, width=60,
    #                                         height=60, alignment=ft.alignment.center,
    #                                         border=ft.border.all(2, color=TC)))
    #
    # # Function to toggle widgets
    # def toggle_widgets(e):
    #     nonlocal is_cleaned
    #     if is_cleaned:
    #         button3.text = "Ochish >"
    #         button3.style = ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=TC)
    #         side_bar.controls[0].controls = column_data
    #         side_bar.controls[0].width = 100
    #     else:
    #         button3.text = "< Yopish"
    #         button3.style = ft.ButtonStyle(text_style=ft.TextStyle(size=20), color=TC)
    #         side_bar.controls[0].width = 350
    #         side_bar.controls[0].controls = [ft.Row(
    #             spacing=20,
    #             adaptive=True,
    #             alignment=ft.MainAxisAlignment.CENTER,
    #             controls=[
    #                 button1,
    #                 button2,
    #                 button3
    #             ]
    #         ),
    #             list_view
    #         ]
    #     is_cleaned = not is_cleaned  # Toggle the state
    #     page.update()
    #
    #
    #
    #
    #
    # # def fetch_data(query):
    # #     url = f"http://176.221.28.202:8008/api/v1/search/?q={query}&search_type={button_number}"
    # #     headers = ""
    # #     if page.client_storage.get('access_token'):
    # #         headers = {
    # #             "Content-Type": "application/json",
    # #             "Authorization": f"Bearer {page.client_storage.get('access_token')}"
    # #         }
    # #     else:
    # #         headers = {
    # #             "Content-Type": "application/json",
    # #         }
    # #     response = requests.get(url=url, headers=headers)
    # #     if response.status_code == 200:
    # #         return response.json().get("result", [])
    # #     else:
    # #         print("ERROR")
    # #     return []
    # #
    # #
    # # def scroll_to_item(item_id, chapter_id):
    # #
    # #     # Perform the necessary actions (e.g., highlight or take some action with chapter_id)
    # #     take_id(chapter_id, number=button_number)
    # #
    # #     # Find the target element
    # #     target_element = next((control for control in right_display.controls if control.key == item_id), None)
    # #
    # #     if target_element:
    # #         # Apply highlight style
    # #         original_bgcolor = target_element.controls[0].controls[0].bgcolor
    # #         target_element.controls[0].controls[0].bgcolor = "yellow"
    # #         target_element.update()
    # #
    # #         # Function to remove highlight after a delay
    # #         def remove_highlight():
    # #             # Sleep for 3 seconds
    # #             time.sleep(3)
    # #             # Restore original background color
    # #             target_element.controls[0].controls[0].bgcolor = original_bgcolor
    # #             target_element.update()
    # #
    # #     # Scroll to the target element
    # #     right_display.scroll_to(key=f"{item_id}", duration=700, curve=ft.AnimationCurve.BOUNCE_OUT)
    # #     remove_highlight()
    # #     page.update()
    # #
    # # def handle_submit(e):
    # #     search.close_view(e.data)
    # #     query = e.data.strip()
    # #
    # #     if not query:
    # #         search.controls.clear()
    # #         search.update()
    # #         return
    # #
    # #     search_data = fetch_data(query)
    # #
    # #     search.controls.clear()
    # #
    # #     def create_on_click_handler(item_id, chapter_id):
    # #         return lambda e: scroll_to_item(item_id, chapter_id)
    # #
    # #     for search_detail in search_data:
    # #         item_id = search_detail.get('id')
    # #         chapter_id = search_detail.get('chapter_id')
    # #
    # #         # Pass both item_id and chapter_id as default arguments to the lambda function
    # #         list_tile = ft.ListTile(
    # #             key=item_id,
    # #             on_click=create_on_click_handler(item_id, chapter_id),
    # #             title=ft.Text(
    # #                 f"{search_detail.get('chapter_name')}, {search_detail.get('number')} - oyat"
    # #             )
    # #         )
    # #         search.controls.append(list_tile)
    # #
    # #     search.open_view()
    # #     search.update()  # Refresh the UI with the new data
    # #
    # # search = ft.SearchBar(
    # #     width=180,
    # #     height=50,
    # #     expand=True,
    # #     bar_bgcolor="white",
    # #     bar_border_side=ft.BorderSide(color=ft.colors.BLUE, width=1),
    # #     divider_color=ft.colors.AMBER,
    # #     bar_leading=ft.Icon(ft.icons.SEARCH),
    # #     bar_hint_text="Nima o'qimoqchisiz?...",
    # #     view_hint_text="Searching...",
    # #     on_submit=handle_submit,  # Trigger search when user submits the query
    # #     controls=[],  # Start with an empty control list
    # # )
    # update_appbar(page)
    # page.add(side_bar)
    # page.update()
