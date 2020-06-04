import sqlite3




# def
if __name__ == "__main__":
    # SQLite DB 연결
    conn = sqlite3.connect("test.sqlite3")

    # Connection 으로부터 Cursor 생성
    cur = conn.cursor()
    # SQL 쿼리 실행
    try:
        cur.execute('select * from customer')
    except sqlite3.OperationalError:
        cur.execute(
            'create table {0}(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, magnet BLOB)'.format('torrent'))
        print('Table Not Created')
        print('I Will Create Them')
        # print('{1} and {0}'.format('spam', 'eggs'))
    # DELETE
    # FROM customer
    # WHERE id IN(
    #     SELECT id FROM(SELECT id FROM customer GROUP BY name HAVING count(*) > 1) temp_table
    # );

        # 데이타 Fetch
    # for row in cur.fetchall():
    #     print(row)

    # Connection 닫기
    conn.close()
