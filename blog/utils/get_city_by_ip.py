import urllib2
import json

def get_city_by_ip(ip = '0.0.0.0'):
	url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
	response = urllib2.urlopen(url)
	result = json.loads(response.read())
	city = result['data']['city']
	return city
