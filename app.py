from flask import Flask, render_template, Response, request, redirect, url_for
import watcher

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/main/')

@app.route('/main/')
def main():
    return render_template('index.html')

@app.route('/watch/')
def watch():
    res=watcher.seek(request.args.get('title'))
    ret=render_template('watch.html',srcs=res,len=len(res))
    return ret

app.run(debug=True)