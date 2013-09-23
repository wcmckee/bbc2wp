from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import pprint
import random
wp = Client('http://wcmckee.com/xmlrpc.php', 'trademe', 'qwerty123')

#priceInfo = open('tradeData', 'r')
#titleInfo = open('tradeTitle', 'r')
#redditInfo = open('redditdrawn', 'r')
#lordeInfo = open('LastData', 'r')
#titleData = open('titleData', 'r')
tacBbc = open('tacBbc','r')
savBbc = open('savBbc','r')

for tac in tacBbc:
     pprint.pprint(tac)

for sav in savBbc:
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
     'post_tag': ['python', 'dataprocess'],
     'category': ['news']
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
