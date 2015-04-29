from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        print request.files
        print request.data
        print request.form
        print request
        req = requests.post(request.form["url"], data={"mark": 100})
        print req
        with open('fail.html', 'w') as file_:
            file_.write(req.content)

    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
