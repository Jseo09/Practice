from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(1, 10)
print(random_number)

@app.route("/")
def home():
    return '<h1 style="text-align: center">Hello, Flask!</h1>'\
        '<h2 style="text-align:center; color=green;" > Welcome to Number guessing Game. Please Guess the number and go to that url </h2>'\
        '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWFkODlqYTN1cnlwY3A5dTM3dzd1dGE4dGsxNXc4emg4b3ZoZzdhMyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xUn3CftPBajoflzROU/giphy.webp" width=500>'

def up_down_game(func):
    def wrapper(**kwargs):

        if int(kwargs['number']) < random_number:
            result = '<br><br> <h1><b> TOO LOW! </b></h1> <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDRwM25oMG1vY29waDN0dzl1NHFkaWdnNGxjcmF3MWx4b3I2cjdvdyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LQ7WlVv55hPifs0Pme/giphy.webp" width=500>'
            function = func(**kwargs)
            return function + result
        elif int(kwargs['number']) > random_number:
            function = func(**kwargs)
            result = '<br><br><h1> Too High! </h1> <img src= "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDd5M3l4YmZ2cW4zZ2ltemUxcmlwbmJ2ZTF0bWRucG9kbzllMTViaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/s1MX7LfOn5nhTyb0dy/giphy.webp" width=500>'
            return function + result
        else:
            result = f'<br><br><h1> Yes! The number {kwargs['number']} was correct!</h1> <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTcycG5oMzBsa2ZnM3VmOXhqZGNmdDYzdWk0NGxzcjZncXQ2NnMydSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26tknCqiJrBQG6bxC/200.webp" width=500>'
            function = func(**kwargs)
            return function + result
    return wrapper

@app.route("/<number>")
@up_down_game
def number(number : int):
    return f'You have guessed number {number}'


if __name__ == "__main__":
    app.run(debug = True)

