from flask import Flask, render_template, Response, request, redirect, url_for
import watcher

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/main/')

@app.route('/main/')
def main():
    cacheget=watcher.cache_get()
    return render_template('index.html',cache=cacheget,len=len(cacheget))

@app.route('/watch/')
def watch():
    res=watcher.seek(request.args.get('title'))
    ret=render_template('watch.html',srcs=res,len=len(res))
    return ret

app.run(host='0.0.0.0', port=8800, debug=True)