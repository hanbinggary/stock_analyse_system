from python.mysql.mysql_pool import sql_pool


"""获取数据库股票信息"""
def get_stock_info(key_word = None):
    sql = "select code_short,stock_name,stock_letters,area_stock_code from trade_stock"
    con = sql_pool().get_connection()
    cursor = con.cursor()
    """判断是否条件查询"""
    if(key_word != None):
        sql = sql + " where area_stock_code like %s or stock_name like %s or stock_letters like %s"
        cursor.execute(sql,(key_word,key_word,key_word))
    else:
        cursor.execute(sql)
    result = cursor.fetchall()
    con.close()
    return result
"""获取数据库股票总数"""
def get_stock_count():
    sql = "select count(1) count from trade_stock"
    con = sql_pool().get_connection()
    cursor = con.cursor()
    """判断是否条件查询"""
    cursor.execute(sql)
    result = cursor.fetchone()['count']
    con.close()
    return result

"""删除股票信息表"""
def delete_stock():
    sql = "delete from trade_stock "
    con = sql_pool().get_connection()
    cursor = con.cursor()
    """判断是否条件查询"""
    cursor.execute(sql)
    con.commit()
    con.close()
def add_stock_list(stock_list):
    sql = "insert ignore into trade_stock(stock_name,area_stock_code,code_short,stock_letters) values(%s,%s,%s,%s) "
    con = sql_pool().get_connection()
    cursor = con.cursor()
    """判断是否条件查询"""
    cursor.executemany(sql,stock_list)
    con.commit()
    con.close()