from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib
import urllib2
register_openers()

def upload(fileName):
    datagen, headers = multipart_encode({"file": open("D:\\software\\java\\jpg\\%s"%fileName, "rb")})
    baseurl = "https://pcs.baidu.com/rest/2.0/pcs/file?"
    args = {
        "method": "upload",
        "access_token": "1.a6b7dbd428f731035f771b8d15063f61.86400.1292922000-2346678-124328",
        "path": "/apps/ResourceSharing/%s"%fileName
    }
    encodeargs = urllib.urlencode(args)
    url = baseurl + encodeargs

    print(url)

    request = urllib2.Request(url, datagen, headers)
    result = urllib2.urlopen(request).read()
    print(result)

upload("123.jpg")