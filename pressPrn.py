from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import pprint
import random
wp = Client('http://bellez.net/xmlrpc.php', 'bellez', 'qwerty123')

#priceInfo = open('tradeData', 'r')
#titleInfo = open('tradeTitle', 'r')
#redditInfo = open('redditdrawn', 'r')
#lordeInfo = open('LastData', 'r')
#titleData = open('titleData', 'r')
tacPrn = open('savTit','r')
savPrn = open('savPrn','r')
savTag = open('savTag','r')

for tag in savTag:
     pprint.pprint(tag)
for tac in tacPrn:
     pprint.pprint(tac)

for sav in savPrn:
     pprint.pprint(sav)
#for result in priceInfo:
#     pprint.pprint(result)

#for titles in titleInfo:
#     pprint.pprint(titles)
     
#for reddit in redditInfo:
#    pprint.pprint(reddit)

#for data in titleData:
#    pprint.pprint(data)

#for lorde in lordeInfo:
#    pprint.pprint(lorde)     
     
Posts = wp.call(GetPosts())
post = WordPressPost()
backPost = WordPressPost()
backPost.title = (tac)
backPost.content = (sav)
backPost.terms_names = {
     'post_tag': [tag],
     'category': ['porn']
}
backPost.post_status = 'publish'
wp.call(NewPost(backPost))

#post.title = (data)
#post.content = (lorde)

#post.terms_names = {
#     'post_tag': ['trademe', 'dataprocess', 'python', 
#                  'reddit', 'lastfm']}
#{'category' : ['trademe']}
#post.post_status = 'publish'
#wp.call(NewPost(post)) 
