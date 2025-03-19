from flask import Flask, render_template, request
import post
app = Flask(__name__)

@app.route('/blogs/<name>')
def blogs(name):
    posts = post.set_data()
    return render_template('index.html', name=name, posts=posts)

@app.route('/post')
def show_post():
    title = request.args.get('title')
    body = request.args.get('body')
    return render_template('post.html', title=title, body=body)


if __name__ == '__main__':
    app.run(debug=True)