#!/usr/bin/python
#coding:utf-8

import markdown,yaml,os,time

'''
    cache = {
    
        'postlist':
    }

'''
cache = {}

class MD(object):
    def __init__(self,config):
        path = os.getcwd()
        self.path = path + '/' + config['path']
        self.pagesize = config['pagesize']

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

    # 分页 
    # 总共多少页
    # 
    def get_page(self, page=1):
        page = int(page)
        allpost = self.findall()
        length = len(allpost)
        pagenum = int(length/self.pagesize) + 1
        if pagenum > length: pagenum = length
        start_idx = (page - 1) * self.pagesize
        end_idx = page * self.pagesize
        page = allpost[start_idx : end_idx]
        return {'len': pagenum, '' 'page': page} 

    # 将文章按照时间排序
    def sort_by_time(self):
        pass

    # 清空缓存
    def flush(self):
        global cache
        cache = {}


if __name__ == '__main__':
    md = MD(config.CONFIG)
    # print md.findall()
    print md.get_page(1)
    # print md.sort_by_time()