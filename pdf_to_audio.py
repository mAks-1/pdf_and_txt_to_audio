from PyPDF2 import PdfReader


def pdf_to_audio(filename, output_mp3):
    reader = PdfReader(filename)

    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text
        full_text = full_text.replace(',', '').replace('\n', ' ')

    if full_text.strip():
        language = 'en'
        tts = gTTS(text=full_text, lang=language, slow=False)
        tts.save(output_mp3)
        print(f"Audio file '{output_mp3}' created.")
    else:
        print(f"Not found any text in '{filename}'.")