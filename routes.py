from flask import Flask, render_template, redirect,url_for
from md import MD
import config

app = Flask(__name__)
md = MD(config.CONFIG)

@app.route('/')
def home():
	allpost = md.findall()[0:5]
	return render_template('home.html',**{'postlist':allpost})

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

@app.route('/404')
@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'),404

if __name__ == '__main__':
	app.run(debug=True)