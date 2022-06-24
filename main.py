from flask import Flask, render_template, jsonify, session, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir + '\database', 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'R~XHH!jmN]LWXT/A78Zrejn359854tjnsT98j/3yX R~XHH!jmN]LWXT'
db = SQLAlchemy(app)

@app.route('/')
def index():
    title = 'Shifty Studio - Вы отдыхаете, мы работаем!'
    return render_template('index.html', title = title)

@app.route('/login')
def loginUserPage():
    if 'user' in session:
        return redirect('/profile')
    else:
        title = 'Shifty Studio - Авторизация'
        return render_template('login.html', title = title)

@app.route('/sign-up')
def createNewUserPage():
    if 'user' in session:
        return redirect('/profile')
    else:
        title = 'Shifty Studio - Регистрация'
        return render_template('sign-up.html', title = title)

@app.route('/user/sign-up', methods = ['POST'])
def newUser():
    login = request.form['login']
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']

    if Users.query.filter_by(login = login).all() != []:
        message = 'Такой логин уже занят'
        return render_template('sign-up.html', message = message)
    else:
        if Users.query.filter_by(email = email).all() != []:
            message = 'Такой email уже занят'
            return render_template('sign-up.html', message = message)
        else:
            secret_password = generate_password_hash(password)
            new_user = Users(login = login, email = email, name = name, password = secret_password)
            db.session.add(new_user)
            db.session.commit()
            title = 'Shifty Studio - Успешная регистрация'
            session['user'] = login
            return render_template('success-signup.html', title = title)

@app.route('/user/login', methods = ['POST'])
def userLogin():
    login = request.form['login']
    password = request.form['password']

    if Users.query.filter_by(login = login).all() == []:
        message = 'Аккаунт не существует'
        return render_template('login.html', message = message)
    else:
        user = Users.query.filter_by(login = login).first()
        secret_password = user.password
        checked_password = check_password_hash(secret_password, password)

        if checked_password != True:
            message = 'Неверный пароль'
            return render_template('login.html', message = message)
        else:
            if 'user' in session:
                return redirect('/profile')
            else:
                session['user'] = login
                return redirect('/profile')

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect('/login')
    else:
        return redirect('/')

@app.route('/profile', methods = ['GET'])
def myProfile():
    if 'user' in session:
        title = 'Shifty Studio - Профиль ' + session['user']
        user = Users.query.filter_by(login = session['user']).first()

        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            user_ip = request.environ['REMOTE_ADDR']
        else:
            user_ip = request.environ['HTTP_X_FORWARDED_FOR']

        return render_template('profile.html', title = title, user_info_id = user.id, user_info_login = user.login, user_info_email = user.email, user_info_name = user.name, user_info_ip = user_ip)
    else:
        return redirect('/login')

@app.route('/api/get/projects', methods = ['GET'])
def getProjects():
    projects = []
    db_projects = Projects.query.all()
    for row in db_projects:
        projects_data = {}
        projects_data['name'] = row.name
        projects_data['img'] = row.img
        projects_data['url'] = row.url
        projects.append(projects_data)
    return jsonify(projects)

@app.route('/api/get/questions', methods = ['GET'])
def getQuestions():
    questions = []
    db_questions = AboutUs.query.all()
    for row in db_questions:
        questions_data = {}
        questions_data['question'] = row.question
        questions_data['answer'] = row.answer
        questions.append(questions_data)
    return jsonify(questions)

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(25), nullable = False, unique = True)
    email = db.Column(db.String(25), nullable = False, unique = True)
    name = db.Column(db.String(25), nullable = True, unique = False, default = 'Не указано')
    date_reg = db.Column(db.Date(), default = datetime.utcnow)
    password = db.Column(db.String(255), nullable = False, unique = False)

    def __init__(self, login, email, name, password):
        self.login = login
        self.email = email
        self.name = name
        self.password = password

class Admins(db.Model):
    __tablename__ = 'Admins'
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(25), nullable = True, unique = True)
    password = db.Column(db.String(255), nullable = True, unique = False)

    def __init__(self, login, password):
        self.login = login
        self.password = password

class Projects(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable = True, unique = True)
    img = db.Column(db.String(255), nullable = True, unique = False)
    url = db.Column(db.String(255), nullable = True, unique = True)

    def __init__(self, name, img, url):
        self.name = name
        self.img = img
        self.url = url

class AboutUs(db.Model):
    __tablename__ = 'AboutUs'
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String(255), nullable = True, unique = True)
    answer = db.Column(db.Text, nullable = True, unique = False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


# db.create_all()
# db.drop_all()

if __name__ == "__main__":
    app.run()
