#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """ docs docs """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """ docs docs """
    users_id = request.args.get("login_as")
    if users_id is not None and int(users_id) in users:
        return users[int(users_id)]
    return None


@app.before_request
def before_request():
    """ docs docs """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """ docs docs """
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ flask funct """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
