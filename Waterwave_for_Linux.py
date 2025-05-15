import sys
import getpass
from PyQt5.QtCore import Qt, QTimer, QDateTime, QRect
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

class WatermarkWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.username = getpass.getuser()
        self.init_ui()
        self.update_time()

        # 设置每分钟更新一次时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(60000)

    def init_ui(self):
        # 设置窗口标志，使窗口透明且始终在最上层
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.setWindowOpacity(0.7)  # 可选：设置窗口透明度
        self.resize(800, 600)
        self.center()

        # 使窗口点击穿透
        self.setWindowFlags(self.windowFlags() | Qt.X11BypassWindowManagerHint)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    def center(self):
        screen = QDesktopWidget().availableGeometry()
        self.setGeometry(screen)

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm")
        self.watermark_text = f"{self.username} {current_time}"
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        # 设置字体
        font = QFont("Arial", 80, QFont.Bold)
        painter.setFont(font)

        # 计算窗口的中心点
        rect = QRect(0, 0, self.width(), self.height())
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(-45)

        # 设置文字颜色
        painter.setPen(QColor(0, 0, 0, 100))

        # 绘制文本并居中显示
        painter.drawText(rect.translated(-self.width() / 2, -self.height() / 2), Qt.AlignCenter, self.watermark_text)

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wm = WatermarkWindow()
    wm.show()
    sys.exit(app.exec_())
