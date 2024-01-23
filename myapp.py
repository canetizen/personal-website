from flask import render_template
from flask import Flask, redirect, url_for
from app.Controller.academic import academicBP
from app.Controller.contact import contactBP


app = Flask('canetizen', template_folder=f'app/templates', static_folder=f'app/static')

app.register_blueprint(academicBP)
app.register_blueprint(contactBP)

@app.route('/')
def index():
    return redirect(url_for('about', lang='tr'))

@app.route('/<lang>/about')
def about(lang):
    return render_template('index.html', current_language=lang, endpoint="about")

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=True, port=5001)
    app.run()
