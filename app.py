from flask import Flask,render_template
from HNAlgolia import default_news,get_news


app = Flask('Hacker News')

@app.route('/')
def start():
    response=default_news()
    data=response.json()
    return render_template('home.html',data=data)

'''
@app.route('/search')
def search():
    return render_template('search.html')
    '''

@app.route('/news&id=<id>')
def build_news(id):
    response=get_news(id)
    data=response.json()
    return render_template('news.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)