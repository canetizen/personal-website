from flask import render_template
from flask import Flask
from app.Controller.academic import academicBP
from app.Controller.contact import contactBP

app = Flask('canetizen', template_folder=f'/home/canetizen/mysite/app/templates', static_folder=f'/home/canetizen/mysite/app/static')
app.secret_key = 'EECY'

app.register_blueprint(academicBP)
app.register_blueprint(contactBP)

@app.route('/')
def index():
    return render_template('index.html', context={"title": "Hakkımda"})

if __name__ == "__main__":
    app.run()
