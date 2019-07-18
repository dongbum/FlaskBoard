# -*- coding: utf-8 -*-

from flask import render_template
from board.board_blueprint import board

@board.route('/')
def index():
    return render_template('index.html')