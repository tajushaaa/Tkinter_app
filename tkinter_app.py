from constants.text_of_this import THIS_TEXT
import tkinter
import customtkinter
import random
# hii
from classes.button_app import FileModification

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Tkinter App by Taya :)")
facts = ["The average person will spend 6 months of their life waiting for red lights to turn green.",
         "The world's largest snowflake on record was 15 inches wide and 8 inches thick.",
         "The shortest war in recorded history lasted only 38 minutes between Britain and Zanzibar on 27 August "
         "1896.",
         "The word 'nerd' was first coined by Dr. Seuss in his book 'If I Ran the Zoo'.",
         "The first recorded game of baseball was played in 1846 in Hoboken, New Jersey."]


def print_this_text():
    return THIS_TEXT


def get_content():
    entry_words.get()


def find_words_in_file():
    value = entry_words.get()
    words = FileModification().find_words(value)
    words = ", ".join(words)
    textbox.insert("1.0", text=words)


def clear_box():
    textbox.delete(1.0, 'end')


def enter_press(event=None):
    find_words_in_file()


def get_fun_fact():
    index = random.randint(0, len(facts) - 1)
    textbox.insert("1.0", text=facts[index])


def dropdown_action(choice):
    choice = option_menu_choose.get()
    if choice == "Print 'Zen of Python'":
        textbox.insert("1.0", text=print_this_text())
    elif choice == "Clear":
        clear_box()
    elif choice == "Show me a fun fact of the day":
        get_fun_fact()


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_word_finder = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Word Finder")
label_word_finder.pack(pady=10, padx=10)
entry_words = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter up to 3 letters")
button_find_words = customtkinter.CTkButton(master=frame_1, text="Find words", command=find_words_in_file)
entry_words.pack(pady=10, padx=10)
button_find_words.pack(pady=10, padx=10)
option_menu_choose = customtkinter.CTkOptionMenu(frame_1,
                                                 values=["Print 'Zen of Python'", "Clear",
                                                         "Show me a fun fact of the day"], command=dropdown_action)
textbox = customtkinter.CTkTextbox(master=frame_1, width=200)
option_menu_choose.pack(pady=10, padx=10)
option_menu_choose.set("Choose")
app.bind("<Return>", enter_press)
textbox.pack(padx=10, pady=10)
textbox.insert("1.0", text="")
app.mainloop()
