import re
import binascii
import flet as ft
from markdownify import markdownify as md


def extract_base64_and_save_images(api_html_response):
    """Process base64 images and save them."""
    expression = r'(data:image/png;base64,[A-Za-z0-9+/=]+)'
    matches = re.findall(expression, api_html_response)

    image_files = []
    parts = []
    last_end = 0

    # Extract base64 images and text
    for index, base64_data in enumerate(matches):
        start = api_html_response.find(base64_data, last_end) - len("data:image/png;base64,")
        end = start + len(base64_data) + len("data:image/png;base64,")

        # Extract text before the image
        if start > last_end:
            text_content = api_html_response[last_end:start].strip()
            result = text_content.rfind("<p")
            parts.append({"type": "text", "content": text_content[:result]})

        try:
            base64_string = base64_data.split(",")[1]
            d = base64_string
            image_files.append(d)
            parts.append({"type": "image", "content": d})
        except binascii.Error:
            parts.append({"type": "text", "content": "[Invalid Image]"})

        last_end = end

    if last_end < len(api_html_response):
        text_content = api_html_response[last_end:].strip()
        index_text = text_content.find('>')
        parts.append({"type": "text", "content": text_content[index_text+1:]})

    return parts, ""


def extract_and_process_videos(api_html_response):
    """Extract video content from HTML response."""
    # Regular expression to match any .mp4 URL
    video_expression = r'https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[\w-]+'

    video_matches = re.findall(video_expression, api_html_response)

    video_files = []
    for video_url in video_matches:
        video_files.append(video_url)
    return video_files


def render_content(container, parts, video_files, page):
    """Render text, images, and videos alternately based on extracted parts."""
    arabic_pattern = r'[\u0600-\u06FF]+'

    video_index = 0  # Track the video index to match video URLs with the actual video components

    for part in parts:
        if part["type"] == "text":
            # Convert HTML content to Markdown
            markdown_content = md(part["content"])

            # Split the content into lines to detect and process Arabic text line by line
            lines = markdown_content.splitlines()
            for line in lines:
                # Check if the line contains a video URL
                video_urls = re.findall(r'https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[\w-]+', line)
                if video_urls:
                    # Render video for each video URL found
                    for video_url in video_urls:
                        if video_index < len(video_files):
                            video_url = video_files[video_index]
                            id_index = video_url.find("=")
                            video_id = video_url[id_index+1:]
                            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/sddefault.jpg"

                            # Function to redirect to YouTube
                            def redirect_to_youtube(e):
                                page.launch_url(video_url)

                            container.controls.append(
                                ft.Stack(
                                    [
                                        ft.Container(
                                            image_src=thumbnail_url,
                                            image_fit=ft.ImageFit.COVER,
                                            width=900,
                                            height=500,
                                            on_click=redirect_to_youtube,
                                            expand=True
                                        ),
                                        ft.Container(
                                            content=ft.Icon(name=ft.icons.PLAY_ARROW, color="white", size=50),
                                            alignment=ft.alignment.center,
                                            bgcolor=ft.colors.BLACK45,
                                            border_radius=ft.border_radius.all(100),
                                            width=100,
                                            height=80,
                                            on_click=redirect_to_youtube
                                        ),
                                    ],
                                    alignment=ft.alignment.center,
                                    # on_click=redirect_to_youtube,  # Redirect on click
                                )
                            )
                            video_index += 1

                else:
                    # Render non-video content as text
                    if re.search(arabic_pattern, line):
                        # Render Arabic text with a custom font using ft.Text
                        container.controls.append(
                            ft.Text(line, style=ft.TextStyle(font_family='Amiri'), text_align=ft.TextAlign.CENTER,
                                    size=20)
                        )
                    else:
                        # Render non-Arabic content as Markdown
                        if line.strip():
                            container.controls.append(ft.Markdown(f"# {line}"))

        elif part["type"] == "image":
            # Directly render base64 images using ft.Image(src_base64=)
            base64_image = part["content"]
            container.controls.append(ft.Image(src_base64=base64_image, width=900, height=400, expand=True))

    # Update the container to reflect changes
    container.update()


def render_description(data, page):
    arabic_pattern = r'[\u0600-\u06FF]+'
    markdown_content = md(data)
    data_list = []

    # Split the content into lines to detect and process Arabic text line by line
    lines = markdown_content.splitlines()
    for line in lines:
        # Render non-video content as text
        if re.search(arabic_pattern, line):
            # Render Arabic text with a custom font using ft.Text
            data_list.append(
                ft.Text(line, style=ft.TextStyle(font_family='Amiri'), text_align=ft.TextAlign.CENTER, size=20,
                        expand=True,
                        width=page.window.width, rtl=True)
            )
        else:
            # Render non-Arabic content as Markdown
            if line.strip():
                data_list.append(ft.Markdown(f"## {line}"))
    container = ft.Container(margin=30, content=ft.Column(controls=data_list, horizontal_alignment=ft.CrossAxisAlignment.CENTER), alignment=ft.alignment.center, adaptive=True, width=page.window.width)
    return container

