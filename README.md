# AutocorrectProject

## Overview

This project implements an autocorrect system that detects and corrects misspelled words in user input. The program compares each word in a sentence to a dictionary of valid words and replaces incorrect words with the closest match.

The system uses a combination of a **Trie data structure** for efficient word storage and **Levenshtein Edit Distance** to measure similarity between words.

---

## How to Run the Program

### Requirements

* Python 3 installed

### Steps

1. Clone the repository or download the files
2. Make sure `dictionary.txt` is in the same folder as the program
3. Run the program:

```
python main.py
```

4. Enter a sentence when prompted

---

## Input

### Dictionary File

A text file named `dictionary.txt` containing one valid word per line.

Example:

```
computer
science
keyboard
screen
```

### User Input

The user enters a sentence through the console.

Example:

```
I lovv computr sciense
```

---

## Output

The program outputs:

* The original sentence
* The corrected sentence
* A list of corrections (if any)

Example:

```
Original: I lovv computr sciense
Corrected: I love computer science

Suggestions:
lovv → love
computr → computer
sciense → science
```

---

## Algorithm

The program uses **Levenshtein Edit Distance** to determine how similar two words are. This distance represents the minimum number of insertions, deletions, or substitutions required to transform one word into another.

### Steps:

1. Load all dictionary words into a Trie
2. Split user input into individual words
3. For each word:

   * If it exists in the dictionary, keep it
   * Otherwise:

     * Retrieve candidate words using Trie prefix matching
     * Compute edit distance between the input word and each candidate
     * Select the word with the smallest distance
4. Combine corrected words into a sentence and display results

---

## Data Structures Used

* **Trie**

  * Stores dictionary words efficiently
  * Supports fast lookup and prefix-based search

* **List**

  * Stores candidate words and suggestions

* **2D Array**

  * Used in dynamic programming to compute edit distance

---

## Runtime Complexity

Let:

* n = number of words in input
* c = number of candidate words from Trie
* k = average word length

### Time Complexity:

```
O(n × c × k²)
```

* Edit distance takes O(k²)
* Trie reduces the number of comparisons from all dictionary words (m) to a smaller subset (c)

---

## File Structure

```
project/
│── main.py
│── dictionary.py
│── trie.py
│── autocorrect_engine.py
│── input_handler.py
│── dictionary.txt
│── README.md
```

---

## Design Overview

* `Main`
  Controls program flow and handles input/output

* `Dictionary`
  Manages word storage using a Trie

* `Trie`
  Stores words and supports prefix-based search

* `AutocorrectEngine`
  Calculates edit distance and finds best matches

* `InputHandler`
  Reads and processes user input

---

## Testing

The program was tested with multiple sentences including:

* Correctly spelled input
* Misspelled words
* Mixed correct and incorrect words

The program runs without crashing and produces clear, readable output.

---

## Future Improvements

* Add multiple suggestions instead of one
* Use word frequency to improve accuracy
* Support punctuation-aware corrections
* Optimize further using advanced Trie traversal
* Add a graphical user interface (GUI)

---

## Author

Paola Ramos Ortiz
