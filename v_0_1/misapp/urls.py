from .. import app
from .views import Index, Query

def approuter():
    app.add_url_rule('/', view_func = Index.as_view('/'), methods=['GET'])
    app.add_url_rule('/query', view_func=Query.as_view('/query'), methods=['GET', 'POST'])
