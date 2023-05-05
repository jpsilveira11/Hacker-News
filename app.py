from flask import Flask

app = Flask('Hacker News')

@app.route('/')
def start():
    return '<h1><center>working!</center></h1>'

if __name__ == '__main__':
    app.run()