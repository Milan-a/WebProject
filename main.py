from flask import Flask, render_template, redirect, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.forms.login_form import LoginForm
from data.forms.register_form import RegisterForm
from data.forms.resume_add_form import ResumeAddForm
from data.forms.vacancies_add_form import VacanciesAddForm
from data.resume import Resume
from data.users import User
from data import db_session
from data.vacancies import Vacancies

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
def index():
    return vacancies()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/vacancies')
def vacancies():
    data = []
    db_sess = db_session.create_session()
    for vacancies in db_sess.query(Vacancies).all():
        data.append(vacancies)
    data.reverse()
    template_name = 'vacancies.html'
    return render_template(template_name, data=data, res_vac='vac')


@app.route('/resume')
def resume():
    data = []
    db_sess = db_session.create_session()
    for resume in db_sess.query(Resume).all():
        data.append(resume)
    data.reverse()
    template_name = 'resume.html'
    return render_template(template_name, data=data, res_vac='res')


@app.route('/vacancies_search/<category>/<request>')
def vacancies_search(category, request):
    data = []
    db_sess = db_session.create_session()
    if category == 'name':
        vacancy = db_sess.query(Vacancies).filter(Vacancies.title.like(f"%{request}%"))
    elif category == 'description':
        vacancy = db_sess.query(Vacancies).filter(Vacancies.description.like(f"%{request}%"))
    elif category == 'address':
        vacancy = db_sess.query(Vacancies).filter(Vacancies.address.like(f"%{request}%"))
    elif category == 'price':
        vacancy = db_sess.query(Vacancies).filter(Vacancies.price.like(f"%{request}%"))
    else:
        vacancy = db_sess.query(Vacancies).filter(Vacancies.title.like(f"%{request}%")
                                                  | Vacancies.company.like(f"%{request}%")
                                                  | Vacancies.price.like(f"%{request}%")
                                                  | Vacancies.experience.like(f"%{request}%")
                                                  | Vacancies.address.like(f"%{request}%")
                                                  | Vacancies.schedule.like(f"%{request}%")
                                                  | Vacancies.hours.like(f"%{request}%")
                                                  | Vacancies.description.like(f"%{request}%"))

    for vac in vacancy:
        data.append(vac)
    data.reverse()
    template_name = 'vacancies.html'
    return render_template(template_name, data=data, res_vac='vac')


@app.route('/resume_search/<category>/<request>')
def resume_search(category, request):
    data = []
    db_sess = db_session.create_session()
    if category == 'name':
        resumes = db_sess.query(Resume).filter(Resume.title.like(f"%{request}%"))
    elif category == 'description':
        resumes = db_sess.query(Resume).filter(Resume.about_me.like(f"%{request}%")
                                               | Resume.education.like(f"%{request}%")
                                               | Resume.specializations.like(f"%{request}%"))
    elif category == 'address':
        resumes = db_sess.query(Resume).filter(Resume.place_of_residence.like(f"%{request}%"))
    elif category == 'price':
        resumes = db_sess.query(Resume).filter(Resume.price.like(f"%{request}%"))
    else:
        resumes = db_sess.query(Resume).filter(Resume.title.like(f"%{request}%")
                                               | Resume.age.like(f"%{request}%")
                                               | Resume.gender.like(f"%{request}%")
                                               | Resume.price.like(f"%{request}%")
                                               | Resume.experience.like(f"%{request}%")
                                               | Resume.place_of_residence.like(f"%{request}%")
                                               | Resume.last_place_of_work.like(f"%{request}%")
                                               | Resume.education.like(f"%{request}%")
                                               | Resume.specializations.like(f"%{request}%")
                                               | Resume.about_me.like(f"%{request}%"))

    for res in resumes:
        data.append(res)
    data.reverse()
    template_name = 'resume.html'
    return render_template(template_name, data=data, res_vac='res')


@app.route('/vacancies_add_form', methods=['GET', 'POST'])
def vacancies_add_form():
    form = VacanciesAddForm()
    if form.validate_on_submit():
        if not form.title.data:
            return render_template('vacancies_add_form.html',
                                   form=form,
                                   message="Введите название вакансии")
        db_sess = db_session.create_session()
        usr_id = current_user.id
        vacancies = Vacancies(
            title=form.title.data,
            company=form.company.data,
            price=form.price.data,
            experience=form.experience.data,
            address=form.address.data,
            schedule=form.schedule.data,
            hours=form.hours.data,
            description=form.description.data,
            phone=form.phone.data,
            email=form.email.data,
            user_id=usr_id
        )
        db_sess.add(vacancies)
        db_sess.commit()
        return redirect('/profile')
    return render_template('vacancies_add_form.html', form=form)


