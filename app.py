from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField 
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecretkey'
Bootstrap(app)
class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(),Length(min=3, max =20)])
    password = PasswordField('password',validators=[InputRequired(),Length(min=5, max =80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(),Email(message='Invaild email'),Length(max=50)])
    username = StringField('username',validators=[InputRequired(),Length(min=3, max =20)])
    password = PasswordField('password',validators=[InputRequired(),Length(min=5, max =80)])
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h2>'+ form.username.data +''+form.password.data + '</h2>'
    

    return render_template('login.html',form = form)
    

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        return '<h2>'+ form.username.data +''+form.email.data +''+form.password.data+'</h2>'
    return render_template('signup.html',form =form)



if __name__ =='__main__':
    app.run(debug=True)



