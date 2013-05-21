from bs4 import BeautifulSoup
import urllib


tem1 = raw_input("name=")
tem2 = tem1.decode('utf-8')
name = tem2.encode('gb2312')

fp = open('show_photos.htm','w+')

base_url = 'http://tieba.baidu.com/f/search/adv' 

#qw = ['%D5%D5','%d7%d4%b1%ac','%d7%d4%c6%d8','%b1%ac%d5%d5','%c6%d8%d5%d5','%c6%d8']
qw = ['%d7%d4%b1%ac','%d7%d4%c6%d8']

for keyword in qw :
	test_url = 'http://tieba.baidu.com/f/search/ures?kw=&qw='+ keyword + '&rn=30&un=' + urllib.quote(name) + '&sm=1&sd=&ed=&pn='
	print '!!' + test_url
	pn = 1 ;
	while(pn<40):
		res = urllib.urlopen(test_url + str(pn))
		soup = BeautifulSoup(res);
		photos = soup.find_all('img','p_pic');
		for photo in photos :
			print pn
			print photo['src']
			fp.write('<img class="p" src="' +  photo['src']	+ '"/>' + '\n')
			
		pn += 1 

fp.close()
