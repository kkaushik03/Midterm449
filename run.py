'''
run.py
The main entry point for running the Flask application.
Initializes the app, registers routes, and starts the web server.
Ensures all configurations and dependencies are properly loaded before execution.
'''
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)