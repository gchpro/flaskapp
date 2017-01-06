title: 测试代码
date: 2016-12-15 16:25:00
summary: 介绍了一个最小接口文件的组成

===

# 测试代码

这是一个最小接口文件，包含了proc,doproc两个方法


	#!usr/bin/python
	#coding:utf-8

	'''
		最小接口文件示例
	'''

	import g

	def proc(conn, data):
    	_res = doproc(conn,data)
    	conn.response(_res)
    	conn.send()

	def doproc(conn, data):
    	_res = {'s':1}
    	_res['d'] = 'Hello World!'
    	return _res
    


![img][./pic/pic.png]