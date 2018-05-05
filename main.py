from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import cgi

# Note: the connection string after :// contains
app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'danken'

########################################################################
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(120))
    blog_body = db.Column(db.String(120))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, blog_title, blog_body, owner):
        self.blog_title = blog_title
        self.blog_body = blog_body
        self.owner = owner

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    blogs =  db.relationship('Blog', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.password = password
###############################################################################
@app.before_request
def require_login():
	allowed_routes = ['login', 'blog', 'signup', 'index', ]
	if request.endpoint not in allowed_routes and 'username' not in session:
		return redirect('/login')

@app.route('/', methods=['POST', 'GET'])
def index():
		return render_template('index.html',title="Blogz", users=User.query.all())

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		user = User.query.filter_by(username=username).first()
		users= User.query.filter(User.username)
		if user and user.password == password:
			session['username'] = username
			flash("Logged in")
			return redirect('/newpost')
		# loging fails
		
		if len(username)==0 and user.password == password:
			flash("No username given! Errror. Give an your username")
			return render_template('login.html', u_error='Invalid username',p_error='Invalid password')
			#return redirect("/login")
		
		if user and user.password != password:
			flash('User password incorrect error. Give your password')
			return render_template('login.html', u_error='',p_error='Invalid password')
			#return redirect("/login")
		
		if not user:
			flash("This username does not exit")
			return render_template('login.html', u_error='No such username is found, be sure you have signed up',p_error='')
			#return redirect("/login")
	return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def  signup():

	username = ''
	u_error = ''
	p_error = ''
	pv_error = ''
	multifield_error = ''

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		verify=request.form['verify']
		existing_user = User.query.filter_by(username=username).first()
		
		if len(password) < 3:
			p_error = 'Invalid Password!'
		if len(username) < 3:
			u_error = 'Invalid Username!'
		if verify != password:
			pv_error = 'Passwords do not Match!'
		if len(username) == 0 or len(password) == 0 or len(verify) == 0:
			multifield_error = 'One or more fields are Invalid!'
		if len(multifield_error) == 0 and len(u_error) == 0 and len(p_error) == 0 and len(pv_error) == 0 and not existing_user:
			new_user = User(username, password)
			db.session.add(new_user)
			db.session.commit()
			session['username'] = username
			return redirect('/newpost')
		else:
			u_error = 'Username already Exists!'
	return render_template('signup.html', u_error=u_error, p_error=p_error, pv_error=pv_error)

@app.route('/newpost', methods=['POST','GET'])
def newpost():
	##		Initilisation of the error_message to empty list:[] no error
	error_message=[]		#error_message=[error_title, error_body]
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
			
		user=User.query.filter_by(username=session['username']).first()
		owner = User.query.filter_by(username=session['username']).first()

		if len(blog_title)>0 and len(blog_body)>0:
			# No error in the filling the newpost's form
			# Create an object of the class Blog
			new_blog=Blog(blog_title, blog_body, owner) # composants of the blog
			db.session.add(new_blog) 	# add new blog to the database
			db.session.commit()      # confirmation of adding the new post to the database
			# allpost.append(new_blog) # adding the new blog to the list
			# Redirect to individual blog post using current blog's information, id is automatically
			return redirect('/blog?id={0}'.format(new_blog.id))
		else:
			return render_template('newpost.html', title_error=error_message[0], body_error=error_message[1])
	else:
		return render_template('newpost.html')

@app.route('/blog', methods=['GET'])
def blog():
#	# variable blog_id for requesting id from database
	blog_id = request.args.get('id')
	owner=request.args.get('owner')
	
	user_posts=Blog.query.filter_by(owner=owner).order_by(Blog.id.desc())
#	user_id= request.args.get('owner_id')
#	# If request is true grab blog using id and render template that returns single blog post
	if blog_id:
		blog = Blog.query.get(blog_id)
		btitle=blog.blog_title
		bbody=blog.blog_body
		return render_template('displayentry.html',blog=blog, btitle=btitle, bbody=bbody)
		#		#Render page that holds all blogs
		#	#return render_template('showall.html', blogs=Blog.query.order_by(Blog.id.desc()).all())

	user_username = request.args.get('user')
	allblog=Blog.query.all()
#	Select the blogs by user_name. Select from Blog, where username=request.args.get('user')
	if user_username: # If exists
		users = Blog.query.filter_by(owner_id=user_username)
		
		return render_template('singleUser.html', users=users)
	return render_template('blog.html', blogs=Blog.query.all(), users = Blog.query.filter_by(owner_id=user_username))

@app.route('/logout')
def logout():
	del session['username']
	return redirect('/')

if __name__ == '__main__':
	app.run()
