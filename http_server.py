import flask_restful
from flask import Flask,Response
from src.respond import resp
from src.mod import mod
app = Flask(__name__)
app.register_blueprint(mod)
flask_restful.abort = resp.new_abort
if __name__ == "__main__":
    app.run(host='127.0.0.1',port = 5000,debug=True)