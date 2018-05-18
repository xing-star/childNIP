from .. import app
from .views import Index, Query, Add, Update, Delete

def approuter():
    app.add_url_rule('/', view_func = Index.as_view('/'), methods=['GET'])

    # 查询路由
    app.add_url_rule('/query', view_func=Query.as_view('/query'), methods=['GET'])

    # 增加路由
    app.add_url_rule('/add', view_func=Add.as_view('/add'), methods=['POST', 'GET'])

    # 修改路由
    app.add_url_rule('/update', view_func=Update.as_view('/update'), methods=['PUT'])

    # 删除路由
    app.add_url_rule('/delete', view_func=Delete.as_view('/delete'), methods=['DELETE'])