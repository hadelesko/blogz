		#post_id=db.session.query(Blog).order_by(Blog.id.desc()).first()
		#@app.route('/')
		#def displayentry():
		#	post_id=db.session.query(Blog).order_by(Blog.id.desc()).first()
		#	blog_title = request.args.get(blog_title)
		#	blog_body  = request.args.get(blog_body)
		#	return render_template('displayentry.html',blog_title=blog_title, blog_body=blog_title, id=post_id)
		#
		#@app.route('/blog')
		#def showallpost():
		#	post_id=db.session.query(Blog).order_by(Blog.id.desc()).first()
		#	id=str(post_id.id)
		#	#return redirect('/blog?id='+build-a-blg.id) 
		#	blogs = Blog.query.all()
		#	posted_blog = Blog.query.filter_by(posted=True).all()
		#	idpost=Blog.query.filter(id).all()
		#	return render_template("entryshow.html",blogs=blogs )
		##@app.route('/blog')
		##def displayposts():
		##	form_id = request.args.get(id)
		
		#if __name__ == '__main__':
		#    app.run()
		#
		#from flask import Flask, request, redirect, render_template, url_for
		#from flask_sqlalchemy import SQLAlchemy
		#import cgi
		#
		####
		##	Prototype of redirect() function is as below −
		##	Flask.redirect(location, statuscode, response)
		##	In the above function −
		##	location parameter is the URL where response should be redirected.
		##	statuscode sent to browser’s header, defaults to 302.
		##	response parameter is used to instantiate response.
		####
		#app = Flask(__name__)
		#app.config['DEBUG'] = True
		## Note: the connection string after :// contains the following info:
		## user:password@server:portNumber/databaseName
		#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:ablog@localhost:3306/build-a-blog'
		#app.config['SQLALCHEMY_ECHO'] = True
		#db = SQLAlchemy(app)
		#
		#class Blog(db.Model):
		#
		#    id = db.Column(db.Integer, primary_key=True)
		#    blog_title = db.Column(db.String(120))
		#    blog_body  = db.Column(db.String(300))
		#    posted     = db.Column(db.Boolean)
		#
		#    def __init__(self,blog_title, blog_body, posted):
		#        self.blog_title= blog_title
		#        self.blog_body= blog_body
		#        self.posted = False
		#        
		#def valid_title(title):
		#	title_message=[]
		#	if len(title)>0:
		#		return True	
		#	else:
		#		title_error="The title can not be empty.Enter a title for your new-post"
		#		return  False
		#def valid_body(body):	
		#	if len(body)>0:
		#		return True
		#	return  False
		####
		##@app.route('/newpost')
		##def entry():
		##	return render_template('blog.html',title_error ="", body_error  ="")
		#
		#allpost=[] 
		#errtitle_message=[]
		#errbody_message=[]
		#ids=[]
		##@app.route('/newpost')
		##def index():
		##	
		##	return render_template("blog.html",title_error="",body_error="")
		#
		#@app.route('/newpost', methods=['POST', 'GET'])
		#def newpost():
		#	if request.method == 'GET':
		#		return render_template("blog.html",title_error="",body_error="")
		#	elif request.method == 'POST':
		#		blog_title = request.form['blog_title']
		#		blog_body=request.form['blog_body']
		#		if len(blog_title)>0:	#if valid _title(blog_title):
		#			title_error=""
		#			errtitle_message.append(title_error)
		#		else:
		#			title_error="The title can not be empty.Enter a title for your new-post"
		#			errtitle_message.append(title_error)
		#		if len(blog_body)>0: #valid_body(blog_body):
		#			body_error=""
		#			errbody_message.append(body_error)
		#		else:
		#			body_error="The body of your blog cannot be empty. Enter something!"
		#			errbody_message.append(body_error)
		#
		#		if len(blog_title)<0 or len(blog_body)<0:
		#			return render_template("blog.html",title_error=errtitle_message[0],body_error=errbody_message[0])
		#		else:
		#			# Create an object of the class Blog 
		#			new_blog=Blog(blog_title, blog_body, posted=True) # composants of the blog
		#			db.session.add(new_blog) # add new blog to the database
		#			db.session.commit()      # confirmation of adding the new post to the database
		#			allpost.append(new_blog) # adding the new blog to the list
		#			return redirect('/blog?id='+str(new_blog.id))
		#post_id=db.session.query(Blog).order_by(Blog.id.desc()).first()
		#@app.route('/')
		#def displayentry(id):
		#	post_id=db.session.query(Blog).order_by(Blog.id.desc()).first()
		#	blog_title = request.args.get(blog_title)
		#	blog_body  = request.args.get(blog_body)
		#	return render_template('displayentry.html',blog_title=blog_title, blog_body=blog_title, id=post_id)
		#
		#@app.route('/blog')
		#def showallpost():
		#	post_id=db.session.query(Blog).order_by(Blog.id.desc()).first()
		#	id=str(post_id.id)
		#	#return redirect('/blog?id='+build-a-blg.id) 
		#	blogs = Blog.query.all()
		#	posted_blog = Blog.query.filter_by(posted=True).all()
		#	idpost=Blog.query.filter(id).all()
		#	return render_template("entryshow.html",blogs=blogs )
		##@app.route('/blog')
		##def displayposts():
		##	form_id = request.args.get(id)
		#
		#if __name__ == '__main__':
		#    app.run()
		