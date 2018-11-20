#coding:utf-8
import time,os,re,urllib,urllib2,hashlib,sys;
import matplotlib.pyplot as plt

#labels='frogs','hogs','dogs','logs'
#sizes=15,20,45,10
#colors='yellowgreen','gold','lightskyblue','lightcoral'
#explode=0,0.1,0,0
#
#
#plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
#plt.axis('equal')
#plt.show()
#print("after 3s  exit\n");
#time.sleep(3);


def  test():
	
	plt.rcParams['font.sans-serif'] = ['SimHei'];#用来正常显示中文标签
	plt.rcParams['axes.unicode_minus'] = False;#用来正常显示负号
	#plt.xticks(x,xtk,size=12,rotation=50);#设置字体大小和字体倾斜度
	plt.xlabel(u'城市');# x轴标签
	plt.ylabel(u'数量');
	plt.title(u'朋友所在城市');# 图的名称
	plt.legend();# 正常显示标题
	plt.show();# 显示图像
if __name__ == '__main__':
	test();
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	