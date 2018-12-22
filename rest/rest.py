from flask import Flask
from flask import jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful import Resource, Api

# initialize Flask
app = Flask(__name__)
api = Api(app)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["24000 per day", "1000 per hour"]
)


class Ping(Resource):
    """oof"""

    @limiter.exempt
    def get(self):
        return jsonify("hure")


# add resources
api.add_resource(Ping, '/ping')

# start the web service
if __name__ == '__main__':
    app.run(port=1337)
