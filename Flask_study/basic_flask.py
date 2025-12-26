from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return '<h1 style="text-align: center">Hello, Flask!</h1>'\
        '<p> this is the paragraph </p>'\
        '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2I4Mzd4MnluZHB5OTNrcjIxcDJyaHBrOTE3d3VvdWE1YTZ6MGcwayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PBAZlGgKo67DFgJ78x/giphy.gif" width=500>'
def make_bold(func):
    def wrapper():
        return f"<b>{func()}<b>"
    return wrapper
def make_italic(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper
def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route("/speed")
def speed():
    return "Speed Calculator"

@app.route("/<name>")
def greet(name):
    return "Hello, " + name

@app.route("/Test")
@make_underline
@make_italic
@make_bold
def test():
    return "Hello, World! "


if __name__ == "__main__":
    app.run(debug = True)

