# -*- coding: utf-8 -*-

from flask import session, redirect, url_for
from board.board_blueprint import board

@board.route('/logout')
def logout():
    session.clear()

    return redirect(url_for('.list'))