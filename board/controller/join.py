# -*- coding: utf-8 -*-

from flask import render_template, request
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

    return render_template('join.html')