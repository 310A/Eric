########### Python 2.7 #############
import httplib, urllib, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'cba30787e3664a648e2d439f9ad9bee7',
}

params = urllib.urlencode({
    # Query parameter
    'q': 'hello',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/luis/v2.0/apps/9d99a7d5-2564-4c02-b91e-54d6d9c3c076?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    print(json.loads(data)['topScoringIntent']['intent'])
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################