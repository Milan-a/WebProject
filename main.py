from flask import Flask, render_template, request, redirect, url_for
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET'])
def index():
    return render_template('registration.html')


@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    # Здесь можно добавить логику для сохранения пользователя в бд

    return redirect(url_for('main_page'))


@app.route('/main', methods=['GET'])
def main_page():
    return render_template('resume.html')


@app.route('/vacancies', methods=['GET'])
def vacancies():
    template_name = 'vacancies.html'
    return render_template(template_name)


@app.route('/resume', methods=['GET'])
def resume():
    template_name = 'resume.html'
    return render_template(template_name)


if __name__ == '__main__':
    db_session.global_init("db/data_base.sqlite")
    app.run(port=8080, host='127.0.0.1')