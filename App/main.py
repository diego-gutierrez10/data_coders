import folium
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/<ser>')
def home():
    return render_template(".html")

@app.route('/software')
def software():
    return render_template("software.html")

if __name__ == '__main__':
    app.run()