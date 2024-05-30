from flask import Flask, request, render_template, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

# List of words with clues for the game
word_list = [
    {"word": "python", "clue": "A popular programming language"},
    {"word": "flask", "clue": "A lightweight WSGI web application framework"},
    {"word": "hangman", "clue": "The name of this game"},
    {"word": "challenge", "clue": "A task or problem that tests a person's abilities"},
    {"word": "programming", "clue": "The process of writing computer software"},
    {"word": "developer", "clue": "A person who creates software"}
]


def choose_word():
    return random.choice(word_list)


def initialize_game():
    word_info = choose_word()
    return {
        'word': word_info['word'],
        'clue': word_info['clue'],
        'guessed': ['_'] * len(word_info['word']),
        'attempts': 6,
        'guessed_letters': []
    }


@app.route("/")
def index():
    if 'game' not in session:
        session['game'] = initialize_game()
    return render_template("index.html", game=session['game'])


@app.route("/guess", methods=["POST"])
def guess():
    letter = request.form.get("letter").lower()
    game = session['game']

    if letter in game['guessed_letters']:
        return redirect(url_for("index"))

    game['guessed_letters'].append(letter)

    if letter in game['word']:
        for idx, char in enumerate(game['word']):
            if char == letter:
                game['guessed'][idx] = letter
    else:
        game['attempts'] -= 1

    if '_' not in game['guessed']:
        game['status'] = 'win'
    elif game['attempts'] <= 0:
        game['status'] = 'lose'

    session['game'] = game
    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    session.pop('game', None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)