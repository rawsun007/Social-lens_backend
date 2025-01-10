from flask import Flask
from flask_cors import CORS
from app.routes import app_routes
import os  # To access environment variables

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes and origins (adjust this in production for security)
CORS(app, resources={r"/*": {"origins": "*"}})

# Register application routes
app.register_blueprint(app_routes)

if __name__ == "__main__":
    print("Starting Flask application...")
    
    # Use the PORT environment variable if defined, default to 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Run the Flask app
    app.run(debug=True, host="0.0.0.0", port=port)
