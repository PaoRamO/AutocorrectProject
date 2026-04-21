from dictionary import Dictionary
from autocorrect_engine import AutocorrectEngine
from input_handler import InputHandler


def main():
    dictionary = Dictionary()
    dictionary.load_from_file("dictionary.txt")

    engine = AutocorrectEngine(dictionary)
    input_handler = InputHandler()

    sentence = input_handler.read_line()
    words = input_handler.parse_words(sentence)

    corrected_words = []
    suggestions = []

    for word in words:
        if dictionary.contains(word):
            corrected_words.append(word)
        else:
            best_match = engine.find_best_match(word)

            if best_match:
                corrected_words.append(best_match)
                suggestions.append(f"{word} → {best_match}")
            else:
                corrected_words.append(word)

    print("\nOriginal:", sentence)
    print("Corrected:", " ".join(corrected_words))

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print(s)


if __name__ == "__main__":
    main()