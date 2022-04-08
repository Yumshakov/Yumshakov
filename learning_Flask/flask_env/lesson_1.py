from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ['Main', 'page_one', 'page_two']


@app.route('/')
def index():
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='about', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
