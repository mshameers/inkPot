import sys,math,os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from writeAreaUi import Ui_Form
from write import Write
from writeWidget import WriteSet
from setWriteUi import Ui_Dialog
from monCalDlgUi import Ui_monCalDlg

POINTSPATH = "points"
#edited
#class Pixmap for an alphabet , to be called by charViewFun
class Pixmap(QObject):
    def __init__(self, pix):
        super(Pixmap, self).__init__()

        self.pixmap_item = QGraphicsPixmapItem(pix)
        self.pixmap_item.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)
    pos = pyqtProperty(QPointF, fset=_set_pos)

class Main(QWidget):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)

#characters store		
		try:	
			os.mkdir('character',0700)									
			self.createPointfun("orange")
			self.createPointfun("blue")
		except:
			pass

#GUI setup		
		self.writeUi = Ui_Form()										
		self.writeUi.setupUi(self)

#some initializations		
		self.langName = 'Latin'										
		self.tempNum = 0
		self.name = ['self.zero','self.one','self.two','self.three','self.four','self.five','self.six','self.seven','self.eight','self.nine','self.ten']
#connect gui widgets
		self.writeUi.languageComboBox.activated.connect(self.languageSelect)	
		self.writeUi.clearButton.clicked.connect(self.clear)
		self.writeUi.setButton.clicked.connect(self.settings)
		
		self.writeUi.quitButton.clicked.connect(self.appQuit)
		self.writeUi.charshowBut.clicked.connect(self.charShow)
		
		#self.updatesEnabled()
#get the screen width and height
		Write.app = app
		Write.appWidth = width											
		Write.appheight = height
		WriteSet.appWidth = width
		WriteSet.appheight = height
		Write.appName = app
#the write area widget setup		
		self.widget = Write(self.writeUi.bottomFrame)
		self.widget.setCursor(QCursor(QPixmap('image/pencil.png'),0,64))
		self.writeUi.gridLayout2.addWidget(self.widget,2, 0, 1, 1)
#set the app fullscreen
		self.showFullScreen()
#refresh characters folder for new characters		
		for files in os.listdir('character/'):							
			os.remove('character/'+files)
#update characters folder with English
		self.characterfun(65,112)									
#the characters showing widget setup		
		self.charView = QGraphicsView(self.writeUi.bottomFrame)
		self.charView.setMinimumHeight(height/4)
#create character images		
		self.charViewFun()							
		self.writeUi.gridLayout2.addWidget(self.charView,1, 0, 1, 1)
#populate language combobox		
		fontData = QFontDatabase()
		self.scripts = fontData.writingSystems()
		i = 0
		self.scrlist=[]
		while i < len(self.scripts):
			self.scriptList = [QFontDatabase.writingSystemName(self.scripts[i]),]
			self.scrlist.append(self.scriptList)
			self.writeUi.languageComboBox.addItems(self.scriptList)
			#self.writeUi.languageComboBox.setCurrentIndex(11)
			i += 1
		self.update()
		
		
	def mousePressEvent(self, event):
# check mouse click		
		if event.button() != Qt.LeftButton:								   
			event.ignore()
			return
#get details of the points
		self.name_dic3 = self.swap_dic(self.widget.names)				   
		#try:
		for i in range(0,len(self.name_dic3)):							   
			self.name_dic3[i].setVisible(False)
		self.widget.names = {}											   
		#except:
		#	pass
		self.charView.setCursor(Qt.ClosedHandCursor)
		mousePosition = QPoint( event.pos().x()-10,  event.pos().y()-50)   # position of alphabets mouse ..slight adjusted here
		self.pixItem = self.charView.itemAt (mousePosition )			   # get character at mouse position
		if self.pixItem in self.items2:
			self.charIndex = self.items2.index(self.pixItem)
			self.widget.image.fill(qRgb(255, 255, 255))
			self.widget.data = self.char[self.charIndex]#.unicode()
			filePath = "points/"+self.langName+".txt"
#if points list not available create one 		
		if not os.path.isfile(filePath):
			a_file = open(filePath,"w")
			a_file.close()
#if points list present get the values			
		with open(filePath,"r") as a_file:  
			for line in a_file:
				evalvedLine = eval(line)
				index = line.find('-'+str(self.charIndex)+',')
				self.widget.filePath = filePath
				if index != -1 and index< 2:
					Write.lineNo = line[1:line.find(',')]
					for i, item in enumerate(evalvedLine[1:]):
						if i == 0:
							self.widget.iconShow(str(i),'image/'+str(i)+'blue.png',item)
						else:
							self.widget.iconShow(str(i),'image/'+str(i)+'orange.png',item)

					self.charView.setHidden(True)
					break
			else:
