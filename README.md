# AutocorrectProject

## How to Run
1. Place dictionary.txt in the same folder
2. Run:
   python main.py

## Input
- Dictionary file: one word per line
- User enters a sentence

## Output
- Displays original and corrected sentence

## Algorithm
The program uses Levenshtein Edit Distance to compare each input word with all dictionary words.
The word with the minimum edit distance is selected as the correction. The Trie is used for efficient word storage and lookup. Currently, all words are retrieved for comparison, but the structure allows future optimization using prefix filtering.

## Complexity
O(n × m × k²)
Where:
n = number of words in input
m = number of words in dictionary
k = average word length
