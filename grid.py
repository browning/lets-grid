from flask import Flask
from flask import render_template, make_response
app = Flask(__name__)

@app.route("/")
def main():
    response = make_response(render_template('grid.html'))
    response.headers['Content-Security-Policy'] =  "default-src: 'none'; script-src: 'self';"
    return response

if __name__ == "__main__":
    app.run(debug=True)