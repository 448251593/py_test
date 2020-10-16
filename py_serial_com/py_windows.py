# -*- coding: utf-8 -*-
import os,re;
import tkinter
from tkinter import messagebox

def but1_cb():
	# tkinter.Message("Hello Python", "Hello Runoob")
	tkinter.messagebox.askokcancel('警告', 'hello')


def window_start():
	wd1 = tkinter.Tk()
	wd1.title("bcg test windows")

	sw = wd1.winfo_screenwidth()#得到屏幕宽度
	sh = wd1.winfo_screenheight()#得到屏幕高度
	ww = 600
	wh = 400

	#窗口宽高为100
	x = (sw-ww) / 2
	y = (sh-wh) / 2


	wd1.geometry("%dx%d+%d+%d" %(ww,wh,x,y));

	frame1 = tkinter.Frame(wd1, background='pink')
	frame2 = tkinter.Frame(wd1, background="yellow")
	frame3 = tkinter.Frame(wd1, background="red")

	but1 = tkinter.Button(frame1, text="1", command=but1_cb ,borderwidth=2, width=8)
	but1.pack(side= tkinter.LEFT,padx=10)#padx 表示 左右都是 同样间距
	but2 = tkinter.Button(frame1, text="2", command=but1_cb,borderwidth=2, width=8)
	but2.pack(side= tkinter.LEFT)
	but3 = tkinter.Button(frame1, text="3", command=but1_cb,borderwidth=2, width=8)
	but3.pack(side= tkinter.LEFT,padx=10)
	but4 = tkinter.Button(frame1, text="4", command=but1_cb,borderwidth=2, width=8)
	but4.pack(side= tkinter.LEFT)

	#
	text1 = tkinter.Text(frame2)
	text1.pack(side="left", fill=tkinter.X)
	# text1.grid(column=0,row=0)

	sb_text = tkinter.Scrollbar(frame2)
	sb_text.pack(side="left", fill=tkinter.Y)
	# sb_text.grid(column=1,row=0)

	sb_text.config(command=text1.yview)


	label2= tkinter.Label(frame3,text="Label222",background="green")
	label2.pack()


	# frame1.grid(row=0,column=0)
	# frame2.grid(row=1,column=0)
	# frame3.grid(row=2,column=0)
	# frame1.pack(side= tkinter.BOTTOM)
	frame2.pack()
	frame1.pack(side= tkinter.BOTTOM,pady=3)
	frame3.pack(side= tkinter.BOTTOM, fill=tkinter.X)

	# 进入消息循环
	wd1.mainloop()










