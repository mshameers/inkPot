#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

class WriteSet(QtGui.QWidget):
	def __init__(self, parent=None):
		super(WriteSet, self).__init__(parent)
#initialization		
		self.setn = 0
		self.positions = []
		self.fontSize = 500
		self.data = ' '
		#self.data = u'\u0D07'u'\u0D6F'u'\u0D38'u'\u0D48'u'\u0D31'u'\u0D4D'u'\u0D31'u'\u0D4D'#u'\u0B85'
		self.write = False
		self.myPenWidth = self.fontSize/6
		self.image = QtGui.QImage()
		self.setFixedSize(QtCore.QSize((self.appWidth)/2+60,(self.appheight)/2-100))
		self.names = {}
		self.pointPos = {}
		self.ht = 30
		self.name = QtGui.QLabel()
		self.setAcceptDrops(True)
		self.pointValues = [[QtCore.QPoint(0,0),],[QtCore.QPoint(0,0),],[QtCore.QPoint(0,0),],[QtCore.QPoint(0,0),],[QtCore.QPoint(0,0),],]
		self.writeStart = 0
		self.check = []
		self.check1 = set()
		self.checkValue = set(['1', '3', '2', '5', '4'])
		self.temp = 0
		self.ok = 0

#display the point 
	def iconShow(self,name,png,wid):
		self.name = QtGui.QLabel(self)
		self.name.setAccessibleName(str(name))
		self.names[self.name]=int(self.name.accessibleName())
		pix = QtGui.QPixmap(png)
		pix = pix.scaled(20,20,QtCore.Qt.KeepAspectRatioByExpanding)

		self.name.setPixmap(pix)
		wid =wid+30
		self.name.move(wid,self.ht)
		self.name.mouseReleaseEvent = self.labelRelease
		self.setMouseTracking(True)
		self.name.setMouseTracking(True)
		self.name.show()
		self.name.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		return self.name
		#return self.name.pos()
		
		
	def labelRelease(self,event):
		print 'mouserelease'	
		
#drag function for the point setting
	def dragEnterEvent(self, event):
		if event.source() == self:
			event.setDropAction(QtCore.Qt.MoveAction)
			
			event.accept()
		else:
			event.acceptProposedAction()
		#else:
		#	event.ignore()

	dragMoveEvent = dragEnterEvent

#drop function for the point setting
	def dropEvent(self, event):
		if event.mimeData().hasFormat('application/x-dnditemdata') and self.setn == 0:
			itemData = event.mimeData().data('application/x-dnditemdata')
			dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.ReadOnly)

			pixmap = QtGui.QPixmap()
			offset = QtCore.QPoint()
			dataStream >> pixmap >> offset
	
			newIcon = QtGui.QLabel(self)
			newIcon.setPixmap(pixmap)
			newIcon.move(event.pos() - offset)
			newIcon.show()
			newIcon.setAttribute(QtCore.Qt.WA_DeleteOnClose)
			self.pointPos[self.childAtpos] = (event.pos().x()*2-12,event.pos().y()*2-72)
			if event.source() == self:
				position = QtCore.QPoint( event.pos().x(),  event.pos().y())
				self.positions.append(position)
				event.setDropAction(QtCore.Qt.MoveAction)
				event.accept()
				self.name_dic = self.swap_dic(self.names)
				self.names.pop(self.name_dic[self.childAtpos])
				self.names[newIcon]= int(self.childAtpos)
			else:
				event.acceptProposedAction()
		else:
			event.ignore()
#start the drag function when on an icon				
	def mousePressEvent(self, event):
			
		if event.button() == QtCore.Qt.LeftButton :
			self.lastPoint = event.pos()
			self.write = True
			mouse = QtCore.QPoint( event.pos().x(),  event.pos().y())
			if self.writeStart ==1:
				self.setAcceptDrops(False)
		else:
			print 'not'	, 	mousePosition
				
		self.child = self.childAt(event.pos())
		self.childAtpos = self.names[self.child]
		if not self.child:
			return
		pixmap = QtGui.QPixmap(self.child.pixmap())
		itemData = QtCore.QByteArray()
		dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.WriteOnly)
		dataStream << pixmap << QtCore.QPoint(event.pos() - self.child.pos())
		mimeData = QtCore.QMimeData()
		mimeData.setData('application/x-dnditemdata', itemData)

		drag = QtGui.QDrag(self)
		drag.setMimeData(mimeData)
		drag.setPixmap(pixmap)
		drag.setHotSpot(event.pos() - self.child.pos())
		tempPixmap = QtGui.QPixmap(pixmap)
		painter = QtGui.QPainter()
		painter.begin(tempPixmap)
		painter.fillRect(pixmap.rect(), QtGui.QColor(127, 127, 127, 127))
		painter.end()
		self.child.setPixmap(tempPixmap)

		if drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction, QtCore.Qt.CopyAction) == QtCore.Qt.MoveAction:
			self.child.close()
		else:
			self.child.show()
			self.child.setPixmap(pixmap)

#show the character to set points
	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		dirtyRect = event.rect()
		painter.drawImage(dirtyRect, self.image, dirtyRect)
		self.path = QtGui.QPainterPath()
		self.path.addText(QtCore.QPointF(self.width()/4,self.height()-60),self.font,self.data)
		self.path.addRect(0,0,self.width(),self.height())
		painter.setPen(QtGui.QPen(QtGui.QColor(self.backColor), 1,QtCore.Qt.SolidLine,QtCore.Qt.FlatCap, QtCore.Qt.MiterJoin))
		painter.setBrush(QtGui.QColor(self.backColor))#122, 163, 39))
	
		painter.drawPath(self.path);
		painter.strokePath(self.path,QtGui.QPen(QtCore.Qt.darkCyan))
		painter.end()
#function when resizing window 		
	def resizeEvent(self, event):
		if self.width() > self.image.width() or self.height() > self.image.height():
			newWidth = max(self.width() + 128, self.image.width())
			newHeight = max(self.height() + 128, self.image.height())
			self.resizeImage(self.image, QtCore.QSize(newWidth, newHeight))
			self.update()
		super(WriteSet, self).resizeEvent(event)
#function to resize image 	
	def resizeImage(self, image, newSize):
		if image.size() == newSize:
			return
		newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
		newImage.fill(QtGui.qRgb(255, 255, 255))
		painter = QtGui.QPainter(newImage)
		painter.drawImage(QtCore.QPoint(0, 0), image)
		self.image = newImage

	def penColor(self):
		return self.myPenColor

	def penWidth(self):
		return self.myPenWidth
	
	def swap_dic(self,dic):
		return dict((v, k) for (k, v) in dic.items())

