import flask_restful
from flask import Flask,Response
from src.respond import resp
from src.mod import mod
app = Flask(__name__)
app.register_blueprint(mod)
flask_restful.abort = resp.new_abort
@app.errorhandler(404)
def error_404(error):
    return resp.response(code = resp.SYSTEM_ERR)
if __name__ == "__main__":
    app.run(host='127.0.0.1',port = 5000,debug=True)
