from flask import Flask,render_template
from HNAlgolia import default_news


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

@app.route('/news')
def get_news():
    return '<center><h1>STARTING NEWS</h1></center>'#render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)