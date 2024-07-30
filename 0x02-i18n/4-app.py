#!/usr/bin/env python3
"""
4. Force locale with URL parameter
"""

from flask import Flask, render_template, request
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


@app.route('/')
def index():
    """
    Route to render the index page.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
