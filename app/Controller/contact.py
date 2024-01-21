from flask import Blueprint, render_template

contactBP = Blueprint('contact', __name__)

@contactBP.route('/<lang>/contact', methods=['GET'])
def contact(lang):
    return render_template('contact.html', current_language=lang, endpoint="contact.contact")
