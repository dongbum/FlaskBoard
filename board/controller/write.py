# -*- coding: utf-8 -*-

import pymysql
from flask import render_template, request, current_app
from board.board_blueprint import board

@board.route('/write')
def write():
    return render_template('write.html')