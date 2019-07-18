# -*- coding: utf-8 -*-

from flask import render_template
from board.board_blueprint import board

@board.route('/login')
def login():
    return render_template('login.html')