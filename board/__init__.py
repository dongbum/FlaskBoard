# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, url_for
from board.controller import *
from board.model import *

def print_settings(config):
    print('===================================================================')
    print('settings for flask-board')
    print('===================================================================')
    for key, value in config:
        print('%s=%s' % (key, value))
    print('===================================================================')

def not_found(error):
    return render_template('404.html'), 404

def server_error(error):
    err_msg = str(error)
    return render_template('500.html', err_msg=err_msg), 500

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

def create_app():
    flask_board_app = Flask(__name__, instance_relative_config=True)

    print('instance_path:[%s]' % flask_board_app.instance_path)

    from board.board_config import FlaskBoardConfig
    flask_board_app.config.from_object(FlaskBoardConfig)
    flask_board_app.config.from_pyfile('config.cfg', silent=True)
    print_settings(flask_board_app.config.items())

    try:
        db_address = flask_board_app.config['DB_ADDRESS']
        db_port = flask_board_app.config['DB_PORT']
        db_id = flask_board_app.config['DB_ID']
        db_password = flask_board_app.config['DB_PASSWORD']
        db_name = flask_board_app.config['DB_NAME']
    except ValueError:
        print("Cannot found DB connection info.")
        exit(1)

    # 로그 초기화
    from board.board_logger import Log
    log_filepath = os.path.join(flask_board_app.instance_path, flask_board_app.config['LOG_FILE_PATH'])
    Log.init(log_filepath=log_filepath)

    from board.board_blueprint import board
    flask_board_app.register_blueprint(board)

    flask_board_app.error_handler_spec['404'] = not_found
    flask_board_app.error_handler_spec['500'] = server_error

    flask_board_app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    return flask_board_app