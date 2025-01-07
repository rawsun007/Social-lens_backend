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
        # Parse JSON request data
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "No message provided"}), 400

        # Extract the message
        message = data["message"]

        # Run Langflow with the provided message
        response = run_flow(message)

        # Debug log the raw response
        print(f"Raw Response from Langflow: {response}")

        # Extract outputs and session_id
        outputs = response.get("outputs", [])
        session_id = response.get("session_id", "No session ID available")

        # Simplify outputs for readability
        if isinstance(outputs, list):
            outputs = [str(output) for output in outputs]  # Convert list items to strings
        elif isinstance(outputs, dict):
            outputs = {key: str(value) for key, value in outputs.items()}  # Simplify dict
        else:
            outputs = str(outputs)  # Fallback for other types

        # Debug log the processed outputs
        print(f"Processed Outputs: {outputs}")

        # Return the processed response
        return jsonify({
            "outputs": outputs,
            "session_id": session_id
        }), 200

    except Exception as e:
        # Log any errors for debugging
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500


@app_routes.route("/", methods=["GET"])
def home():
    """
    Root route for the application.
    """
    return jsonify({"message": "Welcome to the Flask API!"}), 200


@app_routes.route("/favicon.ico", methods=["GET"])
def favicon():
    """
    Return 204 for favicon.ico requests.
    """
    return "", 204  # No Content