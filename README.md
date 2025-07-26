
# 🕹️ Hangman Game in Python

This is a simple **Hangman** game implemented in Python. It's a classic word-guessing game where a player tries to guess a hidden word by suggesting letters, within a certain number of attempts.

## 📌 Features

- Command-line based interface.
- Word randomly selected from a predefined list.
- Tracks used letters and number of remaining attempts.
- Displays visual progress with underscores for hidden letters.
- Ends with a win or lose message.

## 🚀 How to Run

1. **Clone the repository** (if not already):

    ```bash
    git clone https://github.com/NvnNeha/hangman_python.git
    cd hangman_python
    ```

2. **Run the game:**

    ```bash
    python main.py
    ```

    > Make sure you have Python 3 installed on your system.

## 🧠 Game Rules

- You will be shown a word with hidden letters represented by underscores (`_`).
- You must guess one letter at a time.
- If the letter exists in the word, it will be revealed in all its positions.
- If not, your remaining chances decrease.
- The game ends when:
  - You guess the whole word correctly ✅
  - You run out of chances ❌

## 🎮 Example

Welcome to Hangman!
You have 6 lives.
Word: _ _ _ _ _ _

Guess a letter: e
Correct!

Word: _ _ e _ _ _

Guess a letter: a
Wrong! You have 5 lives left.

...

You guessed the word: secret
🎉 You win!


## 🔧 Customization

You can customize the word list by:
- Editing the list inside the Python file.
- Or using an external file like `words.txt` and loading it using Python's `open()` function.

## 📚 Concepts Used

- Python basics: functions, loops, conditionals
- String manipulation
- Lists and sets
- Input/output handling
- Random module for word selection

## ✅ Requirements

- Python 3.x
- No external libraries needed

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).

## 🙌 Author

Developed by **[Naveen Saini](https://github.com/NvnNeha)**

---

Enjoy the game! 🎉
