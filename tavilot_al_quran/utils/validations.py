# Function to limit input length to 9 digits
def limit_length(phone_input, page):
    if len(phone_input.value) > 9:
        phone_input.value = phone_input.value[:9]
        page.update()
