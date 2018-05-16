from .. import app
from .views import Index

def approuter():
    app.add_url_rule('/', view_func = Index.as_view('/'), methods=['GET'])
