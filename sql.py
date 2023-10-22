import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', database='calculator_history', charset='utf8')

cursor = db.cursor()

def get_history():
    sql = "SELECT * FROM history ORDER BY id DESC LIMIT 10"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

def save_history(formula, result):
    sql = "INSERT INTO history(formula, result) VALUES ('%s', '%s')" % (formula, result)
    cursor.execute(sql)
    db.commit()

db.close()

def pressEqual():
    global lists
    global isPressSign

    curnum = result.get()
    lists.append(curnum)

    computrStr = ''.join(lists)
    endNum = eval(computrStr)

    save_history(computrStr, endNum)  # 将计算历史记录保存到数据库中

    result.set(endNum)
    result2.set(computrStr)
    lists.clear()