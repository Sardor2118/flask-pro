from flask import Flask, render_template, request, redirect, url_for

from question import questions
from question.questions import question_bp
from user.user import user_bp

app = Flask(__name__)

#база даннах с вопросом
questions = [{"id": 1, "title": "Кто придумал Python?", "content": "Подскажите ответ"},
            {"id": 2, "title": "Как работать на flask?", "content": "что нужно для работы в flask?"}]
# база с ответами
answers = [{"id": 1, "question_id": 1, "answer": "Все знают, что создатель является 1234"},
           {"id": 2, "question_id": 2, "answer": "Нужно прописать pip install flask"}]


# настройка для защиты
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'aslkmdlamdalkd21asm31'

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", questions=questions)
@app.route('/question/<int:question_id>')
def question(question_id):
    question = next((q for q in questions if q.get('id') == question_id), None)
    if question:
        question_answers = [a for a in answers if a.get('question_id') == question_id]
        return render_template('question.html', question=question, question_answers=question_answers)
    else:
        'Вопрос не найден'

# добавление вопросов
@app.route('/ask', methods=['GET' ,'POST'])
def ask():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_content = {"id": len(questions) + 1, "title": title, "content": content}
        questions.append(new_content)
        return redirect(url_for('home'))
    else:
        return render_template('ask.html')


app.register_blueprint(user_bp)
app.register_blueprint(question_bp)



app.run(debug=True)
