from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    if request.args:
        try:
            thai_word = data[request.args['word']]
        except KeyError:
            thai_word=['Такого слова нет в словаре']
        return render_template('index.html', thai_word=thai_word)
    return render_template('index.html', thai_word= ["Здесь появится перевод!"])


if __name__ == '__main__':
    with open('/Users/gaurwaithmelui/PycharmProjects/english_thai_dict/english_to_thai.json') as data_file:
        data = json.load(data_file)
    app.run()
