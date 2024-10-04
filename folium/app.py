import folium as fl
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    )

    m = fl.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")
    fl.GeoJson(political_countries_url).add_to(m)
    m.save("templates/footprint.html")
    return render_template("footprint.html")

@app.route('/alternativo')
def alternativo():
    return render_template("alternative.html")

@app.route('/ejemplo')
def ejemplo():
    return render_template("choropleth.html")

if __name__ == '__main__':
    app.run()