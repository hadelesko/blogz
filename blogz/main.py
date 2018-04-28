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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:password@localhost:3306/blogz'
app.config['SQLALCHEMY_ECHO'] = True
blogs=db.relationship('movie', backref=owner)
db = SQLAlchemy(app)
app.secret_key = 'danken'


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(120))
    password  = db.Column(db.String(300))
    logged_in = db.Column(db.Boolean)
    user_id   = db.Column(db.Integer, db.ForeignKey('user.id'))
    blogs     = db.relationship('Blogs', backref=owner)
    
    def __init__(self,blog_title, blog_body, posted):
        self.username= username
        self.password= password
        self.logged_in = False

@app.before_request
def require_login():
    allowed_routes = ['login', 'signup']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['username'] = username
            flash("Logged in")
            return redirect('/')
        else:
            flash('User password incorrect, or user does not exist', 'error')

    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def  signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # TODO - validate user's data

        existing_user = User.query.filter_by(username=username).first()
        if not existing_user:
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            return redirect('/')
        else:
            # TODO - user better response messaging
            
            return "<h1>Duplicate user</h1>"

    return render_template('signup.html')

@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')
@app.route('/', methods=['POST', 'GET'])
def index():

    owner = User.query.filter_by(email=session['username']).first()

    if request.method == 'POST':
        task_name = request.form['task']
        new_task = Task(task_name, owner)
        db.session.add(new_task)
        db.session.commit()

    tasks = Task.query.filter_by(completed=False,owner=owner).all()
    completed_tasks = Task.query.filter_by(completed=True,owner=owner).all()
    return render_template('todos.html',title="Get It Done!", 
        tasks=tasks, completed_tasks=completed_tasks)


@app.route('/delete-task', methods=['POST'])
def delete_task():

    task_id = int(request.form['task-id'])
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
app.run()

@app.route('/', methods=['POST', 'GET'])
def confirm_signup():
	username = request.form['username']
	password= request.form['password']
	verify_password= request.form['verify_password']
	email= request.form['email']
	errors = { "username": "", "password": "", "verify_password": "", "email" : ""}
	
	u_error= ""      #errors_massage[0]   #=(list(errors.values()))[0]
	p_error= ""      #errors_massage[1]   #=(list(errors.values()))[1]
	pv_error= ""     #errors_massage[2]   #=(list(errors.values()))[2]
	em_error= ""     #errors_massage[3]   #=(list(errors.values()))[3]
	errors_massage=[]
	if len(username)==0 or len(username) not in range(3, 21) or username.find(' ')!=-1:
		#errors["username"] = "The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
		u_error="The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
		errors_massage.append(u_error)
		#return u_error
	else:
		u_error=""
		errors_massage.append(u_error)
		#return u_error

	if len(password) not in range(3, 21) or password.find(' ')!=-1:
		#errors["password"] = "The '{0}'length has not to be out of the range 3 to 21".format("password")
		p_error= "The '{0}'length has not to be out of the range 3 to 21".format("password")
		p_error
		errors_massage.append(p_error)
		#return p_error
	else:
		p_error=""
		errors_massage.append(p_error)
		#return p_error



	#TODO 1: Fix this later to redirect to '/welcome?username={username}'

	if len(errors_massage[0])==0 and len(errors_massage[1])==0 and len(errors_massage[2])==0 and len(errors_massage[3])==0:
		#if len(u_error)==0 and len(p_error)==0 and len(pv_error)==0 and len(em_error)==0:
		return render_template('confirm.html', email=email, username=username)
		#return redirect('/welcome?username=' + )

		#case errors == at least field has errors
	else:
		return render_template('signup.html', u_error=errors_massage[0], p_error=errors_massage[1], pv_error=errors_massage[2], em_error=errors_massage[3], username=username, email=email)
