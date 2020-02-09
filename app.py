# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/products", methods=["GET", "PUT", "DELETE", "POST"])
def req():
  if request.method == 'GET':
    return jsonify({ 'message': 'Get a Product' })
  if request.method == 'PUT':
    return jsonify({ 'message': 'Put a Product' })
  if request.method == 'DELETE':
    return jsonify({ 'message': 'Delete a Product' })
  if request.method == 'POST':
    return jsonify({ 'message': 'Post a new product' })

@app.route("/products/<product_id>", methods=["GET"])
def get_one_product(product_id):
  return jsonify({ 'message': 'GET one product: '+product_id+' -- '+ request.args.get('teste') })

if(__name__ == '__main__'):
    app.run(debug=True)