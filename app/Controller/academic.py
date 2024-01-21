from flask import Blueprint, render_template

academicBP = Blueprint('academic', __name__)

@academicBP.route('/<lang>/academic', methods=['GET'])
def academic(lang):
    return render_template('academic.html', current_language=lang, endpoint="academic.academic")
