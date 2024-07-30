#!/usr/bin/env python3
"""
Basic Flask app with Babel for internationalization.
"""

from flask import Flask, render_template
from flask_babel import Babel
import config

app = Flask(__name__)
app.config.from_object(config.Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Route to render the index page.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
