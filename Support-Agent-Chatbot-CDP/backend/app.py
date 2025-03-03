from flask import Flask, request, jsonify
from query_processor import process_query
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question", "")
    response = process_query(question)
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True)
