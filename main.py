import mysql.connector
db = mysql.connector.connect(
        host = "www.mydomain-hit-db-demo.com",
        user = "root",
        password = "",
        database = "hit-db-demo",
        charset = 'utf8', use_unicode=True
    )
print(db)