from flask import Flask, render_template
from sqlalchemy import create_engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
app = Flask(__name__)
import json

prcp_data = dict(engine.execute("SELECT date, prcp FROM measurement").fetchall())
station_data = dict(engine.execute("SELECT station, name FROM station").fetchall())

temprature_data = dict(engine.execute("SELECT date, tobs FROM measurement WHERE station='USC00519523' AND date(date)>date('2016-08-23')").fetchall())

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/v1.0/precipitation")
def precipitation():
    return prcp_data

@app.route("/api/v1.0/stations")
def stations():
    return station_data

@app.route("/api/v1.0/tobs")
def tobs():
    return temprature_data


if __name__ == '__main__':
    app.debug = True
    app.run()

