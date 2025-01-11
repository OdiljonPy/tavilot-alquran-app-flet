import re
import binascii
import requests
import os
import pyhtml2md
import flet as ft
import pymupdf
from PIL import Image
from io import BytesIO
import base64


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
            parts.append({"type": "text", "content": text_content})

        try:
            base64_string = base64_data.split(",")[1]
            image_data = base64.b64decode(base64_string, validate=True)

            image_filename = os.path.join(os.getcwd(), f"output_image_{index}.png")
            with open(image_filename, "wb") as image_file:
                image_file.write(image_data)

            image_files.append(image_filename)
            parts.append({"type": "image", "content": image_filename})
        except binascii.Error:
            parts.append({"type": "text", "content": "[Invalid Image]"})

        last_end = end

    if last_end < len(api_html_response):
        text_content = api_html_response[last_end:].strip()
        parts.append({"type": "text", "content": text_content})

    return parts, "Images processed and saved."


def extract_and_process_videos(api_html_response):
    """Extract video content from HTML response."""
    # Regular expression to match any .mp4 URL
    video_expression = r'https?://[^"]+\.mp4'

    video_matches = re.findall(video_expression, api_html_response)

    video_files = []
    for video_url in video_matches:
        video_files.append(video_url)

    print(video_files)  # For debugging, to check the extracted video URLs

    return video_files


def render_content(container, parts, video_files):
    """Render text, images, and videos alternately based on extracted parts."""
    arabic_pattern = r'[\u0600-\u06FF]+'

    video_index = 0  # Track the video index to match video URLs with the actual video components

    for part in parts:
        if part["type"] == "text":
            # Convert HTML content to Markdown
            markdown_content = pyhtml2md.convert(part["content"])

            # Split the content into lines to detect and process Arabic text line by line
            lines = markdown_content.splitlines()
            for line in lines:
                # Check if the line contains a video URL
                video_urls = re.findall(r'https?://[^"]+\.mp4', line)
                if video_urls:
                    # Render video for each video URL found
                    for video_url in video_urls:
                        if video_index < len(video_files):
                            container.controls.append(ft.Video(
                                playlist=[
                                    ft.VideoMedia(
                                        resource=video_files[video_index]
                                    )
                                ],
                                playlist_mode=ft.PlaylistMode.LOOP,
                                fill_color=ft.colors.LIGHT_BLUE,
                                volume=100,
                                autoplay=False,
                                muted=False,
                                show_controls=True,
                                expand=True,
                                width=400,
                                height=400
                            ))
                            video_index += 1
                else:
                    # Render non-video content as text
                    if re.search(arabic_pattern, line):
                        # Render Arabic text with a custom font using ft.Text
                        container.controls.append(
                            ft.Text(line, style=ft.TextStyle(font_family='Amiri'), text_align=ft.TextAlign.CENTER, size=20)
                        )
                    else:
                        # Render non-Arabic content as Markdown
                        if line.strip():
                            container.controls.append(ft.Markdown(line))

        elif part["type"] == "image":
            # Directly render base64 images using ft.Image(src_base64=)
            with open(part["content"], "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode("utf-8")
                container.controls.append(ft.Image(src_base64=base64_image, width=800, height=600, expand=True))

    # Update the container to reflect changes
    container.update()