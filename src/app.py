from flask import Flask, jsonify, request
# from solution import Sudoku

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World"

@app.route('/healthcheck', methods = ['GET'])
def healthcheck():
    return 'Server up and running', 200

@app.route('/sudoku', methods = ['POST'])
def sudoku_solution():
    from solution import Sudoku
    request_data = request.get_json()
    user_sudoku = Sudoku(request_data["table"])
    return jsonify({'table' : user_sudoku.solvesudoku()})

app.run(port=5000)


    
