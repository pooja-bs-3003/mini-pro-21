from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField 
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'project21'
Bootstrap(app)
class ProjectForm(FlaskForm):
    ProjectName = StringField('ProjectName', validators=[InputRequired()])
    TrainingData = FileField('TrainData',validators=[FileRequired()])
    TestData = FileField('TestData',validators=[FileRequired()])
    Submit = SubmitField('Submit')

@app.route('/project', methods=['GET','POST'])
def project():
    form = ProjectForm()
    if form.validate_on_submit():
        return '<h2>' + form.ProjectName.data+''+'</h2>'
    return render_template('page1.html',form =form)




if __name__ =='__main__':
    app.run(debug=True)


