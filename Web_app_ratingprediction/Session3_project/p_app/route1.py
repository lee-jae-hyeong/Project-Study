from flask import Flask, render_template, request, url_for, redirect, Blueprint
from p_app.models.list import List
from p_app.models.user import User
from p_app import db
from p_app.train import model
from p_app.naver_scr import movie, code, people

bp = Blueprint('route1', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
#---------------------------------------------------------------#
@bp.route('/add')
def add():
    return render_template('add.html')
#---------------------------------------------------------------#
@bp.route('/adduser')
def add_user():
    username1 = request.args.get('username')
    # password1 = request.args.get('password') 비밀번호 받기.


    if not username1 :
        return 'Enter username', 400

    if User.query.filter_by(username = username1).first() is not None :
        return 'The name is already registered. Please put a number after your name.', 400  


    if User.query.filter_by(username = username1).first() is None :
#         db.session.add(User(username = username1, password = password1))
        db.session.add(User(username = username1))
        db.session.commit()

        return redirect(url_for('route1.index'))

#---------------------------------------------------------------#
@bp.route('/regist')
def regist():
    return render_template('regist.html')

#---------------------------------------------------------------#
@bp.route('/registmovie')
def registmovie():    
    name1 = request.args.get('name').replace(' ','')
    rat = request.args.get('rating')
    username = request.args.get('username')
    
    try :
        movie(name1)
    except :
        return 'Please check the title of the movie again.', 400
    

    
    try :
        float(rat)
    except :
        return 'Please write in numbers.', 400

    if float(rat) < 0 :
        return 'Please enter positive number.', 400 
    
    if float(rat) > 5 :
        return 'Put it between 0 and 5.', 400


    if not User.query.filter_by(username = username).first() :
        return 'Please register your name', 400

    # if List.query.filter_by(name = name1) :
    #     return "It's already been evaluated.", 400

    # else :

  
    try :
        name1 = people(name1)[3]
        people(name1)
    except :
        return 'Movie not found. Please check the title of the movie again.', 400

    name1 = people(name1)[3]
    
    if List.query.filter_by(name = name1, username = username).first() :
        return "You've already evaluated it.", 400    

    if User.query.filter_by(username = username).first() :     
        movie_name = movie(name1) #cd 이전 할당 이름
        movie_code = code(movie_name) #b 이전 할당 이름
        movie_people = people(name1) #c 이전 할당 이름
        if movie_code[1] :
            db.session.add(List(name = movie_people[3], director = movie_people[0], genre = movie_code[0], country = movie_code[1], actor1 = movie_people[1], actor2 = movie_people[2], rating = rat, username = username))
            db.session.commit()
        else :
            db.session.add(List(name = movie_people[3], director = movie_people[0], genre = movie_code[0], country = movie_code[3], actor1 = movie_people[1], actor2 = movie_people[2], rating = rat, username = username))
            db.session.commit()

        return redirect(url_for('route1.index'))
#---------------------------------------------------------------#    
@bp.route('/search')
def search():
    list1 = List.query.all()
    if not list1 :
        return "There are no registered evaluations. Please regist your movie ratings", 400
    else :            
        return render_template('search.html', list1 = list1)
#---------------------------------------------------------------#
@bp.route('/search/')
@bp.route('/search/<int:id>')
def rat_delete(id=None):
    if not id :
        return '', 400
    if List.query.filter_by(id = id).first() is None:
        return '', 404

    else :
        a = List.query.filter_by(id = id).first()
        db.session.delete(a)
        db.session.commit()

        return redirect(url_for('route1.search'))    
#---------------------------------------------------------------#
@bp.route('/usersearch')
def user_search():
    list1 = User.query.all()
    if not list1 :
        return "There are no registered users. Please regist your name", 400
    else :
        return render_template('user_search.html', list1 = list1)
#---------------------------------------------------------------#
@bp.route('/usersearch/')
@bp.route('/usersearch/<int:id>')
def user_delete(id=None):

    if not id :
        return '', 400

    if User.query.filter_by(id = id).first() is None:
        return '', 404

    else :
        a = User.query.filter_by(id = id).first()
        db.session.delete(a)
        db.session.commit()
        return redirect(url_for('route1.user_search'))
#---------------------------------------------------------------#


@bp.route('/predict')
def predict():
    return render_template('predict.html')
#---------------------------------------------------------------#
@bp.route('/predict_search')
def predict_search():
    name = request.args.get('name').replace(' ','')
    name = people(name)[3]
    username = request.args.get('username')
    if not User.query.filter_by(username = username).first() :
        return "Please register your name", 400

    if List.query.filter_by(username = username, name = name).first():
        return "It's already been evaluated.", 400
    else : 
        predict = model(username, name)

        return render_template('predict_search.html', predict = predict, name = name, username = username)
#---------------------------------------------------------------#
## 생략
# @bp.route('/login', methods = ["post"])
# def login():
#     username = request.args.get('loginID')
#     password = request.args.get('password')

#     if User.query.filter_by(username = username, password = password).first():
#         return render_template('login.html')

#     elif User.query.filter_by(username = username, password != password).first():
#         return '비밀번호가 틀렸습니다. 비밀번호를 다시 한번 확인해주세요.', 400

#     elif User.query.filter_by(username != username).first()
#         return '존재하지 않는 유저입니다. 유저를 등록해주세요.', 400       

# @bp.route('/logout')
# def logout():
#     session.pop("userID")
#     redirect(url_for 





