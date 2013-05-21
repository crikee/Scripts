from bs4 import BeautifulSoup
import urllib

ids = []

f = open("foo.txt")              
line = f.readline()            
while line:
	ids.append(line.decode('utf-8').encode('gb2312'))
	print line                
	line = f.readline()
f.close()

#tem1 = raw_input("name=")
#tem2 = tem1.decode('utf-8')
#name = tem2.encode('gb2312')

cuowu = '%B4%ED%CE%F3%D2%B3'
#print cuowu
#fp = open('show_photos.htm','w+')

base_url = 'http://www.baidu.com/p/' 

count = 1
for id in ids :
	test_url = base_url + urllib.quote(id)[:-3] 
	test_url += '?from=tieba'
	res = urllib.urlopen(test_url)
	soup = BeautifulSoup(res)
	title = urllib.quote(soup.title.text.encode('gb2312'))
	#print title
	if(title == cuowu):
		print count
		print test_url
	count += 1
#fp.close()



