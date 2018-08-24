import waiterdb
database_url = 'HOST'
conn = waiterdb.connect(database_url, user='WAITER_USER', password='WAITER_PASSWORD', sourceType='SOURCE_TYPE', project='PROJECT', autocommit=True)
