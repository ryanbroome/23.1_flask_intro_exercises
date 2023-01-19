from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def greet():
    html = """
        <body>
            <p>
            Welcome
            </p>
        </body>
    """
    return html
@app.route("/welcome/home")
def greet_home():
    html = """
        <body>
            <p>
            Welcome home
            </p>
        </body>
    """
    return html
@app.route("/welcome/back")
def greet_back():
    html = """
        <body>
            <p>
            Welcome back
            </p>
        </body>
    """
    return html

