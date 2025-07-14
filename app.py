from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route
@app.route("/")
def hello():
    return "Hello, Flask CI/CD!"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
