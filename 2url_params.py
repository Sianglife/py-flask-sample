from flask import Flask

app = Flask(__name__)


@app.route('/input/<name>')
def queryInput(name):
    return """<div>Input: {name}</div>""".format(name=name)


if __name__ == '__main__':
    app.run()
