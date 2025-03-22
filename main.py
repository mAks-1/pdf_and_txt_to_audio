import os

from pdf_to_audio import pdf_to_audio
from txt_to_audio import txt_to_audio


def main():
    print('Hello. You can convert .txt and .pdf files into audio\n')
    filename = input('Write the name of the file you want to convert: ')
    if os.path.isfile(filename):
        if filename.endswith('.pdf'):
            output_mp3 = input("Enter the name of the output MP3 file (e.g., 'output.mp3'): ")
            pdf_to_audio(filename, output_mp3)
        elif filename.endswith('.txt'):
            output_mp3 = input("Enter the name of the output MP3 file (e.g., 'output.mp3'): ")
            txt_to_audio(filename, output_mp3)
        else:
            print("Only .txt or .pdf files")
    else:
        print(f"File '{filename}' not found.")

main()
