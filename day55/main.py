from flask import Flask

app = Flask(__name__)

def make_emphasis_decorator(func):
    def wrapper(**kwargs):
        return f"<em>{func(kwargs['name'])}</em>"
    return wrapper
def make_bold(func):
    def wrapper(*args):
        print(args)
        return f"<strong>{func(*args)}</strong>"
    return wrapper
@app.route('/<name>')
@make_emphasis_decorator
@make_bold
def say_hello(name):
    return f"Hello {name}!"

if __name__ == '__main__':
    app.run(debug=True)