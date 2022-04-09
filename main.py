from flask import Flask
from flask_restx import Resource, Api
from crolling import update, data_name

app = Flask(__name__)
api = Api(app)


@api.route('/air/<string:sido>/<string:item>/<int:hour>')
class Air_by_hour(Resource):
    def get(self, sido, item, hour):

        tmps = update(sido, item)

        result = {}
        for tmp in tmps:
            result[tmp[0]] = tmp[hour+3]

        return result

@api.route('/air/<string:sido>/<string:item>/<int:hour>/<string:loc>')


@api.route('/air/<string:sido>/<string:item>')
class Air_all(Resource):
    def get(self, sido, item):
        tmps = update(sido, item)
        result = {}
        for tmp in tmps:
            semi_result = {}
            cnt = 0
            for data in data_name:
                semi_result[data] = tmp[cnt]
                cnt += 1

            result[tmp[0]] = semi_result


        return result


if __name__ == "__main__":
    app.run(debug=True)
