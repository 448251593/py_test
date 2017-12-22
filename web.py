import urllib2
 
request = urllib2.Request("https://www.toutiao.com/api/article/feed/?category=essay_joke&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1C5EAA30A41D12&cp=5A3A212DB1C25E1&_signature=PIbl2QAAZsJXFmLmLMPFQjyG5c")
response = urllib2.urlopen(request)
print response.read()
