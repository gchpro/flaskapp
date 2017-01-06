#!/usr/bin/python
#coding:utf-8

import markdown,yaml,os,config,time

cache = {}

class MD(object):
    def __init__(self,config):
        path = os.getcwd()
        self.path = path + '/' + config['path']

    def find(self,filename):
        global cache
        filename = unicode(filename)
        if filename in cache: return cache[filename]
        try:
            path = self.path + '/' + filename + '.md'
            f = open(path, 'r')
        except:
            print 'Cant find %s.md in %s' % (filename, path)
            return {}

        header,body = f.read().split('===')
        header = yaml.load(header)
        # body.decode('utf8')
        body = unicode(body.decode('utf8'))
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
        # print postslist
        for post in postslist:
            if not post.endswith('.md'): continue
            filename = (post.split('.')[0]).decode('utf8')
            self.find(filename)

        allpost = cache.values()
        allpost.sort(key=lambda x: x['date'], reverse=True)
        return allpost

    # 将文章按照时间排序
    def sort_by_time(self):
        pass

if __name__ == '__main__':
    md = MD(config.CONFIG)
    print md.findall()
    # print md.sort_by_time()