# coding=utf-8
import zipfile
from flask import Flask, request
import requests

app = Flask(__name__)

CODE_DICT = {
    1: u"print('привіт, світ')",
    2: u"a=float(input())"
    u"b=float(input())"
    u"if a<b:"
    u"    print('<')"
    u"elif a>b:"
    u"    print('>')"
    u"else:"
    u"    print('=')",
    3: u"word=input()"
    u"for letter in word"
    u"    print(letter)"

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
        step = 1.0 / len(code)
        mark = 0.0
        with archive.open("learn.py") as solution:
            for s in code:
                sol = solution.read(1)
                print s
                print sol
                print mark
                print

                if s == sol:
                    mark += step
                    print mark
        req = requests.post(request.form["url"], data={"mark": int(mark)})
    return ''

if __name__ == '__main__':
    app.run(debug=True)
