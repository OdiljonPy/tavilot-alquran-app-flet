import requests
import flet as ft
from .html_pdf_handler import extract_base64_and_save_images, extract_and_process_videos, render_content

def about_us_page(page, back_button):
    TC = '#E9BE5F'
    page.clean()
    page.scroll = False
    # Show a loading indicator
    loading = ft.ProgressRing(color=TC)
    page.add(ft.Container(
        expand=True,
        adaptive=True,
        content=loading,
        alignment=ft.alignment.center)
    )
    page.update()

    # API call to fetch the "about" page data
    url = "http://176.221.28.202:8008/api/v1/about/"
    response = requests.get(url=url)

    if response.status_code == 200:
        data = response.json().get("result", {}).get("description", "")
        api_html_response = data

        # Process HTML to handle base64 images and videos
        parts, result = extract_base64_and_save_images(api_html_response)
        video_files = extract_and_process_videos(api_html_response)

        # Clear the page content after the data is loaded
        page.clean()
        page.scroll = True

        # Container to hold the rendered content
        content_container = ft.Container(
            margin=40,
            content=ft.Column(
                controls=[
                    ft.Text(result, text_align=ft.TextAlign.CENTER, size=30),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            expand=True
        )
        page.add(content_container,

                 ft.Video(
                     playlist=[
                         ft.VideoMedia(
                             resource='https://rr2---sn-01oxu-u5ns.googlevideo.com/videoplayback?expire=1737135783&ei=R0KKZ7b0Os_Rv_IP8dqY8QM&ip=195.158.24.249&id=o-AP1nlx6GExEcaZZYAQu5DCB67bi9YTxmcq-5vQkEAip5&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1737114183%2C&mh=_K&mm=31%2C29&mn=sn-01oxu-u5ns%2Csn-4g5lznlz&ms=au%2Crdu&mv=m&mvi=2&pl=20&rms=au%2Cau&initcwndbps=1188750&bui=AY2Et-MzoCP6PCfa_F8ZTtShVCla1hJ4bZaXq0eYE3orVnb7R4eXeE3Tu5pwrcSMTI4ok2lhLXYAk4cE&vprv=1&svpuc=1&mime=video%2Fmp4&ns=WAgqWmWMQ5jpeVgF1dZecE4Q&rqh=1&cnr=14&ratebypass=yes&dur=294.452&lmt=1736282173480390&mt=1737113831&fvip=4&lmw=1&fexp=51326932%2C51335594%2C51353498%2C51371294%2C51384461&c=TVHTML5&sefc=1&txp=5319224&n=9q4vq7SpxbO65w&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIgQH6bu3MMbqWNH8oFH6iP_jBkhBq-8bpYgU5e0Et8Uq4CIQCv4j0ujNx9ouMs8UxGZ0fe1voyfp05JY7lI4KovINRbA%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=AGluJ3MwRAIgKKi8-TdMIFmPiNIgQxsf-310moOQIZe4S0ZmjXUNY_cCIBfF9DXTBJXmz3u9iPuV7p67trxAikZxrqNIphzMdVYI'
                         )
                     ],
                     playlist_mode=ft.PlaylistMode.LOOP,
                     fill_color=ft.colors.BLACK,
                     volume=100,
                     autoplay=False,
                     muted=False,
                     show_controls=True,
                     expand=True,
                     width=800,
                     height=600
                 )

                 )

        # Render the extracted parts (text, images, videos)
        render_content(content_container.content, parts, video_files, page)

    else:
        # Show an error message if the API call fails
        page.clean()
        error_message = ft.Text("Failed to load content.", text_align=ft.TextAlign.CENTER)
        page.add(ft.Container(
            content=error_message,
            alignment=ft.alignment.center,
            expand=True
        ))

    page.update()
