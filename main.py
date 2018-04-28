from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import cgi

###
#	Prototype of redirect() function is as below −
#	Flask.redirect(location, statuscode, response)
#	In the above function −
#	location parameter is the URL where response should be redirected.
#	statuscode sent to browser’s header, defaults to 302.
#	response parameter is used to instantiate response.
###
app = Flask(__name__)
app.config['DEBUG'] = True
# Note: the connection string after :// contains the following info:
# user:password@server:portNumber/databaseName
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:ablog@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(120))
    blog_body  = db.Column(db.Text())
    posted     = db.Column(db.Boolean)

    def __init__(self,blog_title, blog_body, posted):
        self.blog_title= blog_title
        self.blog_body= blog_body
        self.posted = False

def valid_title(title):
	title_message=[]
	if len(title)>0:
		return True
	else:
		title_error="The title can not be empty.Enter a title for your new-post"
		return  False
def valid_body(body):
	if len(body)>0:
		return True
	return  False

##		Initilisation of the error_message to empty list:[] no error
error_message=[]		#error_message=[error_title, error_body]
##		error_title=error_message[0]
##		error_body=error_message[1]

@app.route('/blog', methods=['GET'])
def index():
	# variable blog_id for requesting id from database
	blog_id = request.args.get('id')
	# If request is true grab blog using id and render template that returns single blog post
	if blog_id:
		blogs = Blog.query.get(blog_id)
		btitle=blogs.blog_title
		bbody=blogs.blog_body
		return render_template('displayentry.html', btitle=btitle, bbody=bbody)

		#Render page that holds all blogs
	return render_template('showall.html', blogs=Blog.query.order_by(Blog.id.desc()).all())

@app.route('/newpost', methods=['POST','GET'])
def newpost():
	##		Initilisation of the error_message to empty list:[] no error
	error_message=[]		#error_message=[error_title, error_body]
	##						error_title=error_message[0]
	##						error_body=error_message[1]
#	if request.method=="GET":
#		return render_template("blog.html", title_error="", body_error="")
	if request.method=="POST":
		blog_title=request.form["blog_title"]
		blog_body=request.form["blog_body"]

		# Collection of the eventuel error in error massage

		if len(blog_title)>0:
			title_error=""
			error_message.append(title_error)
		elif len(blog_title)==0:
			title_error="Enter a title for your post"
			error_message.append(title_error)
		if len(blog_body)>0:
			body_error=""
			error_message.append(body_error)
		elif len(blog_body)==0:
			body_error="The body of your blog cannot be empty. Enter something!"
			error_message.append(body_error)

		if len(blog_title)>0 and len(blog_body)>0:			# No error in the filling the newpost's form
			# Create an object of the class Blog
			new_blog=Blog(blog_title, blog_body, posted=True) # composants of the blog
			db.session.add(new_blog) # add new blog to the database
			db.session.commit()      # confirmation of adding the new post to the database
			# allpost.append(new_blog) # adding the new blog to the list
			# Redirect to individual blog post using current blog's information, id is automatically
			return redirect('/blog?id='+str(new_blog.id))
		else:
			return render_template('newpost.html', title_error=error_message[0], body_error=error_message[1])
	else:
		return render_template('newpost.html')


if __name__ == '__main__':
   app.run()