@app.route('/resume_add_form', methods=['GET', 'POST'])
def resume_add_form():
    form = ResumeAddForm()
    if form.validate_on_submit():
        if not form.title.data:
            return render_template('resume_add_form.html',
                                   form=form,
                                   message="Введите название вакансии")

        db_sess = db_session.create_session()
        usr_id = current_user.id

        # if form.portfolio.data:
        #     filename = secure_filename(form.portfolio.data.filename)
        #     image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #     form.portfolio.data.save(image_path)

        resume = Resume(
            title=form.title.data,
            age=form.age.data,
            gender=form.gender.data,
            price=form.price.data,
            experience=form.experience.data,
            place_of_residence=form.place_of_residence.data,
            last_place_of_work=form.last_place_of_work.data,
            education=form.education.data,
            specializations=form.specializations.data,
            about_me=form.about_me.data,
            contacts=form.contacts.data,
            user_id=usr_id
        )

        db_sess.add(resume)
        db_sess.commit()
        return redirect('/profile')
    return render_template('resume_add_form.html', form=form)


@app.route('/support')
def support():
    template_name = 'support.html'
    return render_template(template_name)


@app.route('/profile')
def profile():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        user_id = current_user.get_id()

        res = db_sess.query(Resume).filter(Resume.user_id == user_id).first()
        resume = 0 if res is None else res

        vac = db_sess.query(Vacancies).filter(Vacancies.user_id == user_id).first()
        vacancies = 0 if vac is None else vac
        # print(f'User id-{user_id}: resume-{resume}, vacancies-{vacancies}')

        template_name = 'profile.html'
        return render_template(template_name, resume=resume, vacancies=vacancies)


@app.route('/vacancy/<int:vacancy_id>')
def vacancy_detail(vacancy_id):
    db_sess = db_session.create_session()
    vacancy = db_sess.query(Vacancies).filter(Vacancies.id == vacancy_id).first()
    if vacancy is None:
        return "Вакансия не найдена", 404
    return render_template('vacancy_detail.html', vacancy=vacancy)


@app.route('/resume/<int:resume_id>')
def resume_detail(resume_id):
    db_sess = db_session.create_session()
    resume = db_sess.query(Resume).filter(Resume.id == resume_id).first()
    if resume is None:
        return "Резюме не найдено", 404
    return render_template('resume_detail.html', resume=resume)


@app.route('/delete_resume/<int:resume_id>')
def delete_resume(resume_id):
    db_sess = db_session.create_session()
    resume = db_sess.query(Resume).get(resume_id)
    if not resume:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(resume)
    db_sess.commit()
    return redirect("/profile")


@app.route('/delete_vacancies/<int:vacancies_id>')
def delete_vacancies(vacancies_id):
    db_sess = db_session.create_session()
    vacancies = db_sess.query(Vacancies).get(vacancies_id)
    if not vacancies:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(vacancies)
    db_sess.commit()
    return redirect("/profile")


@app.route('/resume_edit/<int:resume_id>', methods=['GET', 'POST'])
@login_required
def resume_edit(resume_id):
    db_sess = db_session.create_session()
    resume = db_sess.query(Resume).get(resume_id)

    if not resume:
        return "Резюме не найдено", 404

    if resume.user_id != current_user.id:
        return "Нет доступа", 403

    form = ResumeAddForm(obj=resume)  # Инициализируем форму с существующими данными
    if form.validate_on_submit():
        resume.title = form.title.data
        resume.age = form.age.data
        resume.gender = form.gender.data
        resume.price = form.price.data
        resume.experience = form.experience.data
        resume.place_of_residence = form.place_of_residence.data
        resume.last_place_of_work = form.last_place_of_work.data
        resume.education = form.education.data
        resume.specializations = form.specializations.data
        resume.about_me = form.about_me.data
        resume.contacts = form.contacts.data

        db_sess.commit()
        return redirect('/profile')

    return render_template('resume_add_form.html', form=form, title='Редактировать резюме')


@app.route('/vacancy_edit/<int:vacancies_id>', methods=['GET', 'POST'])
@login_required
def vacancy_edit(vacancies_id):
    db_sess = db_session.create_session()
    vacancy = db_sess.query(Vacancies).get(vacancies_id)

    if not vacancy:
        return "Вакансия не найдена", 404

    if vacancy.user_id != current_user.id:
        return "Нет доступа", 403

    form = VacanciesAddForm(obj=vacancy)  # Инициализируем форму с существующими данными
    if form.validate_on_submit():
        vacancy.title = form.title.data
        vacancy.company = form.company.data
        vacancy.price = form.price.data
        vacancy.experience = form.experience.data
        vacancy.address = form.address.data
        vacancy.schedule = form.schedule.data
        vacancy.hours = form.hours.data
        vacancy.description = form.description.data
        vacancy.phone = form.phone.data
        vacancy.email = form.email.data

        db_sess.commit()
        return redirect('/profile')

    return render_template('vacancies_add_form.html', form=form, title='Редактировать вакансию')


if __name__ == '__main__':
    db_session.global_init("db/data_base.sqlite")
    app.run(port=8080, host='127.0.0.1')
