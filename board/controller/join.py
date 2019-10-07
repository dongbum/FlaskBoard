# -*- coding: utf-8 -*-

import pymysql
from flask import render_template, request, current_app
from board.board_blueprint import board

@board.route('/join')
def join():
    return render_template('join.html')

@board.route('/join_process', methods=['POST'])
def join_process():
    id = request.form['id']
    password = request.form['password_1']
    email = request.form['email']

    print('id:[%s] password:[%s] email:[%s]' % (id, password, email))

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
        sql = "INSERT INTO users(id, password, email) VALUES('%s', '%s', '%s')" % (id, password, email)
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return render_template('join.html', title='Member Join')