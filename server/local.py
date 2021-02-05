from flask import Flask, send_file,jsonify

from server.routes.io.file import file

app = Flask(__name__)
app.register_blueprint(file, url_prefix="/api/io/file")


@app.route('/')
def api():
    return {
        "version": '1.2.3',
    }


@app.route('/favicon.ico')
def favicon():
    return send_file('./assets/favicon.ico', 'image/x-icon')


if __name__ == '__main__':
    app.run('127.0.0.1', '7000')
