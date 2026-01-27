from flask import Flask

def create_app():
    # Skapar själva Flask-appen
    app = Flask(__name__)

    # Här hämtar vi (importerar) dina routes från Presentation-lagret
    from .presentation.routes import main_bp
    
    # Här kopplar vi ihop dessa routes med appen
    app.register_blueprint(main_bp)

    return app