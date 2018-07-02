
#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Feng ZHAO
@Date 2018/02/02
@Purpose Cron jobs 

ChangeLog
2018/07/02 Feng ZHAO Initial Draft
2018/07/02 Feng ZHAO Class PXB  debug comand = /usr/local/python/bin/python3 /www/python/biportal/manage.py crontab run 9da3a107c107d7271341ba543a223a78
'''

class Pxb():

    def __init__(self):
        self.utils = Utils()

    def main(self):

        accessTokenUrl = 'http://www.91pxb.com/api/AccessToken/Get'
        rootCompanyUrl = 'http://www.91pxb.com/api/Companies/SynchronizeRootCompany' 
        auth = {'appId': 'hHvKkSxRt113b690', 'appSecret': '98F2709A98B91FD3BEEFB32697DD144971246D0A'}
        header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}


        accessToken = self.getPxbAccessToken(accessTokenUrl, auth, header)
        if (accessToken['err'] == 0):
            header['ACCESS-TOKEN'] = accessToken['data']
            #rootCompany = getRootCompany()
            rootCompany = {'code': 'A001', 'organization_name': '培训宝'}
            updateReturn = self.updateRootCompany(rootCompanyUrl, rootCompany, header)

            print(updateReturn)
        else:
            print(accessToken['err'] + accessToken['data'])
        

        
    def getPxbAccessToken(self, url, post, header):
        return self.utils.apiCall(url, post, header)

    def updateRootCompany(self, url, post, header):
        return self.utils.apiCall(url, post, header)

    #def getRootCompany():


    #Public function for api call for pxb, maycour ...
    '''
    def apiCall(self, url, post, header):

        import urllib.request
        import urllib.parse
        import json
        post = json.dumps(post)
        post = bytes(post,'utf8')
        request = urllib.request.Request(url, post, header)
        result = urllib.request.urlopen(request).read()
        return json.loads(result)
    '''

class Utils():
    
    def apiCall(self, url, post, header):
        import urllib.request
        import urllib.parse
        import json
        post = json.dumps(post)
        post = bytes(post,'utf8')
        request = urllib.request.Request(url, post, header)
        result = urllib.request.urlopen(request).read()
        return json.loads(result)


pxb = Pxb()
pxb.main()
