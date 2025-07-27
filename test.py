from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("Hello PyQt5")
window.resize(300, 200)
window.show()
app.exec_()
