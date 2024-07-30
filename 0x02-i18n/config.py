#!/usr/bin/env python3
"""
Configuration settings for the Flask application.
"""


class Config:
    """
    Config class for Flask application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
