from flask import Blueprint
from flask_restful import Api
from .mod import NewRes

mod = Blueprint('mod', __name__)
resource = Api(mod)
resource.add_resource(NewRes, "/shopee/test")