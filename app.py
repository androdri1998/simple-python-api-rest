# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def get_product():
  return jsonify({ 'message': 'Get a Product' })

@app.route("/products", methods=["PUT"])
def put_product():
  return jsonify({ 'message': 'Put a Product' })

@app.route("/products", methods=["DELETE"])
def delete_product():
  return jsonify({ 'message': 'Delete a Product' })

@app.route("/products", methods=["POST"])
def post_product():
  return jsonify({ 'message': 'Post a new product' })

@app.route("/products/<product_id>", methods=["GET"])
def get_one_product(product_id):
  return jsonify({ 'message': 'GET one product: '+product_id+' -- '+ request.args.get('teste') })

if(__name__ == '__main__'):
    app.run(debug=True)