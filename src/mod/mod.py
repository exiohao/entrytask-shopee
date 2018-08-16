from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from src.respond import resp

parser = RequestParser()
parser.add_argument("a", type=int, location="args", required=True,help = 'a must be int')
parser.add_argument("b", type=str, location="args", required=True,help = 'b must be a str')

class NewRes(Resource):
    def get(self):
        req = parser.parse_args(strict=True)
        a = req.get("a")
        b = req.get("b")
        res_data = b+' : '+str(a) 
        return resp.response(code = resp.SUCCESS,data=res_data)