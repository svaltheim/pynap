import Shodan

def ShodanTest():
  try:
     ShodankeyString = "P9kLzRulaTpm7f3NzkNJsZmqrks1Whld"
     results = ShodanApi.search("apache")
     for result in results['matches']:
        print "IP: %s" % result["ip_str"]
        print result['data']
        print ''
  except shodan.APIError, e:
      print "Error %s" % e

if __name__ == "__main__":
    ShodanTest()
