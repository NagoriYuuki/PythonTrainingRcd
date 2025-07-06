    import sqlite3

    con = sqlite3.connect('test1.db3')
    cur = con.cursor()

    sql = '''
    INSERT INTO beauty (
        keyword, no_face, one, two, three, four, five, six, seven, eight, nine, ten
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''

    values1 = ("abc", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    values2 = ("范冰冰", 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    values3 = ("高振力", 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)

    cur.execute(sql, values1)
    cur.execute(sql, values2)
    cur.execute(sql, values3)

    sql1 = '''
    DELETE FROM beauty WHERE id = ?
    '''
    cur.execute(sql1,(2,))

    sql2 = '''
    UPDATE beauty SET keyword = ? WHERE id = ?
    '''
    cur.execute(sql2, ("周杰伦",1))

    # cur.execute('DELETE FROM beauty;')

    con.commit()
    print("Accepted")

    con.close()
