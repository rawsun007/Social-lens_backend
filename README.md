
# Backend - Social Lens

This repository contains the backend for the Social Lens project, designed to handle API requests, data processing, and AI-powered insights for social media performance analytics.

## Features

- RESTful APIs to fetch and process social media engagement data.
- Integration with **DataStax Astra DB** for scalable data storage and retrieval.
- AI-driven insights using **Gemini** (powered by GPT) for advanced analytics.
- Workflow automation with **Langflow**.
- Built with **Flask** for lightweight and robust API development.

## Tech Stack

- **Flask** - Python framework for creating RESTful APIs.
- **DataStax Astra DB** - For managing engagement data.
- **Langflow** - For automating workflows and AI integration.
- **Gemini** - GPT-based AI for generating insights and powering the chatbot.

## Installation and Deployment

Run the following commands step by step to set up and run the backend server:

```bash
# Clone the repository
git clone https://github.com/yourusername/backend-repo.git
cd backend-repo

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create the environment file
echo "FLASK_APP=app.py
FLASK_ENV=development
ASTRA_DB_ID=your-astradb-id
ASTRA_DB_REGION=your-astradb-region
ASTRA_DB_KEYSPACE=your-keyspace
ASTRA_DB_APPLICATION_TOKEN=your-app-token
GEMINI_API_KEY=your-gemini-api-key" > .env

# Start the Flask server
flask run
