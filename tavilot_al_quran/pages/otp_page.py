import flet as ft

# Create six text fields
text_fields = [ft.TextField(width=50, text_align=ft.TextAlign.CENTER) for _ in range(6)]


# Function to automatically move focus to next or previous field
def on_change(e):
    # Get the current field index
    current_index = text_fields.index(e.control)
    # If the input is a number and the field has more than one digit, clear extra digits
    if e.control.value.isdigit() and len(e.control.value) > 1:
        e.control.value = e.control.value[0]  # Keep only the first digit
        e.control.update()
    # If the input is a number and the field has exactly one digit, move to the next field
    if e.control.value.isdigit() and len(e.control.value) == 1:
        next_field_index = current_index + 1
        if next_field_index < len(text_fields):
            text_fields[next_field_index].focus()
    # If the input is cleared, move to the previous field
    elif e.control.value == "":
        prev_field_index = current_index - 1
        if prev_field_index >= 0:
            text_fields[prev_field_index].focus()


# Function to collect all numbers into one variable
def collect_otp():
    otp = "".join(field.value for field in text_fields if field.value.isdigit())
    print(f"Collected OTP: {otp}")
    return otp


# Attach the on_change event to each text field
for text_field in text_fields:
    text_field.on_change = on_change
# Add text fields to a row to display them in a horizontal line
row = ft.Row(adaptive=True, controls=text_fields)


# ------------------------------------------------------------------------------------------------------------------------


def otp_verify(key_otp):
    url = "https://alquran.zerodev.uz/api/v1/auth/verify/"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        'otp_code': collect_otp,
        'otp_key': key_otp
    }
    print(data)
    response = requests.post(url=url, json=data, headers=headers)
    print(response)


def go_to_otp_page(page):
    page.clean()
    page.add(ft.Container(
        adaptive=True,
        content=ft.Row(
            adaptive=True,
            controls=[
                ft.Column(
                    adaptive=True,
                    controls=[
                        ft.Text(value="  TA'VILOT \nAL-QURON \n", color=TC, style="displayLarge"),
                        ft.Text(value=f"Parol ushbu raqamga jonatildi \n+998{phone_input.value}", width=400,
                                weight='bold',
                                style="titleLarge"),
                        row,
                        ft.Text(),
                        ft.OutlinedButton(
                            text="Davom etish",
                            on_click=otp_verify(otp_key),
                            # Link the button to validation
                            width=400,
                            height=60,
                            style=ft.ButtonStyle(
                                color='white',
                                bgcolor=TC,
                                shape=ft.RoundedRectangleBorder(radius=8),
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(
                    content=ft.Image(
                        src=os.path.abspath("assets/tavilot_book.png"),
                        width=700,
                        height=900,
                        fit=ft.ImageFit.COVER,
                        border_radius=100
                    ),
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  # Enable anti-aliasing for smoother edges
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,  # Spread content and image to left and right
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,  # Center the entire row in the middle of the page
        expand=True,  # Make the container expand to fill the page
    ))
