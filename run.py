from flask import Flask,render_template,jsonify
from ds18b20 import read_temp
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/temp')
def get_data():
    temp = read_temp()
    return jsonify({"value": temp, "name": '室温'})

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
