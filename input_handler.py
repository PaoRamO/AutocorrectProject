import re


class InputHandler:
    def read_line(self):
        return input("Enter a sentence: ")

    def parse_words(self, sentence):
        # removes punctuation and splits cleanly
        return re.findall(r"\b\w+\b", sentence)