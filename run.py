"""
Flask application
https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
"""

from app import create_app, Flask

if __name__ == "__main__":
    app: Flask = create_app()
    app.run()
