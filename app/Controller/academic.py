from flask import Blueprint, render_template

academicBP = Blueprint('academic', __name__, url_prefix='/academic')

@academicBP.route('/', methods=['GET'])
def academic():
    return render_template("academic.html", context = {"title":"Akademik"})