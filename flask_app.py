from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def guess_answer(max, min):
    """A binary search algorithm

    :return: a guessed number
    :rtype: int
    """
    return (max - min) // 2 + min


@app.route("/")
def hello_world():
    """Simple redirect."""
    return redirect("welcome")


@app.route("/welcome", methods=["GET", "POST"])
def welcome_screen():
    """Displays welcome message.
    The OK button redirects user to 'game' page.
    """
    if request.method == "POST":
        return redirect("game")
    else:
        return render_template("welcome_screen.html")


@app.route("/game", methods=["GET", "POST"])
def game():
    """Apps main function"""
    if request.method == "POST":
        max = int(request.form["max"])
        min = int(request.form["min"])
        attempts = int(request.form["attempts"]) + 1
        guess = guess_answer(max, min)
        user_input = request.form["button"]
        if user_input == "too_much":
            max = guess
            guess = guess_answer(max, min)
            return render_template("game.html", max=max, min=min, attempts=attempts, guess=guess)
        elif user_input == "too_little":
            min = guess
            guess = guess_answer(max, min)
            return render_template("game.html", max=max, min=min, attempts=attempts, guess=guess)
        elif user_input == "guessed":
            attempts = int(request.form["attempts"])
            return redirect(url_for("game_over", attempts=attempts))
    else:
        return render_template("game.html", max=1000, min=0, attempts=1, guess=500)


@app.route("/game_over", methods=["GET", "POST"])
def game_over():
    """End game message.
    Button restarts the game.
    """
    if request.method == "POST":
        return redirect("/welcome")
    else:
        attempts = int(request.args.get("attempts"))
        return render_template("game_over.html", attempts=attempts)


if __name__ == '__main__':
    app.run()
