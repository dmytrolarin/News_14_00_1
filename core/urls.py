import user
from .settings import project

user.user_app.add_url_rule(
    rule= "/registration/",
    view_func= user.render_registration,
    methods = ["GET", "POST"]
)
project.register_blueprint(user.user_app)