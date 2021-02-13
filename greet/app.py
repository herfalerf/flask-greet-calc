from flask import Flask, request

app = Flask(__name__)


# /welcome
# returns "welcome"



@app.route('/welcome')
def welcome():
    return """
    <html>
      <body>
        <h1>welcome</h1>
      </body>
    </html
    """


# /welcome/home
# Returns "welcome home"

@app.route('/welcome/home')
def welcome_home():
    return """
    <html>
      <body>
        <h1>welcome home</h1>
      </body>
    </html
    """

# /welcome/back
# returns "welcome back"

@app.route('/welcome/back')
def welcome_back():
    return """
    <html>
      <body>
        <h1>welcome back</h1>
      </body>
    </html
    """