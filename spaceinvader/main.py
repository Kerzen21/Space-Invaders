from PyQt5 import QtWidgets as qw
from PyQt5 import QtCore as qc
from PyQt5 import QtGui as qg
import sys
import pathlib

DATA_DIR = pathlib.Path(__file__).parent.parent.joinpath("data")
SPRITES_DIR = DATA_DIR.joinpath("sprites")
SOUNDS_DIR = DATA_DIR.joinpath("sounds")

class Window(qw.QWidget):
    #Signals:

    def __init__(self):
        super().__init__()
        
        

        self.scene = qw.QGraphicsScene()
        self.view = qw.QGraphicsView()
        self.view.setScene(self.scene)
        
        layout = qw.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

     
        self.img_player = qg.QPixmap(str(SPRITES_DIR.joinpath("player.png")))  

        self.scene.setSceneRect(0, 0, 640, 500)
        
        self.view.scale(1, -1)
        self.player = self.addPixmap(self.img_player)
        
        


        self.player_shot = Shot(self, True)








        self.shot_timer = qc.QTimer()
        self.shot_timer.setInterval(16)
        self.shot_timer.timeout.connect(Shot.handle_all)
        self.shot_timer.start()
        
        self.timer = qc.QTimer()
        self.timer.setInterval(50)# ms
        self.timer.timeout.connect(self.handleActiveKeys)
        self.timer.start()




        self.active_keys = set()
    
 

    def addPixmap(self, pixmap):
        transformation = qg.QTransform().scale(1, -1)
        transformed_pixmap = pixmap.transformed(transformation)
        return self.scene.addPixmap(transformed_pixmap)
        
    

    def keyPressEvent(self, event):
        self.active_keys.add(event.key())


    def keyReleaseEvent(self, event):
        self.active_keys.remove(event.key())
    

    def handleActiveKeys(self):

        #print("X:", self.scene.width())

        
        if qc.Qt.Key_D in self.active_keys and self.player.x()+self.img_player.width() < self.scene.width():
            self.player.setX(self.player.x()+5)
        if qc.Qt.Key_A in self.active_keys and self.player.x() > 0:
            self.player.setX(self.player.x()-5)
        if qc.Qt.Key_Space in self.active_keys:  #attackspeed:
            #self.img_player_shot.width() 
            new_shot = Shot(self, True) ### shot_timer.ti
            new_shot.item.setX(self.player.x()+self.img_player.width()/2 - new_shot.img_item.width()/2) 
            new_shot.item.setY(self.player.y() + new_shot.img_item.height())
            new_shot.item.show()
            new_shot.item.setY(0)
            new_shot.is_active = True

            print("IS_ACTIVE?: ", new_shot.is_active)

            
        
class Shot(object):


    
    
    def __init__(self, window:Window, player=True):
        super().__init__()
        self.is_active = False
        
        self.window = window
        
        if player == True:
            self.img_item = qg.QPixmap(str(SPRITES_DIR.joinpath("player_shot.png")))
        else:
            self.img_item = qg.QPixmap(str(SPRITES_DIR.joinpath("invader_shot.png")))
        self.item = window.addPixmap(self.img_item)
        self.item.hide()

        self.shot_timer.timeout.connect(self.update)
        
        
        print("Step 1")
    def update(self):
        print("Step 2")
        if self.is_active:
            print("Active!!!!!", self)
        #if self.is_active == True:
        if self.item.isVisible() == True:
            self.item.setY(self.item.y()+5)
            #print("Step 3")
        if self.item.y() >= self.window.scene.height():
            self.is_active = False
            self.item.hide()
        
    @classmethod
    def handle_all(cls):
        print("Hello all!!!")



if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    window = Window()
    window.show()
    
    app.exec_()




  # while True: #main thread
  #     events = get_event()
  #     handle_events(events)
  #     update_gui()


  # while True: #timer thread
  #     handleActiveKeys()
  #     sleep(50)   #ms





#python -m pip inst

