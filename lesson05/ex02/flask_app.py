from flask import Flask, render_template

class FlaskApp:
    app = Flask(__name__)

    @staticmethod
    @app.route('/home/<name>')
    def home(name=None):
        return render_template('home.html',name=name)

    @staticmethod
    @app.route('/About')
    def about():
        return "this is the ABOUT page of my Flask App"

    @staticmethod
    @app.route('/user/<name>')
    def user_profile(name=None):
        return render_template('lesson05/ex02/profile.html', name=name, number=11111111, id=222)