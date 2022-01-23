"""
The flask application package.
"""

from flask import Flask
import pymysql
app = Flask(__name__)

import RandomConnectionSolution.views
