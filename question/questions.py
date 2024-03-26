from flask import Blueprint, render_template

from question.forms import QuestionForm

question_bp = Blueprint('question_bp', __name__, url_prefix='/question')
@question_bp.route('/add_question', methods=['GET', 'POST'])
def add_question():
    form = QuestionForm()
    return render_template('add_question.html', form=form)
