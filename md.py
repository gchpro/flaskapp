#!/usr/bin/python
#coding:utf-8

import markdown,yaml,os,config

cache = {}

class MD(object):
    def __init__(self,config):
        path = os.getcwd()
        self.path = path + '/' + config['path']

    def find(self,filename):
        global cache
        if filename in cache: return cache[filename]
        try:
            path = self.path + '/' + filename + '.md'
            f = open(path, 'r')
        except:
            print 'Cant find %s.md in %s' % (filename, path)
            return {}

        header,body = f.read().split('===')
        header = yaml.load(header)
        body = markdown.markdown(body)
        data = header
        data.update({'body':body})
        data['filename'] = filename
        cache[filename] = data
        return data

    # 获取所有的文章，返回
    def findall(self):
        global cache
        postslist = os.listdir(self.path)
        print postslist
        for post in postslist:
            filename = post.split('.')[0]
            self.find(filename)

        return cache.values()

    # 将文章按照时间排序
    def sortposts(self):
        global cache
        1

if __name__ == '__main__':
    md = MD(config.CONFIG)
    print md.findall()