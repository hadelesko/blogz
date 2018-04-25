from flask import Flask, request, redirect, render_template

import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/newpost')
def indx():
	return render_template('myforms.html',body_error="Dommage dommage!!!", title_error="ne repectpas les mots")
	
@app.route('/pierre')
def index():
	return render_template('myforms.html', body_error="Dommage dommage!!!", title_error="ne repectpas les mots")
if __name__ == '__main__':
    app.run()