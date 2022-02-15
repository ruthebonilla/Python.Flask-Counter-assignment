from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= "cookies"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/counting')
def counting():
    if 'submit' not in session:
        session['submit'] = 0
    else:
        session['submit'] += 1
    return redirect("/")


@app.route('/cleared')
def cleared():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)