#open a dialog for getting points
				self.dlg = QDialog()
				self.dlg.setFixedSize(width/2+60,height/2)
				self.showWindow = Ui_Dialog()
				self.showWindow.setupUi(self.dlg)
								
				self.widgetset = WriteSet(self.showWindow.widget)
				self.widgetset.backColor ="#7AA327"
				self.widgetset.penColor ="#FF000F"
				self.showWindow.spinBox.setMaximum(10)
				self.showWindow.spinBox.valueChanged.connect(self.points)
				self.showWindow.pushButton.clicked.connect(self.setWrite)
				self.widgetset.data = self.char[self.charIndex]
				self.widgetset.image.fill(qRgb(255, 255, 255))
				self.widgetset.font = QFont('Andica',height/4)
#if dialog ok, save the points				
				if self.dlg.exec_():
					filePath = "points/"+self.langName+".txt"
					if os.path.isfile(filePath):
						with open(filePath,"a") as a_file:
							a_file.write('-'+str(self.charIndex))								#write character's index first
							for i in range(0,len(self.widgetset.pointPos.values())):
								a_file.write(','+str(self.widgetset.pointPos.values()[i]))
					self.tempNum = 0
					with open(filePath,"a") as a_file:
						a_file.write('\n')		
					
					with open(filePath,"r") as a_file:  
						for line in a_file:
							evalvedLine = eval(line)
							#print evalvedLine
							index = line.find('-'+str(self.charIndex)+',')
							
							if index != -1 and index< 2:
								for i, item in enumerate(evalvedLine[1:]):
						#	print i,item, type(item)
									self.widget.iconShow(str(i),'image/'+str(i)+'orange.png',item)
					self.charView.setHidden(True)
				else:
					self.charView.setHidden(False)
					print 'not found'
					
			self.update()
			return
	#	else:
	#		print 'no file'
#update he language combobox			
	def languageSelect(self):
		for files in os.listdir('character/'):
			os.remove('character/'+files)
		self.langName = self.writeUi.languageComboBox.currentText()
		#print self.langName
		self.langDict = {"Latin":(65,112),"Malayalam":(3330,3435),"Tamil":(2947,3058),"Greek":(880,8486),"Cyrillic":(1024,7544),"Armenian":(1329,1418),"Hebrew":(1425,1524),"Arabic":(1542,1901),"Syriac":(1792,1866),"Devanagari":(2304,2418),"Bengali":(2433,2554),"Gurmukhi":(2561,2677),"Telugu":(3073,3183),"Kannada":(3202,3311),"Sinhala":(3458,3572),"Lao":(3713,3805),"Thai":(3585,3675),"Myanmar":(4096,4255),"Tibetan":(3840,4052),"Georgian":(4256,4348),"Cyrillic":(1024,7544),"Armenian":(1329,1418),"Hebrew":(1425,1524),"Arabic":(1542,1901)}
		self.start = self.langDict[str(self.langName)][0]
		self.stop = self.langDict[str(self.langName)][1]
		#print self.start
		self.characterfun(self.start,self.stop)
		self.charViewFun()
#create characters image in character folder
	def characterfun(self,start,stop):
		self.updatesEnabled()
		osPath = 'character/'
		#key = 65
		self.char = []
		while start < stop:
			character = QChar(start)
			self.char.append(character)
			pixmap = QPixmap( 80,90 )
			pixmap.fill(QColor(39,40,26))#(15,69,103))#0F4567))#(39,184,229))
			path = QPainterPath()
			font = QFont('Andika Basic')
			font.setPointSize(30 )
			font.setWeight( QFont.Bold )
			fontMetrics =QFontMetrics(font)

			path.addText( 10,60, font,QChar(start))# char[i] )
			painter = QPainter(pixmap )
			painter.setRenderHint( QPainter.Antialiasing )
			painter.setPen(QColor(255,255,255) )
			painter.setBrush( QBrush(QColor(255,255,255)))
			painter.drawPath(path)
			pixmap.save(osPath+str(start)+".png" )
			painter.end()
			start +=1
