class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def _collect_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)

        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)

    def get_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        words = []
        self._collect_words(node, prefix, words)
        return words

    def get_all_words(self):
        return self.get_words_with_prefix("")