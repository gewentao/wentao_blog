import urllib2
import json

def get_city_by_ip(ip = '0.0.0.0'):
	url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
        #url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip=' + ip
        location = {}
        try:
            response = urllib2.urlopen(url)
        except urllib2.URLError,e:
            return location
        result = json.loads(response.read())
	#location['country'] = result['country']
	#location['province'] = result['province']
	location['city'] = result['data']['city']
	return location
