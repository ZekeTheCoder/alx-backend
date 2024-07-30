#!/usr/bin/env python3
"""
5. Mock logging in
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """
    Config class for Flask application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)

# Mock a database user table.
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported languages.
    """
    # Variable to store the locale parameter
    requested_locale = request.args.get('locale')

    # Checks if requested_locale is not None and if it is a supported locale.
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale
    else:
        # fall back to default behavior
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Retrieve a user based on login_as URL parameter."""
    user_id = request.args.get('login_as')

    # check if user exist and is a number
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Set the user before processing each request."""
    g.user = get_user()


@app.route('/')
def index():
    """
    Route to render the index page.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
