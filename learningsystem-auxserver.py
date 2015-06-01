# coding=utf-8
import zipfile
from flask import Flask, request
import requests

app = Flask(__name__)

CODE_DICT = {
    1: "print('привіт, світ')",
    2: """\
a=float(input())
b=float(input())
if a<b:
    print('<')
elif a>b:
    print('>')
else:
    print('=')""",

    3: """\
word=input()
for letter in word
    print(letter)"""

}

@app.route('/<int:assign_id>', methods=['GET', 'POST'])
def first(assign_id):
    if request.method == 'POST':
        print "Request: ", request
        print "Form: ", request.form
        print "Files: ", request.files
        archive = zipfile.ZipFile(request.files.get("solution"))
        mark = 0.0
        code = CODE_DICT[assign_id].split()
        step = (100.0 / len(code))

        with archive.open("learn.py") as solution:
            sol = solution.read().split()
            print sol

            for c, s in zip(code, sol):
                if c == s:
                    mark += step

        req = requests.post(request.form["url"], data={"mark": 100 if mark > 99.9 else int(mark)})
    return ''

if __name__ == '__main__':
    app.run(debug=True)
