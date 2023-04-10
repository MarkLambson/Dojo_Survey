from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "dojosurvey"

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/results', methods=["POST"])
def results():
    session['name'] =  request.form["name"]
    session['dojo_location'] = request.form["dojo_location"]
    session['fav_language'] = request.form["fav_language"]
    session['comment'] = request.form["comment"]
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)