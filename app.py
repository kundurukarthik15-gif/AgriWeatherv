from flask import Flask, request, jsonify

app = Flask(__name__)

# API Key
API_KEY = "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"

# Disease database
disease_solutions = {
    "blight": "Use copper-based fungicides and rotate crops to prevent blight spread.",
    "rust": "Apply sulfur dusting and resistant crop varieties to control rust.",
    "wilt": "Improve soil drainage, use resistant seeds, and apply bio-fungicides.",
    "mosaic": "Remove infected plants and use virus-free seeds."
}

# Middleware: check API key
@app.before_request
def check_api_key():
    if request.endpoint == "get_disease":
        key = request.headers.get("x-api-key")
        if key != API_KEY:
            return jsonify({"error": "Forbidden. Invalid API Key."}), 403

# Endpoint: Get disease solution
@app.route("/api/disease", methods=["GET"])
def get_disease():
    name = request.args.get("name", "").lower()
    if name in disease_solutions:
        return jsonify({"disease": name, "solution": disease_solutions[name]})
    else:
        return jsonify({"error": "Disease not found."}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
