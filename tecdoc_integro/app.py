from flask import Flask
from flask_restx import Resource, Api
# from models import Suppliers
# from config import load_session
from utils import fetch_queryset, filter_queryset_with_id, filter_queryset_first, filter_queryset_with_article_number

app = Flask(__name__)
app.config.from_pyfile('config.py')

# api = Api(app)
# session = load_session()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# @api.route('/main')
# class Hello(Resource):
#     def get(self):
#         articles = filter_queryset_first(session, Articles, 10)
#         articles_list = []
#         for article in articles:
#             print(article.supplierId)
#             supplier = filter_queryset_with_id(session, Suppliers, article.supplierId)
#             article_info_list = []
#             article_data = filter_queryset_with_article_number(session, ArticleInformation, article.DataSupplierArticleNumber)
#             print('aricle_inf', article_data)
#             for article_info in article_data:
#                 article_info_list.append({"informationText": article_info.InformationText, "informationType": article_info.InformationType})
#             articles_list.append({
#                 'ArticleNumber': article.DataSupplierArticleNumber,
#                 'description': article.Description,
#                 'supplierId': supplier.description,
#                 'pack_unit': article.PackingUnit,
#                 'info': article_info_list
#             })
#         return {
#             "message": "Hello",
#             "articles": articles_list
#         }


# @api.route('/main')
# class SuppliersAPI(Resource):
#     def get(self):
#         suppliers = filter_queryset_first(session, Suppliers, 10)
#         suppliers_list = []
#         for supplier in suppliers:
#
#             suppliers_list.append({
#                 'dataversion': supplier.dataversion,
#                 'description': supplier.description,
#
#             })
#         return {
#             "message": "Hello",
#             "articles": suppliers_list
#         }

if __name__ == '__main__':
    app.run()