#function to make the characters animate
	def charViewFun(self):
		self.scene = QGraphicsScene()
		path = 'character/'
		listed = []
		listing = os.listdir(path)
		for i in range(0,len(listing)):
			listed.append(int(listing[i].split('.')[0]))
		listed.sort()
		self.items1 =[]
		self.items2 =[]
		for infile in listed:
			self.item = Pixmap(QPixmap('character/'+str(infile)))
			self.items1.append(self.item)
			#self.items1.sort()
			self.items2.append(self.item.pixmap_item)		
			self.scene.addItem(self.item.pixmap_item)

		self.tiledButton = QPushButton()
		# States.
		self.rootState = QState()
		self.tiledState = QState(self.rootState)
		# Values.
		for i, item in enumerate(self.items1):
			self.tiledState.assignProperty(item, 'pos',QPointF(((i % 15) - 4) * 82 + 30,((i //15) - 4) * 92 + 30))
		# Ui.
		self.charView.setScene(self.scene)

		self.charView.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
		
		self.states = QStateMachine()
		self.states.addState(self.rootState)
		self.states.setInitialState(self.rootState)
		self.rootState.setInitialState(self.tiledState)

		self.group = QParallelAnimationGroup()
		for i, item in enumerate(self.items1):
			self.anim = QPropertyAnimation(item, 'pos')
			self.anim.setDuration(750 + i * 25)
			self.anim.setEasingCurve(QEasingCurve.InOutBack)
			self.group.addAnimation(self.anim)
		self.trans = self.rootState.addTransition(self.tiledButton.pressed, self.tiledState)
		self.trans.addAnimation(self.group)
		self.timer = QTimer()
		self.timer.start(125)
		self.timer.setSingleShot(True)
		self.trans = self.rootState.addTransition(self.timer.timeout,self.tiledState)
		self.trans.addAnimation(self.group)
		self.states.start()
		
		#self.charView.centerOn(self.charView.width()/10,-self.charView.height()*100)
#show points when spinbox value of dialog box altered
	def points(self,int):
		if int-self.tempNum==1:
			self.widget.wid = self.widget.width()/1.4
			self.pnts = self.showWindow.spinBox.textFromValue(int)
			ht = 50*int
			
			self.name[int] = self.widgetset.iconShow(int,'image/'+self.pnts+'orange.png',ht)
			self.tempNum=int
		else:
			self.name_dic2 = self.widgetset.swap_dic(self.widgetset.names)
			
			self.name_dic2[int+1].clear()
			self.tempNum=self.tempNum-1
		#self.intValue = int
		#print self.tempNum
	def setWrite(self):
		print self.widgetset.pointPos.values()[0]
#when clear button pressed
	def clear(self):
		self.widget.image.fill(qRgb(255, 255, 255))
		self.widget.startWriting = 0
		self.widget.swapNames[0].setPixmap(QPixmap('image/'+str(0)+'blue.png').scaled(35,35,Qt.KeepAspectRatioByExpanding))
		for i in range (1,len(self.widget.swapNames)):
			self.widget.swapNames[i].setPixmap(QPixmap('image/'+str(i)+'orange.png').scaled(35,35,Qt.KeepAspectRatioByExpanding))
		self.update()
		
	def settings(self):
		self.setDlg = QDialog()
		self.setWindow = Ui_monCalDlg()
		self.setWindow.setupUi(self.setDlg)
		try:
			with open(POINTSPATH+"/Adjust.txt","r") as b_file:
				horAdjust = int(b_file.readline())
				verAdjust = int(b_file.readline())
		except:
				horAdjust = 0
				verAdjust = 0
		self.setWindow.horizontalSlider.setValue(horAdjust)
		self.setWindow.horizontalSlider_2.setValue(verAdjust)
		if self.setDlg.exec_():
			with open(POINTSPATH+"/Adjust.txt","w") as a_file:
				a_file.writelines(str(self.setWindow.horizontalSlider.value())+"\n"),
				#a_file.write('/n')
				a_file.writelines(str(self.setWindow.horizontalSlider_2.value()))
#function to swap a dict key value pair		
	def swap_dic(self,dic):
		return dict((v, k) for (k, v) in dic.items())
		
	def charShow(self):	
			self.charView.setHidden(False)
			
	def appQuit(self):
		sys.exit(0)	
#create the points		
	def createPointfun(self,circle):
		i= 0
		
		while i < 10:
			osPath = 'image/'
			pixmap = QPixmap("image/"+circle+"Circle.png")
			path = QPainterPath()
			font = QFont('Andika Basic')
			font.setPointSize(450 )
			font.setWeight( QFont.Bold )
			fontMetrics =QFontMetrics(font)

			path.addText( 275,675, font,str(i))
			painter = QPainter(pixmap)
			
			painter.setRenderHint( QPainter.Antialiasing )
			painter.setPen(QColor(255,255,255) )
			painter.setBrush( QBrush(QColor(255,255,255)))
			painter.drawPath(path)
			pixmap.save(osPath+str(i)+circle+".png" )
			painter.end()
			i+=1
			
		
if __name__ == "__main__":
	
    app = QApplication(sys.argv)
    width = QApplication.desktop().width()
    height = QApplication.desktop().height()

    window = Main()
    window.show()
    sys.exit(app.exec_())
	
	
	
	
