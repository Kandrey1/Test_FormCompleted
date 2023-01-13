from app.db_mongo import insert_document, collection_forms


def create_data():
    insert_document(collection_forms,
                    {'name': 'OrderBuy',
                     'product_name': 'text',
                     'user_email': 'email'})

    insert_document(collection_forms,
                    {'name': 'OrderDate',
                     'client_phone': 'phone',
                     'date_buy': 'date'})

    insert_document(collection_forms,
                    {'name': 'OrderInfo',
                     'product_about': 'text',
                     'client_email': 'email'})

    insert_document(collection_forms,
                    {'name': 'DataClient',
                     'client_login': 'text',
                     'client_phone': 'phone',
                     'client_email': 'email'})

    insert_document(collection_forms,
                    {'name': 'UserInfo',
                     'user_name': 'text',
                     'user_email': 'email'})

    insert_document(collection_forms,
                    {'name': 'UserDateRegister',
                     'user_login': 'text',
                     'date_reg': 'date'})

    insert_document(collection_forms,
                    {'name': 'UserData',
                     'user_email': 'email',
                     'user_phone': 'phone'})

    insert_document(collection_forms,
                    {'name': 'RegistrationData',
                     'user_login': 'text',
                     'user_phone': 'phone',
                     'user_email': 'email'})

    insert_document(collection_forms,
                    {'name': 'ForumReg',
                     'client_phone': 'phone',
                     'user_login': 'text'})

    insert_document(collection_forms,
                    {'name': 'UserArticle',
                     'login_user': 'text',
                     'article': 'text',
                     'date_create': 'date'})
