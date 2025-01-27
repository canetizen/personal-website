from flask import Flask, render_template, redirect, url_for, json, abort

app = Flask('canetizen', template_folder='app/templates', static_folder='app/static')

def load_translations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

layout_translations = load_translations('translations/layout_tran.json')
index_translations = load_translations('translations/index_tran.json')
academic_translations = load_translations('translations/academic_tran.json')
contact_translations = load_translations('translations/contact_tran.json')

last_updated = "27 January 2025, 11:00 AM +03"

@app.route('/')
def index():
    return redirect(url_for('about', lang='tr'))

@app.route('/<lang>/about')
def about(lang):
    if lang not in ['tr', 'en']:
        abort(404)
    return render_template('index.html', translations={**layout_translations, **index_translations}, current_language=lang, endpoint='about', last_updated=last_updated)

@app.route('/<lang>/academic', methods=['GET'])
def academic(lang):
    if lang not in ['tr', 'en']:
        abort(404)
    return render_template('academic.html', translations={**layout_translations, **academic_translations}, current_language=lang, endpoint='academic', last_updated=last_updated)

@app.route('/<lang>/contact', methods=['GET'])
def contact(lang):
    if lang not in ['tr', 'en']:
        abort(404)
    return render_template('contact.html', translations={**layout_translations, **contact_translations}, current_language=lang, endpoint='contact', last_updated=last_updated)

@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page Not Found", 404

if __name__ == "__main__":
    app.run()
