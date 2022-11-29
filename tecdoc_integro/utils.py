# from config import load_session
#
#
# def fetch_queryset(session, ModelClass):
#     return session.query(ModelClass).all()
#
#
# def filter_queryset_first(session, ModelClass, no_of_records):
#
#     return session.query(ModelClass).limit(no_of_records).all()
#
# def filter_queryset_with_id(session, ModelClass, id):
#     return session.query(ModelClass).filter(ModelClass.id==id)[0]
#
# def filter_queryset_with_article_number(session, ModelClass, article_number):
#     return session.query(ModelClass).filter(ModelClass.DataSupplierArticleNumber==article_number)