from flask import Flask, render_template
from datetime import date
import requests
AGE = "agify"
GENDER = "genderize"

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_year = date.today().year
    return render_template('index.html', current_year = current_year)
@app.route('/Guess')
def guess():
    return "Enter the Name in the URL for guessing the gender and Age for the Name!"
@app.route('/Guess/<name>')
def guess_name(name):
    age = requests.get(f"https://api.{AGE}.io/?name={name}")
    gender = requests.get(f"https://api.{GENDER}.io/?name={name}")
    age_data = age.json()['age']
    gender_data = gender.json()['gender']
    return render_template('guessing_age_and_gender.html', name = name, age=age_data, gender=gender_data)

if __name__ == '__main__':
    app.run(debug=True)
