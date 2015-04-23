# from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page. <a href='/hello'>Take me to hello.</a>"

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label>
                <label>Compliment:
                    <input type="radio" name="compliment" value="awesome">Awesome
                    <input type="radio" name="compliment" value="ducky">Ducky
                    <input type="radio" name="compliment" value="wonderful">Wonderful
                    <input type="radio" name="compliment" value="lovely">Lovely
                </label>
                <label>What's the first word that comes to your mind?
                <input type="text" name="firstword">
                </label>
                <label>Favorite color(s):
                    <input type="checkbox" name="color" value="purple">Purple
                    <input type="checkbox" name="color" value="teal">Teal
                    <input type="checkbox" name="color" value="sunflower">Sunflower
                    <input type="checkbox" name="color" value="orange">Orange
                </label>
                <input type="submit">
            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")
    compliment = request.args.get("compliment")
    first_word = request.args.get("firstword")
    colors = request.args.getlist("color")
    print colors
    print type(colors)

    color_str = " and ".join(colors)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s! And I know you really like %s %s!
        </body>
    </html>""" % (player, compliment, color_str, first_word)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
