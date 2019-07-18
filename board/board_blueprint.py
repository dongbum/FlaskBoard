# -*- coding: utf-8 -*-

from flask import Blueprint

board = Blueprint('bikeparking', __name__, template_folder='../templates', static_folder='../static')