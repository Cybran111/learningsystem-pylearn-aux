# coding=utf-8
import zipfile
from flask import Flask, request
import requests

app = Flask(__name__)

CODE_DICT = {
    1: "print('привіт, світ')",
    2: "a=float(input())"
    "b=float(input())"
    "if a<b:"
    "    print('<')"
    "elif a>b:"
    "    print('>')"
    "else:"
    "    print('=')",
    3: "word=input()"
    "for letter in word"
    "    print(letter)"

}

@app.route('/<int:assign_id>', methods=['GET', 'POST'])
def first(assign_id):
    if request.method == 'POST':
        print "Request: ", request
        print "Form: ", request.form
        print "Files: ", request.files
        archive = zipfile.ZipFile(request.files.get("solution"))
        code = CODE_DICT[assign_id]
        print code
        step = (100.0 / len(code))
        mark = 0.0
        with archive.open("learn.py") as solution:
            for s in code:
                sol = solution.read(1)

                if s == sol:
                    mark += step
                print s
                print sol
                print mark

        req = requests.post(request.form["url"], data={"mark": 100 if mark > 99.9 else int(mark)})
    return ''

if __name__ == '__main__':
    app.run(debug=True)
