#coding:utf-8
import os
import platform
import tkinter
import time
import hashlib
from tkinter.constants import END, LEFT, RIDGE, RIGHT, SW, TOP, Y


LOG_LINE_NUM = 0

class MY_GUI():
	def __init__(self,init_window_name):
		self.init_window_name = init_window_name



	#设置窗口
	def set_init_window(self):
		self.init_window_name.title("文本处理工具_v1.2")           #窗口名
		#self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置

		# 获取屏幕宽度和高度
		scn_w, scn_h = self.init_window_name.maxsize()
		curWidth = scn_w/2# 1680
		curHight = scn_h/2#681
		print(curWidth)
		print(curHight)

		# 计算中心坐标
		cen_x = (scn_w- curWidth) / 2;
		cen_y = (scn_h-curHight) / 2;


		# 设置窗口初始大小和位置
		size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)
		self.init_window_name.geometry(size_xy)

		# self.init_window_name.geometry('1068x681+10+10')
		#self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
		#self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
		#标签
		self.init_data_label = tkinter.Label(self.init_window_name, text="待处理数据")
		self.init_data_label.grid(row=0, column=0);

		self.init_data_Text = tkinter.Text(self.init_window_name,height=10)  #原始数据录入框
		self.init_data_Text.insert(1.0,"11111")
		self.init_data_Text.grid(row=1, column=0);

		#文本框
		self.log_label = tkinter.Label(self.init_window_name, text="日志")
		self.log_label.grid(row=2, column=0);
		self.log_data_Text = tkinter.Text(self.init_window_name,height= 10)  # 日志框
		self.log_data_Text.insert(1.0,"2222")
		self.log_data_Text.grid(row=3, column=0, padx=5);



		#按钮
		self.str_trans_to_md5_button = tkinter.Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
		self.str_trans_to_md5_button.grid(row=1, column=1, padx=5);

		self.result_data_label = tkinter.Label(self.init_window_name, text="输出结果")
		self.result_data_label.grid(row=0, column=2,padx=5);
		self.result_data_Text = tkinter.Text(self.init_window_name ,height= 10)  #处理结果展示
		self.result_data_Text.insert(1.0,"3333")
		self.result_data_Text.grid(row=1, column=2,padx=5);










	#功能函数
	def str_trans_to_md5(self):
		src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
		print("src =",src)
		if src:
			try:
				myMd5 = hashlib.md5()
				myMd5.update(src)
				myMd5_Digest = myMd5.hexdigest()
				#print(myMd5_Digest)
				#输出到界面
				self.result_data_Text.delete(1.0,END)
				self.result_data_Text.insert(1.0,myMd5_Digest)
				self.write_log_to_Text("INFO:str_trans_to_md5 success")
			except:
				self.result_data_Text.delete(1.0,END)
				self.result_data_Text.insert(1.0,"字符串转MD5失败")
		else:
			self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


	#获取当前时间
	def get_current_time(self):
		current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		return current_time



	#日志动态打印
	def write_log_to_Text(self,logmsg):
		global LOG_LINE_NUM
		current_time = self.get_current_time()
		logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
		if LOG_LINE_NUM <= 7:
			self.log_data_Text.insert(END, logmsg_in)
			LOG_LINE_NUM = LOG_LINE_NUM + 1
		else:
			self.log_data_Text.delete(1.0,2.0)
			self.log_data_Text.insert(END, logmsg_in)


def gui_start():
	init_window = tkinter.Tk()              #实例化出一个父窗口
	ZMJ_PORTAL = MY_GUI(init_window)
	# 设置根窗口默认属性
	ZMJ_PORTAL.set_init_window()

	init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示



if __name__ == '__main__':
	gui_start()

