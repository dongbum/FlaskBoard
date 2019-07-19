# -*- coding: utf-8 -*-

import pymysql
from flask import render_template, request, current_app
from board.board_blueprint import board

@board.route('/list', methods=['GET'])
def list():
    page = request.args.get('page')

    db_address = current_app.config['DB_ADDRESS']
    db_port = current_app.config['DB_PORT']
    db_id = current_app.config['DB_ID']
    db_password = current_app.config['DB_PASSWORD']
    db_name = current_app.config['DB_NAME']

    conn = pymysql.connect(host=db_address,
                           port=int(db_port),
                           user=db_id,
                           password=db_password,
                           db=db_name,
                           charset='utf8')

    try:
        cursor = conn.cursor()
        sql = "SELECT `no`, `content`, `writer`, `read` FROM board ORDER BY `write_time` DESC"
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row_data in rows:
            print('no:[%s] content:[%s] writer:[%s] read:[%s]' % (row_data[0], row_data[1], row_data[2], row_data[3]))

    finally:
        conn.close()

    return render_template('list.html', rows=rows)