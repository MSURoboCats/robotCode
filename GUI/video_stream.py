import cv2
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage


class VideoStream(QThread):
    image_update = pyqtSignal(QImage)

    def run(self):
        self.thread_active = True
        capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = capture.read()
            if ret:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                convert_to_qt_format = QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QImage.Format_RGB888)
                pic = convert_to_qt_format.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(pic)

    def stop(self):
        self.thread_active = False
        self.quit()