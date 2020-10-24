from flask import Flask, render_template, request, redirect, url_for, flash
import covid19_data

app = Flask(__name__)


@app.route('/')
def index():
    covid_total = covid19_data.jsonByName("Total")
    
    return render_template('index.html', data = covid_total)

if __name__ == "__main__":
    app.run(debug=False)
