from flask import Flask

app = Flask(__name__)


@app.route('/get')
def get_file():
    try:
        with open('data.txt', 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return 'File not found'


@app.route('/get/<name>')
def get_file_by_name(name):
    try:
        with open('src/{filename}'.format(filename=name), 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return 'File not found'


if __name__ == '__main__':
    app.run()
