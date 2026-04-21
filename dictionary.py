from trie import Trie


class Dictionary:
    def __init__(self):
        self.trie = Trie()

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                self.add_word(line.strip().lower())

    def add_word(self, word):
        self.trie.insert(word)

    def contains(self, word):
        return self.trie.search(word.lower())

    def get_candidates(self, word):
        # Use prefix filtering (IMPORTANT: this is where Trie is USED)
        prefix = word[:2].lower()  # first 2 letters
        candidates = self.trie.get_words_with_prefix(prefix)

        # fallback if no matches
        if not candidates:
            candidates = self.trie.get_all_words()

        return candidates