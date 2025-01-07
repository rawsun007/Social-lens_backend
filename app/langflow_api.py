import json
import requests
from typing import Optional

from dotenv import load_dotenv
import os

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Langflow API settings
BASE_API_URL = os.getenv("BASE_API_URL")
LANGFLOW_ID = os.getenv("LANGFLOW_ID")
FLOW_ID = os.getenv("FLOW_ID")
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")
SECRET_KEY = os.getenv("SECRET_KEY")


def run_flow(
    message: str,
    endpoint: str = FLOW_ID,
    output_type: str = "chat",
    input_type: str = "chat",
    tweaks: Optional[dict] = None,
    application_token: Optional[str] = APPLICATION_TOKEN,
) -> dict:
    try:
        api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
        payload = {
            "input_value": message,
            "output_type": output_type,
            "input_type": input_type,
        }
        if tweaks:
            payload["tweaks"] = tweaks
        headers = {"Authorization": f"Bearer {application_token}", "Content-Type": "application/json"}

        print(f"Sending request to Langflow API with payload: {payload}")  # Debug log
        response = requests.post(api_url, json=payload, headers=headers)
        print(f"Langflow API Response: {response.json()}")  # Debug log
        return response.json()
    except Exception as e:
        print(f"Error occurred in run_flow: {e}")
        return {"error": str(e)}
