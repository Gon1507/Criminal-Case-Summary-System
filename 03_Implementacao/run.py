import os
from final_report_app.final_report import create_app

# Create the Flask application with the required configuration
app = create_app()

if __name__ == "__main__":
    # Debug mode is off by default; enable it with FLASK_DEBUG=1 for local development
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=5000, debug=debug)
