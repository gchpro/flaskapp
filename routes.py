from flask import Flask, render_template, redirect,url_for
from md import MD
import config
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']
md = MD(config.MDCONFIG)
toolbar = DebugToolbarExtension(app)

@app.route('/')
def home():
    pagenum = 1
    res = md.get_page(pagenum)
    return render_template('page.html', **{'postlist':res['page'], 'page':pagenum,'length':res['len']})


@app.route('/page/<pagenum>')
def show_page(pagenum):
    pagenum = int(pagenum)
    res = md.get_page(pagenum)
    return render_template('page.html', **{'postlist':res['page'], 'page':pagenum,'length':res['len']})

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<filename>')
def show_post(filename):
    post = md.find(filename)
    if post:
        return render_template('post.html',**{'post':post})

    else:
        redirect(url_for('/404'))

@app.route('/admin')
def admin():
    pass


@app.route('/flush')
def flush():
    md.flush()
    return redirect(url_for('home'))

@app.route('/tags/<tagname>')
def tags(tagname):
    return tagname
     

@app.route('/404')
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
