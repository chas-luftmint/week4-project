# Importing flask class from the flask module like this:
from flask import Flask

# Instance creation of flask class
app = Flask(__name__)

# Route defining and function to handle requests to specific route
@app.route('/')
def this_works():
    return 'This works! Wow!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
