"""
Text To Speech
-------------------------------------------------------------
pip install nltk newspaper3k gtts
"""

import pyttsx3  # https://pypi.org/project/pyttsx3/

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def text_to_speech_ui():
    def open_file():
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not filepath:
            return

        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"TextToSpeech - {filepath}")

    def save_file():
        filepath = asksaveasfilename(
            defaultextension="mp3",
            filetypes=[("Audio Files", "*.mp3"), ("All Files", "*.*")],
        )

        if not filepath:
            return

        text = txt_edit.get(1.0, tk.END)
        text_to_speech(text, filepath, chosen_voice.get())

    window = tk.Tk()
    window.title("TextToSpeech")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(window)
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="TextToSpeech", command=save_file)

    # Create the list of options
    voices_list = ["Man", "Woman"]

    # Variable to keep track of the option
    # selected in OptionMenu
    chosen_voice = tk.StringVar(window)

    # Set the default value of the variable
    chosen_voice.set("Select a voice")
    # Create the optionmenu widget and passing
    # the options_list and value_inside to it.
    question_menu = tk.OptionMenu(fr_buttons, chosen_voice, *voices_list)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    question_menu.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()


def text_to_speech(text, filepath, chosen_voice):
    engine = pyttsx3.init()

    """ RATE"""
    rate = engine.getProperty("rate")  # getting details of current speaking rate
    # print (rate)                        #printing current voice rate
    engine.setProperty("rate", 180)  # setting up new voice rate

    """VOICE"""
    voices = engine.getProperty("voices")  # getting details of current voice
    if chosen_voice == "Man":
        engine.setProperty(
            "voice", voices[0].id
        )  # changing index, changes voices. o for male
    else:
        engine.setProperty(
            "voice", voices[1].id
        )  # changing index, changes voices. 1 for female

    engine.save_to_file(text, filepath)
    engine.runAndWait()


if __name__ == "__main__":
    text_to_speech_ui()
