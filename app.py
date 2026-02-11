# Importing flask class from the flask module like this:
from flask import Flask

# Instance creation of flask class
app = Flask(__name__)

# Route defining and function to handle requests to specific route
@app.route('/')
def main_page():
    return '''
    <h1>Main Page</h1>
    <p>Main Page</p>
    <a href="/working"><button>This works?</button></a>
    '''

@app.route('/working')
def this_works():
    return '''
    <h1>This works</h1>
    <p>This is a test button, hopefully</p>
    <a href="/"><button>This should send you somewhere!</button></a>
    '''
    
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
