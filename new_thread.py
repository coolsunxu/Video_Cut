
from PyQt5.QtCore import *
from time import strftime,gmtime
import os
import cv2
from pathlib import Path

class new_thread(QThread):
 
	def __init__(self,a,b,kind,read_path,save_path,tag):
		super(new_thread, self).__init__()
		
		self.ex_3 = ['组装装置','缩小实像','放大实像','记录数据','整理器材','其他动作']
		self.ex_4 = ['挂测力计','记录数据','加挂钩码','整理器材','其他动作']
		self.fps = cv2.VideoCapture(read_path).get(cv2.CAP_PROP_FPS)
		self.a = int(float(a)/self.fps)
		self.b = int(float(b)/self.fps)
		self.kind = kind
		self.read_path = read_path
		self.save_path = save_path
		self.tag = tag
 
	def run(self):
		if(self.tag==3):
			self.final_path = self.save_path+'/ex_3/'+str(self.ex_3.index(self.kind)+1)+'/'
		else:
			self.final_path = self.save_path+'/ex_4/'+str(self.ex_4.index(self.kind)+1)+'/'
		Path(self.final_path).mkdir(parents=True,exist_ok=True)
		name = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
			
		#os.system('ffmpeg -y -i '+self.read_path+' -ss '+str(self.a)+' -t '+str(self.b-self.a)+' -acodec copy -vcodec copy -async 1 '+self.final_path+name+'.mp4')
		os.system('ffmpeg -y -i '+self.read_path+' -ss '+str(self.a)+' -t '+str(self.b-self.a)+' -ab 56k -ar 44100 -b:v 2200k -r '+str(self.fps)+' '+self.final_path+name+'.avi')
		print("时间戳:{}-{}属于类别：{},保存为{}".format(self.a,self.b,self.kind,name+'.avi'))
