import pymysql

def db_query(db, sql, params):
    # Connect to MySQL
    conn = pymysql.connect(
        host='codefrds.ckfb5jjpo5r8.ap-northeast-2.rds.amazonaws.com',
        user='admin',
        password='zhem2019!',
        charset='utf8',
        db=db
    )
    try:
        # create Dictionary Cursor
        with conn.cursor() as cursor:
            sql_query = sql
            # excute SQL
            cursor.execute(sql_query, params)
        # commit data
        conn.commit()
    finally:
        conn.close()
#
#def insert_trnasaction(email, password): 
#    sql = 'INSERT INTO trans_info (resut, data) VALUES (%s, %s)' 
#    params = (email, password) 
#    db_query(db='codef_db', sql=sql, params=params)

def insert_transaction(data1, data2, data3 ,data4, data5):
#def insert_trnasaction(data1,data2):
    sql = 'INSERT INTO transaction(commEndDate, commStartDate, resAccountBalance, resWithdrawalAmt, resTrHistoryList) VALUES (%s, %s, %s, %s, %s)'
    params = (data1, data2, data3, data4, data5)
#    params = (data1,data2)
    db_query(db='codef_db', sql=sql, params=params)


def insert_db(data1, data2, data3 ,data4, data5, data6, data7):
    sql = 'INSERT INTO codef_Transaction(serialNumber, resAccountIn, resName, resTraType, resType, resTime, resBalance) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    params = (data1, data2, data3, data4, data5, data6, data7)
    db_query(db='codef_db', sql=sql, params=params)




def select_transaction(number): 
    conn = pymysql.connect( host='codefrds.ckfb5jjpo5r8.ap-northeast-2.rds.amazonaws.com', user='admin', password='zhem2019!', charset='utf8', db='codef_db' ) 
    sql = 'SELECT * FROM codef_Transaction  WHERE serialNumber = %s' 
    params = (number,) 
    try: 
        with conn.cursor() as cursor: 
            cursor.execute(sql, params) 
            result = cursor.fetchone() 
            return result
        conn.commit() 
    finally: 
        conn.close()
'''
#미구현
def update_email(new, old): 
    sql = 'UPDATE student SET email = %s WHERE email = %s' 
    params = (new, old) 
    db_query(db='school', sql=sql, params=params)

def delete_student(email): 
    sql = 'DELETE FROM student WHERE email = %s' 
    params = (email,) 
    db_query(db='school', sql=sql, params=params)
'''
