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

        print("X:", self.scene.width())

        
        if qc.Qt.Key_D in self.active_keys and self.player.x()+self.img_player.width() < self.scene.width():
            self.player.setX(self.player.x()+5)
        if qc.Qt.Key_A in self.active_keys and self.player.x() > 0:
            self.player.setX(self.player.x()-5)
        #Add Spacebar later!




if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    window = Window()
    window.show()
    
    app.exec_()