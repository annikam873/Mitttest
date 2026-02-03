"""
Public routes - accessible without authentication.

This blueprint handles all public-facing pages including the landing page.
"""

from flask import Blueprint, render_template

bp = Blueprint("public", __name__)


@bp.route("/")
def index():
    """Render the landing page."""
    return render_template("index.html")


@bp.route("/subscribe")
def subscribe():
    """Render the subscription form."""
    return render_template("subscribe.html")


@bp.route("/om")
def about():
    """Render the about page."""
    return render_template("about.html")
