class AutocorrectEngine:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def calculate_edit_distance(self, w1, w2):
        len1, len2 = len(w1), len(w2)

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if w1[i - 1] == w2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # delete
                        dp[i][j - 1],      # insert
                        dp[i - 1][j - 1]   # replace
                    )

        return dp[len1][len2]

    def find_best_match(self, word):
        candidates = self.dictionary.get_candidates(word)

        best_match = None
        min_distance = float("inf")

        for dict_word in candidates:
            # small optimization
            if abs(len(word) - len(dict_word)) > 2:
                continue

            distance = self.calculate_edit_distance(word.lower(), dict_word)

            if distance < min_distance:
                min_distance = distance
                best_match = dict_word

        return best_match