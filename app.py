from flask_cors import CORS
import os
import sqlalchemy
import pandas as pd
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
CORS(app)

engine = create_engine("sqlite:///trip.db")

# @app.route("/")
# def index():
#     """Return the homepage."""
#     return render_template("index.html")

@app.route('/priorwkdata')
def jundata():
    df=pd.read_sql("SELECT * FROM priorwkdata",engine)
    data=df.to_json()
    return data 



@app.route('/pridedata')
def pridedata():
    length = request.args.get('length', None)
    df=pd.read_sql_query(f"SELECT * FROM pridedata limit {length}",engine)
    data=df.to_json(orient="records")
    return  {'results': json.loads(data)}

if __name__ =='__main__':
    app.run(debug=True,threaded=True)