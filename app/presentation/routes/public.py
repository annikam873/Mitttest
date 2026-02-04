"""
Public routes - accessible without authentication.

This blueprint handles all public-facing pages including the landing page
and subscription flow.
"""

from flask import Blueprint, render_template, request

bp = Blueprint("public", __name__)


@bp.route("/")
def index():
    """Render the landing page."""
    return render_template("index.html")


@bp.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    """Render the subscription form or handle submission."""
    if request.method == "POST":
        email = request.form.get("email", "")
        name = request.form.get("name", "")
        
        # Basic validation
        if not email:
            return render_template(
                "subscribe.html",
                error="Email is required",
                email=email,
                name=name,
            )
        
        # Normalize values
        email = email.lower().strip()
        name = name.strip() if name else "Subscriber"
        
        # For now, just show the thank you page
        # In a real app, you would save to the database here
        return render_template(
            "thank_you.html",
            email=email,
            name=name,
        )
    
    return render_template("subscribe.html")


@bp.route("/om")
def about():
    """Render the about page."""
    return render_template("about.html")
