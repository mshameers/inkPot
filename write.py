#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import math
from time import sleep 


class Write(QWidget):
	def __init__(self, parent=None):
		super(Write, self).__init__(parent)
#initialization		
		self.fontSize = self.appheight/2
		self.font = QFont('Andica Basic',self.fontSize)
		self.fontMetrics = QFontMetrics(self.font)
		self.data = '   '
		self.names ={}
		self.fontRect = self.fontMetrics.boundingRect(self.data)
		#self.setFixedSize(QSize(self.appWidth,self.appheight))
		self.showFullScreen()
		#self.setFixedSize(QSize(self.appWidth-30,self.appheight-120))
		self.startWriting = 0
		self.checkValue = []
		self.check = [0,1,2,3,4,5,6,7,8,9,10]
		self.penWidth = self.fontSize/5
		self.penColor = QColor(39,40,26)#(168,206,50)#(30, 144,255)
		self.image = QImage()
		self.setAcceptDrops(True)
		
#right click to start writing, left click to delete points
	def mousePressEvent(self, event):
		
		if event.button() == Qt.LeftButton :
			self.lastPoint = event.pos()
			mouse = QPoint( event.pos().x(),  event.pos().y())
			if self.names[self.childAt(event.pos())] == 0:
				self.startWriting = 1
				self.checkValue = []
			else:
				pass
			self.child = self.childAt(event.pos())
			if self.child in self.names:
				try:
					self.index = self.names.index(self.child)
					self.names.remove(self.child) 
				except:
					pass
			if not self.child:
				return
		else:
			
			self.dlg = QDialog()
			reply = QMessageBox.question(self, "Delete the stored points ?", "If Yes, return yes button else return No button",QMessageBox.Yes|QMessageBox.Cancel)
			if reply == QMessageBox.Yes:
				#print self.line1,self.filePath
				#with open(self.filePath,"r") as a_file:
				file(self.filePath, 'w').writelines([l for l in file(self.filePath).readlines() if '-'+self.lineNo+',' not in l])
					#index = line.find('-'+self.lineNo+',')
					#lines =   a_file.readlines()
					#print self.lineNo,lines.index(self.lineNo)
					#lines.remove(self.lineNo)
				#with open(self.filePath,"w") as a_file:
					#for item in lines:
					#	a_file.write(item)
			self.update()
				#print lines,'yes'
			return
					
#check the mouse move path, ensure it in order else stop write				
	def mouseMoveEvent(self, event):
		
		if (event.buttons() & Qt.LeftButton) and self.startWriting == 1:
			self.drawLineTo(event.pos())
			
		if self.childAt(event.pos()):
			if self.names[self.childAt(event.pos())] not in self.checkValue:
				self.checkValue.append(self.names[self.childAt(event.pos())])
			if self.checkValue != self.check[:self.names[self.childAt(event.pos())]+1] and self.startWriting == 1:
				self.startWriting = 0
				self.splash('check')
				"""dlg = QDialog()
				dlg.setWindowFlags(Qt.FramelessWindowHint)
				label =QLabel(dlg)
				label.setGeometry(QRect(90, 30, 300, 300))
				label.setPixmap(QPixmap("image/check.png"))
				if dlg.exec_():
					QTimer.singleShot(6000, dlg.quit)"""
				print self.checkValue,'order incorrect',self.check[:self.names[self.childAt(event.pos())]+1]
			else:
				pass
			
				self.countNo = self.names[self.childAt(event.pos())]+1
				self.swapNames = self.swap_dic(self.names)
				self.swapNameLabel = self.swapNames.get(self.names[self.childAt(event.pos())]+1)
				self.swapNameLabel1 = self.swapNames.get(self.names[self.childAt(event.pos())])
				if self.startWriting == 1:
					if len(self.names) >= self.countNo+1:
						#print len(self.names),self.countNo-2
						self.swapNameLabel.setPixmap(QPixmap('image/'+str(self.countNo)+'blue.png').scaled(35,35,Qt.KeepAspectRatioByExpanding))
					else:
						self.splash('splash')
						self.startWriting = 0
						"""
						print 'super'
						dlg = QDialog()
						label =QLabel(dlg)
						label.setGeometry(QRect(90, 30, 300, 300))
						label.setPixmap(QPixmap("image/splash.png"))
						if dlg.exec_():
							QTimer.singleShot(6000, dlg.quit)
							print 'ok'
							"""
				self.swapNameLabel1.setPixmap(QPixmap('image/'+str(self.countNo-1)+'orange.png').scaled(35,35,Qt.KeepAspectRatioByExpanding))
				#print self.swapNameLabel,'swapname'				
				
		else:
			pass
