# from flask import Flask, jsonify, request
#
#
# app = Flask(__name__)
#
#
# testing_types = [
#     {'name': 'unit testing', 'description': 'testing individual units of a source code'}
# ]
#
#
# @app.route('/tests')
# def get_test_types():
#     return jsonify(testing_types)
#
#
# @app.route('/tests', methods=['POST'])
# def add_test_type():
#     testing_types.append(request.get_json())
#     return "SuccessFully Added Type", 204
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
