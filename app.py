from flask import Flask,render_template,request
from HNAlgolia import default_news,get_news,search_news


app = Flask('Hacker News')

@app.route('/')
def start():
    response=default_news()
    data=response.json()
    return render_template('home.html',data=data)


@app.route('/search',methods=['GET'])
def search():

    keywords=request.args.get('keywords')
    by=request.args.get('by')
    response=search_news(keywords,by)
    data=response.json()
    
    return render_template('search.html',data=data,keywords=keywords,by=by)
    #return 'Keywords: {} | Filter By: {}'.format(keywords,by)


@app.route('/news&id=<id>')
def build_news(id):
    response=get_news(id)
    data=response.json()
    return render_template('news.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)