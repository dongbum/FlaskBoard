# -*- coding: utf-8 -*-

import pymysql
from flask import render_template, request, redirect, url_for, current_app
from board.board_blueprint import board

@board.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        writer = request.form['writer']
        content = request.form['content']

        if writer and content:
            print('POST writer:[%s] content:[%s]' % (writer, content))
        else:
            return render_template('write.html')

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
            sql = "INSERT INTO board(writer, content) VALUES(%s, '%s')" % (writer, content)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        finally:
            conn.close()
            return redirect(url_for('.list'))

    return render_template('write.html', title='Article Write')