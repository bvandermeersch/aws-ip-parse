import json
import urllib2

resource_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
response = urllib2.urlopen(resource_url)
data = json.load(response)

for prefix in data['prefixes']:
        print prefix['ip_prefix'] + " #" + prefix['region'] + " " + prefix['service']
