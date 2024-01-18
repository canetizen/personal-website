from flask import Blueprint, render_template

contactBP = Blueprint('contact', __name__, url_prefix='/contact')

@contactBP.route('/', methods=['GET'])
def contact():
    return render_template("contact.html", context={"title": "İletişim"})