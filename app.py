from flask import Flask, render_template, Response, request, redirect, url_for
import watcher
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'arthur'
app.config['BASIC_AUTH_PASSWORD'] = 'arthur'

basic_auth = BasicAuth(app)

@app.route('/')
def index():
    return redirect('/main/')

@app.route('/main/')
@basic_auth.required
def main():
    cacheget=watcher.cache_get()
    return render_template('index.html',cache=cacheget,len=len(cacheget))

@app.route('/watch/')
def watch():
    res=watcher.seek(request.args.get('title'))
    ret=render_template('watch.html',srcs=res,len=len(res))
    return ret

app.run(host='0.0.0.0', port=8800, debug=True)