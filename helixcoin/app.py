import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from files_needed import block
from files_needed import transactions
import postman 

app = Flask(__name__)
blockchain = block.Block()

@app.route('/new-transactions', methods=['POST'])
def new_transactions(sender, recipient, amount):
    transaction = transactions.Transaction.new(sender, recipient, amount)
    block.Block.new_transaction(transaction)
    return " " 
@app.route('/time-stamp', methods=['POST'])
def time_stamp(sender, recipient):
     time_stamp = timestamp.time_stamp.new(sender, recipient)
     block.Block.time_stamp(timestamp)
     return time_stamp

@app.route('/mine', methods = ['GET'])
def mine():
    return "We'll mine a new block"
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = blockchain.proof_of_work(last_proof)
@app.route('/chain', methods = ['GET'])
def full_chain():
    response = {
        'chain': block.Block,
        'length': len(block.Block)
    }
    return jsonify(response), 200
previous_hash = blockchain.hash(last_block)
block1 = blockchain.new_proof(proof, previous_hash)
response = {
        'message': "New Block Forged",
        'index': block1['index'],
        'transactions': block1['transactions'],
        'proof': block1['proof'],
        'previous_hash': block1['previous_hash'],
    }
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
 
  


    


