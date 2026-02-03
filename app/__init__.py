from flask import Flask

def create_app():
    app = Flask(
        __name__,
        template_folder="presentation/templates",
        static_folder="presentation/static",
    )

    from .presentation.routes.public import bp as public_bp
    app.register_blueprint(public_bp)

    return app