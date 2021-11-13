import datetime
import pymysql
from models import db, Message
from flask import Flask, render_template, redirect, request, jsonify
import json


app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

@app.route("/", methods=["GET", "POST"])
def message():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        data = json.loads(request.get_data().decode('utf8')).get("data")
        now = datetime.datetime.utcnow()
        koreaTime = now + datetime.timedelta(hours=9)
        _message = Message(content=data, created_at=koreaTime.strftime('%Y-%m-%d %H:%M:%S'))
        db.session.add(_message)
        db.session.commit()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)