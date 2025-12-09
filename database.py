import psycopg2

class Database():
    def __init__(self):
        self.host = "localhost"
        self.name = "ETL App DB"
        self.user = "postgres"
        self.password = "postgresql"
        self.port = 5432



    def connect_sql(self):
        self.conn = psycopg2.connect(host=self.host, dbname=self.name, user= self.user,
                                     password=self.password, port=self.port)
        self.cur = self.conn.cursor()


    def insert_row(self):
        insert_query = "INSERT INTO 'ETL App DB' (Sale_date, Store_ID, Product_ID, Product, 'Quantity sold', Price, Total_revenue)"\
                        "Values(%s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(insert_query, ("10", "9", "8", "7", "6", "5", "4"))
        self.conn.commit()
        self.conn.close()