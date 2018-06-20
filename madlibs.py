"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

MADLIB_TEMPLATES = ["ml_school.html", "madlib.html",
]



@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Shows madlib form"""

    response = request.args.get("yn")

    if response == "yes":

        return render_template("game.html")

    else:

        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """ Shows madlib with user input"""
    person = request.args.get("person")
    color = request.args.get("color")
    noun1 = request.args.get("noun1")
    noun2 = request.args.get("noun2")
    noun3 = request.args.get("noun3")
    noun4 = request.args.get("noun4")
    noun5 = request.args.get("noun5")
    adjectives = request.args.getlist("adjective")
    adjective1 = request.args.get("adjective1")
    adjective2 = request.args.get("adjective2")
    adjective3 = request.args.get("adjective3")
    adjective4 = request.args.get("adjective4")
    adjective5 = request.args.get("adjective5")
    propernoun1 = request.args.get("propernoun1")
    propernoun2 = request.args.get("propernoun2")
    pluralnoun1 = request.args.get("pluralnoun1")
    pluralnoun2 = request.args.get("pluralnoun2")
    celebrity1 = request.args.get("celebrity1")
    celebrity2 = request.args.get("celebrity2")
    liquid1 = request.args.get("liquid1")
    liquid2 = request.args.get("liquid2")
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    num3 = request.args.get("num3")
    num4 = request.args.get("num4")
    num5 = request.args.get("num5")
    superad1 = request.args.get("superad1")
    superad2 = request.args.get("superad2")
    superad3 = request.args.get("superad3")
    adverb1 = request.args.get("adverb1")
    adverb2 = request.args.get("adverb2")
    adverb3 = request.args.get("adverb3")
    adverb4 = request.args.get("adverb4")
    adverb5 = request.args.get("adverb5")

    chosen_madlib = choice(MADLIB_TEMPLATES)

    return render_template(chosen_madlib,
                           person=person,
                           color=color,
                           adjectives=adjectives,
                           noun1=noun1,
                           noun2=noun2,
                           noun3=noun3,
                           noun4=noun4,
                           noun5=noun5,
                           adjective1=adjective1,
                           adjective2=adjective2,
                           adjective3=adjective3,
                           adjective4=adjective4,
                           adjective5=adjective5,
                           propernoun1=propernoun1,
                           propernoun2=propernoun2,
                           pluralnoun1=pluralnoun1,
                           pluralnoun2=pluralnoun2,
                           celebrity1=celebrity1,
                           celebrity2=celebrity2,
                           liquid1=liquid1,
                           liquid2=liquid2,
                           num1=num1,
                           num2=num2,
                           num3=num3,
                           num4=num4,
                           num5=num5,
                           superad1=superad1,
                           superad2=superad2,
                           superad3=superad3,
                           adverb1=adverb1,
                           adverb2=adverb2,
                           adverb3=adverb3,
                           adverb4=adverb4,
                           adverb5=adverb5,)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
