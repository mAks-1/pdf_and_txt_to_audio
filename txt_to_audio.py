from gtts import gTTS


def txt_to_audio(filename, output_mp3):
    with open(filename, 'r') as f:
        mytext = f.read()

    language = 'en'
    tts = gTTS(text=mytext, lang=language, slow=False)
    tts.save(output_mp3)
    print(f"Audio file '{output_mp3}' created.")