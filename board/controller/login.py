# -*- coding: utf-8 -*-

import pymysql
from flask import render_template, request, current_app, session, redirect, url_for
from functools import wraps
from board.board_blueprint import board
from board.board_logger import Log

# 로그인처리용 함수
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            session_key = request.cookies.get(current_app.config['SESSION_COOKIE_NAME'])

            is_login = False

            if session.sid == session_key and session.__contains__('user_info'):
                is_login = True

            if not is_login:
                return redirect(url_for('.login_form', next=request.url))

            return f(*args, **kwargs)
        except Exception as e:
            Log.error('Login error : %s' % str(e))

    return decorated_function


@board.route('/login')
def login_page():
    next_url = request.args.get('next', '')
    id = request.form['id']
    password = request.form['password']

    return render_template('login.html')

@board.route('/login', methods=['POST'])
def login_process():

    id = request.form['id']
    password = request.form['password']

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
        sql = "SELECT `usn`, `id`, `email`, `update_time` FROM users WHERE `id`='%s' AND `password`='%s' LIMIT 1" % (id, password)

        print(sql)

        cursor.execute(sql)
        rows = cursor.fetchall()

        for row_data in rows:
            print('usn:[%s] id:[%s] email:[%s] update_time:[%s]' % (row_data[0], row_data[1], row_data[2], row_data[3]))

    finally:
        conn.close()

    return render_template('login.html')