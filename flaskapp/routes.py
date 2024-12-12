from flaskapp import app
from flask import render_template, session, redirect, url_for

@app.route('/')
def home():
    return "Benvenuto nella tua app Flask!"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard', active='dashboard')

@app.route('/graph')
def graph():
    return render_template('graph.html', title='Graph', active='graph')

# logout
@app.route("/logout")
def logout():
  session.pop('logged_in', None)
  return redirect(url_for('login'))