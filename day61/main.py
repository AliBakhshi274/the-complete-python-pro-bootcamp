from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from forms import LoginForm
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
Bootstrap(app)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.name.data}!', 'success')
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['password'] = form.password.data
        return redirect(url_for('success', form=form))
    return render_template('login.html', form=form)

@app.route("/success", methods=['GET', 'POST'])
def success():
    email = session.get('email')
    name = session.get('name')
    password = session.get('password')
    return render_template('success.html', email=email, name=name, password=password)

if __name__ == '__main__':
    app.run(debug=True)
