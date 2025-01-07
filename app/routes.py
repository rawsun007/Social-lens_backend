from flask import Blueprint, request, jsonify
from app.langflow_api import run_flow

app_routes = Blueprint("app_routes", __name__)

@app_routes.route("/chat/analyze", methods=["POST"])
def chat_analyze():
    """
    Endpoint for chat-based analysis using Langflow.
    """
    print("POST request received at /chat/analyze")  # Debug log
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "No message provided"}), 400

        # Run Langflow with the provided message
        message = data["message"]
        response = run_flow(message)

        # Extract outputs and session_id if available
        outputs = response.get("outputs", "No outputs available")
        session_id = response.get("session_id", "No session ID available")

        print(f"Langflow Outputs: {outputs}")  # Debug log
        print(f"Session ID: {session_id}")    # Debug log

        return jsonify({
            "outputs": outputs,
            "session_id": session_id
        }), 200
    except Exception as e:
        print(f"Error occurred: {e}")  # Debug log
        return jsonify({"error": str(e)}), 500


@app_routes.route("/", methods=["GET"])
def home():
    """
    Root route for the application.
    """
    return jsonify({"message": "Welcome to the Flask API!"}), 200


@app_routes.route("/favicon.ico", methods=["GET"])
def favicon():
    return "", 204  # No Content
