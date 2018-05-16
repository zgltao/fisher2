import json

from flask import Flask
from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search/<q>/<page>')
def search():
    """

    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # dict 序列化
    return json.dumps(result), 200, {'conttype':'application/json'}


@app.route('/hello')
def hello():
    return 'hello flask'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8111)
