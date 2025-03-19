from flask import Flask, render_template, request
import email_manager

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_mail():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    email_manager.EmailManager(name, email, subject, message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
































