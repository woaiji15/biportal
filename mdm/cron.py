
#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Feng ZHAO
@Date 2018/07/02
@Purpose Cron jobs 

ChangeLog
2018/07/02 Feng ZHAO Initial Draft
2018/07/02 Feng ZHAO Class PXB & Utils  debug comand = /usr/local/python/bin/python3 /www/python/biportal/manage.py crontab run 9da3a107c107d7271341ba543a223a78
2018/07/04 Feng ZHAO Using Django model to get queryset 
'''

class Pxb():

    def __init__(self):
        from mdm.models import Company 
        from django.core import serializers

        self.company = Company
        self.utils = Utils()

        self.serializers = serializers
    def main(self):

        accessTokenUrl = 'http://www.91pxb.com/api/AccessToken/Get'
        rootCompanyUrl = 'http://www.91pxb.com/api/Companies/SynchronizeRootCompany' 
        auth = {'appId': 'hHvKkSxRt113b690', 'appSecret': '98F2709A98B91FD3BEEFB32697DD144971246D0A'}
        header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}


        accessToken = self.getPxbAccessToken(accessTokenUrl, auth, header)
        if (accessToken['err'] == 0):
            header['ACCESS-TOKEN'] = accessToken['data']
            rootCompany = self.getRootCompany()

            for c in rootCompany:
                company = []
                company.append({
                    'code': c['code'],
                    'organization_name': c['name'],
                })
                print(company)
                #updateReturn = self.updateRootCompany(rootCompanyUrl, company, header)

        else:
            print(accessToken['err'] + accessToken['data'])
        

        
    def getPxbAccessToken(self, url, post, header):
        return self.utils.apiCall(url, post, header)

    def updateRootCompany(self, url, post, header):
        return self.utils.apiCall(url, post, header)

    def getRootCompany(self):
        companies = self.company.objects.filter(status=2).values('code', 'name')

        return companies


class Utils():
    
    def apiCall(self, url, post, header):
        import urllib.request
        import urllib.parse
        #post = json.dumps(post)
        post = self.json(post, 'encode')
        post = bytes(post,'utf8')
        request = urllib.request.Request(url, post, header)
        result = urllib.request.urlopen(request).read()
        #return json.loads(result)
        return self.json(result, 'decode')
    
    def json(self, data, jsonType):
        import json
        if (jsonType == 'encode'):
            return json.dumps(data)
        elif (jsonType == 'decode'):
            return json.loads(data)
        else:
            return false

def pxb():
    pxb = Pxb()
    pxb.main()
