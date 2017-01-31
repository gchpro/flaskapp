#!/usr/bin/python
#coding:utf-8

from flask import Flask
from md import MD
from routes import route

def create_app(mdconfig):
    app = Flask(__name__)
    md = init_md(mdconfig)
    add_route(app, md)
    return app

def init_md(mdconfig):
    md = MD(mdconfig)
    return md


def add_route(app, md):
    route(app, md)