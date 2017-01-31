from mongoengine import *

kwargs = {}
# kwargs['name'] = 'test'
kwargs['host'] = '10.0.0.7'
kwargs['port'] = 27017
kwargs['username'] = 'root'
kwargs['password'] = 'iamciniao'
kwargs['authentication_source'] = 'admin'

print "kwargs",kwargs
connect(db='test',**kwargs)

class Post(Document):
    post = StringField(max_length=140)

post = Post(post='hello mongoengine')
post.save()

