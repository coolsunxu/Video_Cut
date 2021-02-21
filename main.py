

import sys
from QxtSpanSlider import QxtSpanSlider
from new_thread import new_thread
	
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import cv2
from pathlib import Path
 
 
class TestWindow(QWidget):
	def __init__(self):
		super(TestWindow, self).__init__()
		layout = QFormLayout(self)
		
		# 选择文件夹
		self.select_folder = QPushButton("选择文件夹")
		self.select_folder.clicked.connect(self.choose_paths)
		self.video_paths = QLineEdit()
		
		self.jump = QPushButton("跳转")
		self.jump.clicked.connect(self.push_jump)
		self.jump_index = QLineEdit('0')
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(self.select_folder)
		hbox4.addWidget(self.video_paths)
		hbox4.addWidget(self.jump)
		hbox4.addWidget(self.jump_index)
		layout.addRow(hbox4)
		
		# 保存文件夹
		self.save_folder = QPushButton("保存文件夹")
		self.save_folder.clicked.connect(self.save_paths)
		self.save_paths = QLineEdit()
		
		self.next = QPushButton("下一个")
		self.next.clicked.connect(self.push_next)
		self.next_index = QLineEdit('0')
		
		hbox5 = QHBoxLayout()
		hbox5.addWidget(self.save_folder)
		hbox5.addWidget(self.save_paths)
		hbox5.addWidget(self.next)
		hbox5.addWidget(self.next_index)
		layout.addRow(hbox5)
		
		# 计数用
		self.index = 0
		
		
		# 读取彩色图片
		self.label = QLabel()
		self.img_src = cv2.imread("1.jpg")
		self.img_src = cv2.cvtColor(self.img_src,cv2.COLOR_BGR2RGB)
		# 读取label宽高
		self.label_width = 640
		self.label_height = 360
 
		# 将图片转换为QImage
		self.temp_imgSrc = QImage(self.img_src, self.img_src.shape[1], self.img_src.shape[0],self.img_src.shape[1]*3, QImage.Format_RGB888)
		# 将图片转换为QPixmap方便显示
		self.pixmap_imgSrc = QPixmap.fromImage(self.temp_imgSrc).scaled(self.label_width, self.label_height)
 
		# 使用label进行显示
		self.label.setPixmap(self.pixmap_imgSrc)
		layout.addRow(self.label)
		
		self.label1 = QLabel('0')
		self.label2 = QLabel('0')
		self.label3 = QLabel('起始帧:')
		self.label4 = QLabel('结束帧:')
		self.label7 = QLabel('时长:')
		self.label8 = QLabel('0')
		
		
		hbox1 = QHBoxLayout()
		hbox1.addStretch(1)
		hbox1.addWidget(self.label3)
		hbox1.addWidget(self.label1)
		hbox1.addWidget(self.label4)
		hbox1.addWidget(self.label2)
		hbox1.addWidget(self.label7)
		hbox1.addWidget(self.label8)
		hbox1.addStretch(1)
		layout.addRow(hbox1)

		self.slider = QxtSpanSlider()
		self.slider.setSpan(0,0)
		self.slider.setRange(0, 100)
		color = QColor(Qt.blue).lighter(150)
		self.slider.setGradientLeftColor(color)
		self.slider.setGradientRightColor(color)
		
		self.slider.lowerPositionChanged.connect(lambda:self.get_index(1))
		self.slider.upperPositionChanged.connect(lambda:self.get_index(2))
		
		layout.addRow(self.slider)
		
		# 帧按钮
		self.button2 = QPushButton() 
		self.button2.setText("前进")
		self.button2.clicked.connect(self.forward)
		
		self.button3 = QPushButton() 
		self.button3.setText("后退")
		self.button3.clicked.connect(self.back)
		
		self.button2.setAutoRepeat(True)
		self.button2.setAutoRepeatDelay(200)
		self.button2.setAutoRepeatInterval(20)
		
		self.button3.setAutoRepeat(True)
		self.button3.setAutoRepeatDelay(200)
		self.button3.setAutoRepeatInterval(20)
		
		hbox = QHBoxLayout()
		hbox.addWidget(self.button2)
		hbox.addWidget(self.button3)
		layout.addRow(hbox)
		
		
		# 保存视频
		self.label5 = QLabel('实验三:')
		layout.addRow(self.label5)
		
		self.button4 = QPushButton() 
		self.button4.setText("组装装置")
		self.button4.clicked.connect(lambda:self.save("组装装置",3))
		
		self.button5 = QPushButton() 
		self.button5.setText("缩小实像")
		self.button5.clicked.connect(lambda:self.save("缩小实像",3))
		
		self.button6 = QPushButton() 
		self.button6.setText("放大实像")
		self.button6.clicked.connect(lambda:self.save("放大实像",3))
		
		self.button7 = QPushButton() 
		self.button7.setText("记录数据")
		self.button7.clicked.connect(lambda:self.save("记录数据",3))
		
		self.button8 = QPushButton() 
		self.button8.setText("整理器材")
		self.button8.clicked.connect(lambda:self.save("整理器材",3))
		
		self.button9 = QPushButton() 
		self.button9.setText("其他动作")
		self.button9.clicked.connect(lambda:self.save("其他动作",3))
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(self.button4)
		hbox2.addWidget(self.button5)
		hbox2.addWidget(self.button6)
		hbox2.addWidget(self.button7)
		hbox2.addWidget(self.button8)
		hbox2.addWidget(self.button9)
		layout.addRow(hbox2)
		
		self.label6 = QLabel('实验四:')
		layout.addRow(self.label6)
		
		self.button10 = QPushButton() 
		self.button10.setText("挂测力计")
		self.button10.clicked.connect(lambda:self.save("挂测力计",4))
		
		self.button11 = QPushButton() 
		self.button11.setText("记录数据")
		self.button11.clicked.connect(lambda:self.save("记录数据",4))
		
		self.button12 = QPushButton() 
		self.button12.setText("加挂钩码")
		self.button12.clicked.connect(lambda:self.save("加挂钩码",4))
		
		self.button13 = QPushButton() 
		self.button13.setText("整理器材")
		self.button13.clicked.connect(lambda:self.save("整理器材",4))
		
		self.button14 = QPushButton() 
		self.button14.setText("其他动作")
		self.button14.clicked.connect(lambda:self.save("其他动作",4))
		
		hbox3 = QHBoxLayout()
		hbox3.addWidget(self.button10)
		hbox3.addWidget(self.button11)
		hbox3.addWidget(self.button12)
		hbox3.addWidget(self.button13)
		hbox3.addWidget(self.button14)
		layout.addRow(hbox3)
		
	# 选择文件夹
	def choose_paths(self):
		directory = QtWidgets.QFileDialog.getExistingDirectory(None,"选取文件夹","D:/programming/other/python/video_data/")
		self.video_directory = directory
		self.video_paths.setText(directory)
		self.get_video_name()
		self.index = 0 # 初始化
		self.next_index.setText(str(self.index+1)+'/'+str(self.len))
		
		self.set_slider()
		
	# 保存文件夹
	def save_paths(self):
		directory = QtWidgets.QFileDialog.getExistingDirectory(None,"选取文件夹","D:/programming/other/python/video_data/")
		self.save_directory = directory
		self.save_paths.setText(directory)
		
	# 读取视频名
	def get_video_name(self):
		self.data_root = Path(self.video_directory)
		self.all_video_paths = list(self.data_root.glob('*'))
		self.all_video_paths = [str(i) for i in self.all_video_paths]
		self.len = len(self.all_video_paths)
		#print(self.all_video_paths)
	
	# 点击下一个
	def push_next(self):
		if(self.index<self.len):
			self.index = self.index + 1
			self.set_slider()
		else:
			print('已结束')
			
	# 点击跳转
	def push_jump(self):
		self.index = int(self.jump_index.text())
		if(self.index<self.len):
			self.index = self.index - 1
			self.set_slider()
		else:
			print('不在范围内，请重新输入')
			
	# 设置进度条
	def set_slider(self):
		self.current_path = self.all_video_paths[self.index]
		self.next_index.setText(str(self.index+1)+'/'+str(self.len))
		print(self.current_path)
		
		# 读取视频
		self.cap = cv2.VideoCapture(self.current_path)
		self.fps = self.cap.get(cv2.CAP_PROP_FPS)
		
		self.length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
		self.slider.setSpan(0,0)
		self.slider.setRange(0, self.length-24)
		
	def get_index(self,tag):
		
		print(self.slider.lowerValue,self.slider.upperValue)
		if(tag==1):
			self.keys_frame = self.slider.lowerValue
			self.label1.setText(str(self.slider.lowerValue))
		else: 
			self.keys_frame = self.slider.upperValue
			self.label2.setText(str(self.slider.upperValue))
		self.show_image()
		
		
	def show_image(self):
		self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.keys_frame)  # keys_frame为关键帧的序号
		ret, frame = self.cap.read()
			
		self.img_src = frame
		self.img_src = cv2.cvtColor(self.img_src,cv2.COLOR_BGR2RGB)
		
		self.temp_imgSrc = QImage(self.img_src, self.img_src.shape[1], self.img_src.shape[0],self.img_src.shape[1]*3, QImage.Format_RGB888)
		# 将图片转换为QPixmap方便显示
		self.pixmap_imgSrc = QPixmap.fromImage(self.temp_imgSrc).scaled(self.label_width, self.label_height)
 
		# 使用label进行显示
		self.label.setPixmap(self.pixmap_imgSrc)
		
		self.label8.setText(str(int((self.slider.upperValue-self.slider.lowerValue)/self.fps)))
		
	def save(self,kind,tag):
		self.new_thread = new_thread(self.slider.lowerValue,self.slider.upperValue,kind,self.current_path,self.save_directory,tag)
		self.new_thread.start()
			   
		
	def forward(self):
		self.slider.setLowerPosition(self.slider.lowerPosition+1)
		self.keys_frame = self.slider.lowerPosition
		self.label1.setText(str(self.slider.lowerPosition))
		print(self.slider.lowerValue,self.slider.upperValue)
		self.show_image()
		self.label8.setText(str(int((self.slider.upperValue-self.slider.lowerValue)/self.fps)))
		
	def back(self):
		self.slider.setUpperPosition(self.slider.upperPosition-1)
		self.keys_frame = self.slider.upperPosition
		self.label2.setText(str(self.slider.upperPosition))
		print(self.slider.lowerValue,self.slider.upperValue)
		self.show_image()
		self.label8.setText(str(int((self.slider.upperValue-self.slider.lowerValue)/self.fps)))
		
		
			
def show_w():
	
	app = QApplication(sys.argv)
 
	w = TestWindow() 
 
	w.resize(500, 500) 
	w.move(500, 100) 
	w.setWindowTitle('VideoCut')
	w.show()
	
 
	sys.exit(app.exec_())
	
	
if __name__ == '__main__':
 
	show_w()
	
	# 33
	#os.system('ffmpeg -y -i 1.mp4 -ss 0 -t 360 -acodec copy -vcodec copy -async 1 2.mp4')
	
	
