import datetime as dt
from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('users', methods=['GET'])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"], "timestamp": dt.datetime.utcnow().isoformat()})
