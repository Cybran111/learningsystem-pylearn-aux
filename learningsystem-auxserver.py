import zipfile
from flask import Flask, request
from nltk.corpus import stopwords
import requests
import nltk

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        archive = zipfile.ZipFile(request.files.get("solution"))
        with archive.open("extra.txt") as solution:
            languages_ratios = {}
            tokens = nltk.wordpunct_tokenize(solution.read().decode('utf-8'))
            words_set = set([word.lower() for word in tokens])
            for language in stopwords.fileids():
                stopwords_set = set(stopwords.words(language))
                common_elements = words_set.intersection(stopwords_set)
                if common_elements:
                    languages_ratios[language] = len(common_elements)

            # 50%
            mark = (float(languages_ratios['english']) / sum(languages_ratios.values())) * 50

            # 50%
            words_count = len(words_set)
            mark += (words_count / 200) * 50 if words_count < 200 else 50

        req = requests.post(request.form["url"], data={"mark": int(mark)})

    return ''

if __name__ == '__main__':
    app.run(debug=True)
