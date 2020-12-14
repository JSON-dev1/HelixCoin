import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from dataclasses import *

app = Flask(__name__)

@app.route('/mine', methods = ['GET'])
def mine():
    return "We'll mine a new block"
@app.route('/transactions/new', methods = ['POST'])
def new_transactions():
    return "We'll add a new transaction"
@app.route('/chain', methods = ['GET'])
def full_chain():
    response = {
        'chain': block.Block,
        'length': len(block.Block)
    }
    return jsonify(response), 200
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)








    


