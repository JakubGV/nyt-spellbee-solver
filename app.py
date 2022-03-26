import os
from flask import Flask, request, jsonify
from spelling_bee_solver import SpellingBeeSolver

app = Flask(__name__)
solver = SpellingBeeSolver('word_list.txt')

@app.route("/solve", methods=['GET'])
def solve():
    letters = request.args['letters']
    if letters is not None:
        try:
            return jsonify(solver.solve(letters)) 
        except ValueError as err:
            return "Invalid input", 400
    else:
        return "Invalid input", 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))