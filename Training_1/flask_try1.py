from fileinput import filename
from posixpath import abspath
from flask import Flask as fl,render_template as rt
from flask_wtf import FlaskForm #CSRF   
from wtforms import FileField,SubmitField
from werkzeug.utils import secure_filename
import os
app=fl(__name__)
app.config['SECRET_KEY']='supersecretkey'
app.config['UPLOAD_FOLDER']='static/Files'
class uploadfile(FlaskForm):
    file=FileField("file")
    submit=SubmitField("Upload file")
@app.route("/okok",methods=['GET','POST'])
def home():
    form=uploadfile()
    if form.validate_on_submit():
        file=form.file.data
        filename = secure_filename(file.filename)
        to_save=(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename))
        file.save(to_save)
        return rt('kharshi_editor.html')
    return rt('index.html',form=form)
if __name__=='__main__':
    app.run(debug=True)