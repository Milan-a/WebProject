from flask import Flask, render_template
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    template_name = 'resume.html'
    return render_template(template_name)

@app.route('/vacancies')
def vacancies():
    template_name = 'vacancies.html'
    return render_template(template_name)

@app.route('/resume')
def resume():
    template_name = 'resume.html'
    return render_template(template_name)


if __name__ == '__main__':
    db_session.global_init("db/data_base.sqlite")
    app.run(port=8080, host='127.0.0.1')