#when relesing mouseclick draw line	
	def mouseReleaseEvent(self, event):
		if event.button() == Qt.LeftButton and self.startWriting == 1:
			self.drawLineTo(event.pos())
			
#display the character 		
	def paintEvent(self, event):
		self.painter = QPainter(self)
		self.path = QPainterPath()
		self.path.addText(QPointF(self.width()/2-((self.fontRect.width()/2)+200),self.height()/2+self.fontSize/5),self.font,self.data)
		rectangle = self.path.boundingRect()
		self.painter.drawImage(rectangle, self.image,rectangle)
		self.path.addRect(0,0,self.width(),self.height())
		self.painter.setPen(QPen(QColor(122, 163, 39), 1,Qt.SolidLine,Qt.FlatCap, Qt.MiterJoin))
		self.painter.setBrush(QColor(223,216,174))#(QColor(180, 71, 132))
		self.painter.drawPath(self.path)
		self.painter.strokePath(self.path,QPen(Qt.darkCyan))
		#self.setAcceptDrops(True)
		self.painter.end()
		
	def resizeEvent(self, event):
		
		if self.width() > self.image.width() or self.height() > self.image.height():
			newWidth = max(self.width() + 128, self.image.width())
			newHeight = max(self.height() + 128, self.image.height())
			self.resizeImage(self.image, QSize(newWidth, newHeight))
			self.update()
		super(Write, self).resizeEvent(event)

	def resizeImage(self, image, newSize):
		if image.size() == newSize:
			return
		newImage = QImage(newSize, QImage.Format_RGB32)
		newImage.fill(qRgb(255, 255, 255))
		painter = QPainter(newImage)
		painter.drawImage(QPoint(0, 0), image)
		self.image = newImage
		self.newSize = newSize
#paint the mouse path with the brush, called when mouse movements
	def drawLineTo(self, endPoint):
		painter = QPainter(self.image)
		painter.setPen(QPen(self.penColor, self.penWidth,Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
		painter.drawLine(self.lastPoint, endPoint)
		rad = (self.penWidth / 2) + 2
		self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
		self.lastPoint = QPoint(endPoint)

	def penColor(self):
		return self.myPenColor

	def penWidth(self):
		return self.myPenWidth
#display the points on the character	
	def iconShow(self,name,png,(wd,ht)):
		self.name = QLabel(self)
		self.name.setAccessibleName(name)
		self.names[self.name]=int(self.name.accessibleName())
		self.name.setText("<font color='red'>"+png+"</font>")
		pix = QPixmap(png)
		pix = pix.scaled(35,35,Qt.KeepAspectRatioByExpanding)
		self.name.setPixmap(pix)
		self.name.setMask(pix.mask())
		self.name.move(QPoint(wd,ht))
		self.setMouseTracking(True)
		self.name.setMouseTracking(True)
		self.name.show()
		self.name.setAttribute(Qt.WA_DeleteOnClose)
		return self.name
		
	def swap_dic(self,dic):
		return dict((v, k) for (k, v) in dic.items())	
	def splash(self,image):
		#"""
		self.spdlg = QDialog()
		label =QLabel(self.spdlg)
		label.setGeometry(QRect(90, 30, 300, 300))
		label.setPixmap(QPixmap("image/"+image+".png"))
		#print dir(self.spdlg)
		#dlg.connect(self.dlgmouseEvent)
		#QObject.connect(dlg, SIGNAL("clicked()"),dlg.destroy)
		self.spdlg.mousePressEvent = self.dlgmouseEvent
		
		#dlg.event = self.dlgmouseEvent
		self.spdlg.exec_()
		#dlg.raise()
		#dlg.activateWindow()
		#sleep(2)
		self.spdlg.destroy()
		
		
		#dlg.exec_()
		#self.app.processEvents()
		#if dlg.exec_():
		#sleep(2)
		#self.app.processEvents()
		#print dir(dlg)
		#dlg.close()
			#QTimer.singleShot(6000, dlg.quit)
		print 'ok'
		
		"""
		splashPix = QPixmap("image/"+image+".png")
		splash = QSplashScreen(splashPix,Qt.WindowStaysOnTopHint)
		self.app.processEvents()
		splash.show()
		self.app.processEvents()
		print image
		sleep(2)
		splash.close()
"""
	def dlgmouseEvent(self, event):
		#print 'event'
		if event.button():
			self.spdlg.close()
