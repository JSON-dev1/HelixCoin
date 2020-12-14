import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask
from dataclasses import *

app = Flask(__name__)

@app.route ('/mine', methods = ['GET'])
def mine():
    return "We'll mine a new block"






    


