from flask import Flask, request, redirect, render_template
from waitress import serve
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

share_url = ''


@app.route('/', methods=['GET'])
def index_get():
    return share_url


@app.route('/', methods=['POST'])
def index_post():
    global share_url
    share_url = request.data.decode('utf-8')

    return {
        "success": True
    }


@app.route('/redirect', methods=['GET'])
def redirect_handler():
    return redirect(share_url)


@app.route('/ui')
def ui():
    return render_template('index.html')


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)
