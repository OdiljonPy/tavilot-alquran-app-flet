import flet as ft

current_language = "uz"

translations = {
    "uz": {
        "back_button_text": "Orqaga qaytish",
        "three_window_moturudiy": "\n   Abu Mansur Matrudiy",
        "al_quron_text": "\n   Ta'vilot Al-Quron",
        'menuscript_text': "\n   Qo'lyozma va sharhlar",
        "studies_text": "\n   Zamonaviy tadqiqotlar",
        "resources_text": "\n   Resurslar: O'quv qo'llanmalari va ilmiy manba'lar",
        "refusal_text": "\n   Mutaassib oqimlarga raddiyalar",
        "abu_mansur_motrudiy": "Abu Mansur Motrudiy"
    },
    "kr": {
        "back_button_text": "Оркага кайтиш",
        "three_window_moturudiy": "\n   Абу Мансур Мотрудий",
        "al_quron_text": "\n   Тавилот Ал-Курон",
        'menuscript_text': "\n   Колйозма ва шархлар",
        "studies_text": "\n   Замонавий тадкикотлар",
        "resources_text": "\n   Ресурслар: Окув колланмалари ва \n   илмий манбалар",
        "refusal_text": "\n   Муттаасиб окимларга раддийалар",
        "abu_mansur_motrudiy": "Абу Мансур Мотрудий"
    }
}

# Initialize text widgets
def initialize_texts(page):
    return {
        "back_button_text": ft.Text(value=translations[current_language]["back_button_text"], color='black'),
        "three_window_moturudiy": ft.Text(value=translations[current_language]["three_window_moturudiy"], size=page.window_width * 0.017, color='white', expand=True),
        "al_quron_text": ft.Text(value=translations[current_language]["al_quron_text"], size=page.window_width * 0.017, color='white', expand=True),
        "menuscript_text": ft.Text(value=translations[current_language]["menuscript_text"], size=page.window_width * 0.017, color='white', expand=True),
        "studies_text": ft.Text(value=translations[current_language]["studies_text"], size=page.window_width * 0.017, color='white', expand=True),
        "resources_text": ft.Text(value=translations[current_language]["resources_text"], size=page.window_width * 0.014, color='white', expand=True),
        "refusal_text": ft.Text(value=translations[current_language]["refusal_text"], size=page.window_width * 0.017, color='white', expand=True),
        "abu_mansur_motrudiy": ft.Text(value=translations[current_language]["abu_mansur_motrudiy"])
    }

# Function to update the UI text
def update_ui(language, page, texts):
    texts["back_button_text"].value = translations[language]["back_button_text"]
    texts["three_window_moturudiy"].value = translations[language]["three_window_moturudiy"]
    texts["al_quron_text"].value = translations[language]["al_quron_text"]
    texts["menuscript_text"].value = translations[language]["menuscript_text"]
    texts["studies_text"].value = translations[language]["studies_text"]
    texts["resources_text"].value = translations[language]["resources_text"]
    texts["refusal_text"].value = translations[language]["refusal_text"]
    texts["abu_mansur_motrudiy"].value = translations[language]["abu_mansur_motrudiy"]

# Popup menu button selection
def language_selected(e, page, texts):
    global current_language
    current_language = e
    update_ui(current_language, page, texts)
