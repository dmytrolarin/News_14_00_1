import flask

project = flask.Flask(
    import_name= "core",
    template_folder= "templates",
    static_url_path= "/core/",
    static_folder= "static"
)