#!/usr/bin/python
#coding:utf-8

from app import create_app
import config

app = create_app(config.MDCONFIG)
