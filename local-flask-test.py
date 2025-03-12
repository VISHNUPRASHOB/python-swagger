# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 01:36:29 2025

@author: vishnuprashob
"""

from flask import Flask, jsonify, request
from flasgger import Swagger
from waitress import serve

app = Flask(__name__)

# Swagger Configuration 
app.config['SWAGGER'] = {
    'title': 'Simple Flask API with Swagger',
    'uiversion': 3
}
swagger = Swagger(app)


@app.route('/hello', methods=['GET'])
def hello_world():
    """
    A simple hello world endpoint.
    ---
    responses:
      200:
        description: A successful response
        examples:
          greeting: "Hello, World!"
    """
    return jsonify({"greeting": "Hello, World!"})


@app.route('/add', methods=['GET'])
def add_numbers():
    """
    Add two numbers.
    ---
    parameters:
      - name: a
        in: query
        type: integer
        required: true
        description: First number
      - name: b
        in: query
        type: integer
        required: true
        description: Second number
    responses:
      200:
        description: Sum of the numbers
        schema:
          type: object
          properties:
            sum:
              type: integer
              example: 5
    """
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({"sum": a + b})


#if __name__ == "__main__":
   
#    app.run(host="127.0.0.1", port=8080, debug=True, use_reloader=False, threaded=True)
if __name__ == '__main__':
    serve(app, host="127.0.0.1", port=8081)
