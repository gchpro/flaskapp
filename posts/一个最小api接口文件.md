title: 一个最小api接口文件
date: 2016-12-18 16:25:00
summary: 介绍了一个最小接口文件的组成

===

# 一个最小api接口文件

这是一个最小接口文件，包含了proc,doproc两个方法

```python
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
    
```

```javascript
var local = 0
function(data){
  console.log(data);
}
```

```java
public class Hello(){
  public static void main(String args){
    System.out.println('Hello World!');
  }
}
```

![img][./pic/pic.png]