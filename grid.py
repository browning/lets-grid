from flask import Flask
from flask import render_template, make_response, request, redirect, url_for, flash
import grid_data

app = Flask(__name__)
app.secret_key = 'blablablabla'

@app.route("/")
def main():
    response = make_response(render_template('main.html'))
    response.headers['Content-Security-Policy'] =  "img-src 'self'; frame-src 'self'; media-src 'self'"
    return response

@app.route("/create")
def create():
    response = make_response(render_template('grid.html'))
    response.headers['Content-Security-Policy'] =  "img-src 'self'; frame-src 'self'; media-src 'self'"
    return response

@app.route("/save_grid", methods=["POST"])
def save_grid():
    js_code = request.form['codearea']
    app_id = grid_data.save_grid(js_code)
    flash('Copy the URL in the url bar to share your creation with friends')
    return redirect(url_for('show_grid', grid_id=app_id))

@app.route("/grid/<grid_id>")
def show_grid(grid_id):
    js_data = grid_data.load_grid(grid_id)
    response = make_response(render_template('grid.html', usrjs=js_data))
    response.headers['Content-Security-Policy'] =  "img-src 'self'; frame-src 'self'; media-src 'self'"
    return response

@app.route("/tutorials")
def tutorials_list():
    response = make_response(render_template('tutorials.html'))
    response.headers['Content-Security-Policy'] =  "img-src 'self'; frame-src 'self'; media-src 'self'"
    return response

@app.route("/tutorials/<tutorial_name>")
def show_tutorial(tutorial_name):
    if tutorial_name == "basics":
        response = make_response(render_template('basics_tutorial.html'))
    elif tutorial_name == "variables":
        response = make_response(render_template('variables_tutorial.html'))
    elif tutorial_name == "functions":
        response = make_response(render_template('functions_tutorial.html'))
    elif tutorial_name == "if-statements":
        response = make_response(render_template('if_tutorial.html'))
    elif tutorial_name == "loops":
        response = make_response(render_template('loops_tutorial.html'))
    elif tutorial_name == "advanced":
        response = make_response(render_template('advanced_tutorial.html'))
    elif tutorial_name == "resources":
        response = make_response(render_template('resources_tutorial.html'))
    response.headers['Content-Security-Policy'] =  "img-src 'self'; frame-src 'self'; media-src 'self'"
    return response



if __name__ == "__main__":
    app.run(debug=True)