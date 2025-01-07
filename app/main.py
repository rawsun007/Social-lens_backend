from flask import Flask
from flask_cors import CORS
from app.routes import app_routes

app = Flask(__name__)
CORS(app)  # Enable CORS

# Register routes
app.register_blueprint(app_routes)

if __name__ == "__main__":
    print("Starting Flask application...")
    app.run(debug=True, host="0.0.0.0", port=5000)
