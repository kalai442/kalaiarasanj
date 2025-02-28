from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chatbot_response():
    query = request.json.get("query", "").strip()
    if not query:
        return jsonify({"response": "Please provide a valid query."})
    return jsonify({"response": f"Mock response for: {query}"})

if __name__ == "__main__":
    app.run(debug=True)