# Simple main.py for gunicorn web server
from web.app import app

# This is for gunicorn to import the app
# The app is created in web/app.py

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)