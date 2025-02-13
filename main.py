import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import nltk
from nltk.corpus import words  # Fixed typo

nltk.download("words")

class SpellingChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.text = ScrolledText(self.root, font=('Arial', 14))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()

        self.old_spaces = 0 

        self.root.mainloop()

    def check(self, event):
        content = self.text.get("1.0", tk.END)
        space_count = content.count(" ")

        self.text.tag_remove("misspelled", "1.0", tk.END)  # Remove previous highlights

        if space_count != self.old_spaces:
            self.old_spaces = space_count
            words_list = words.words()  # Get the list of valid words
            
            for word in content.split():
                cleaned_word = re.sub(r"[^\w]", "", word.lower())  # Remove punctuation
                if cleaned_word and cleaned_word not in words_list:
                    start_index = content.find(word)
                    end_index = start_index + len(word)

                    self.text.tag_add("misspelled", f"1.{start_index}", f"1.{end_index}")
                    self.text.tag_config("misspelled", foreground="red")

SpellingChecker()

