from flask import Flask
from flask_cors import CORS
from app.routes import app_routes
import os  # To access environment variables

app = Flask(__name__)
CORS(app)  # Enable CORS

# Register routes
app.register_blueprint(app_routes)

if __name__ == "__main__":
    print("Starting Flask application...")
    
    # Use the PORT environment variable if defined; default to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
