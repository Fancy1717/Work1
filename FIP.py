# python3
import urllib.request as urllib2

# the source ip to fake
ipAddress = "4.4.4.4" 

# try to change the XFF in the header 
headers = {
    "X-Forwarded-For":ipAddress, 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}

# build a request throuth Request()
url = r'http://104.129.186.123:5000/iptest'
request = urllib2.Request(url, headers = headers)

# send the request and get the response
response = urllib2.urlopen(request)

# decode the response and print
html = response.read()
print(html.decode('gb2312'))
