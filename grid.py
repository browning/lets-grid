from flask import Flask
from flask import render_template, make_response, request
import grid_data

app = Flask(__name__)

@app.route("/")
def main():
    response = make_response(render_template('grid.html'))
    response.headers['Content-Security-Policy'] =  "default-src: 'none'; script-src: 'self';"
    return response

@app.route("/save_grid", methods=["POST"])
def save_grid():
	js_code = request.form['codearea']
	app_id = grid_data.save_grid(js_code)
	return app_id

if __name__ == "__main__":
    app.run(debug=True)