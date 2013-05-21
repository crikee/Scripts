import urllib 
from bs4 import BeautifulSoup

tem = input("pn=")
lp = int(tem)
fp = open('baidu_billboard2.txt','w+')

while lp > 10 :
	pn = str((lp-1)*50)
	base_url = 'http://tieba.baidu.com/f/good?kw=billboard%BA%F3%BB%A8%D4%B0&cid=0&tp=0&pn=0'
	base_url += pn 
	b_res = urllib.urlopen(base_url) 
	b_soup = BeautifulSoup(b_res)
	thread_list = b_soup.find_all('div','threadlist_text threadlist_title j_th_tit  notStarList ')
	thread_url_arr = [] ;

	for thread in thread_list :
		thread_url_arr.append('http://tieba.baidu.com' + thread.a['href'] + '?see_lz=1')

	for t_url in thread_url_arr :
		print t_url
		t_res = urllib.urlopen(t_url)
		t_soup = BeautifulSoup(t_res)
		t_tile = t_soup.find('h1','core_title_txt').text
		fp.write(t_tile.encode('utf-8') + '\n')
		fp.write('==========================================================================' + '\n')
		#print t_tile
		#print '==============================================================================='
		floors = t_soup.find_all('div','p_content')
		index = 1 
		for floor in floors :
			fp.write('[' + str(index) + ']')
			fp.write(floor.cc.text.encode('utf-8') + '\n')
			index += 1  
			#print floor.cc.text
			#print '==============================================================================='
		fp.write('\n' + '\n')
		#break
	lp -= 1 

fp.close()