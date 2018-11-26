
#def seach():
   # cx = "017759274803393121870:zu8mzk87c34"
    #gcse = document.createElement('script')
    #gcse.type = "text/javascript"
    #gcse.async = True
    #gcse.src = "https://cse.google.com/cse.js?cx=" + cx
    #s = document.getElementsByTagName('script')[0]
    #s.parentNode.insertBefore(gcse, s)


#import webbrowser

#def google_search(input):
 #   url= "https://www.google.com/search?ei=EMjyW7G-NMaagQbP2qmYCw&q={}".format(input)
#
 #   webbrowser.open(url, new=2, autoraise=False)
  #  newUrl = "http://schema.org/SearchResultsPage"
#
 #   webbrowser.open(newUrl, new=1)

#n = input("User: ")
#google_search(n)

import urllib.request
import urllib
import json
url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
query = input("Query:")
query = urllib.parse.urlencode( {'q' : query } )
response = urllib.request.urlopen (url + query ).read()
data = json.loads ( response.decode() )
results = data[ 'responseData' ][ 'results' ]
for result in results:
    title = result['title']
    url = result['url']
    print ( title + '; ' + url )