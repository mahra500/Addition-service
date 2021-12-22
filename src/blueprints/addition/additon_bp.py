from flask import Flask, request
from flask.blueprints import Blueprint

app = Flask(__name__)
addition_bp = Blueprint('addition_bp',__name__)

@addition_bp.route('/addition', methods = ['GET'])
def add():
    print(request.args.get('number_1'))
    if not (request.args.get('number_1') and request.args.get('number_2')):
        print(request.args.get('number_1'))
        return 'Please provide two numbers for addition'
    elif not (request.args.get('number_1').isdigit() and request.args.get('number_2').isdigit()):        
        return 'Please enter integers for addition'
    else:
        return str(int(request.args.get('number_1')) + int(request.args.get('number_2')))