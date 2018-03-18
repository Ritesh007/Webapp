from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('404.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__=='__main__':
   app.run(debug=True)
   #print (app.url_map)