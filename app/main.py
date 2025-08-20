import sys
from PySide6.QtWidgets import QApplication, QLabel

def main():
    app = QApplication(sys.argv)
    label = QLabel("NSFW-Editor is running!")
    label.resize(400, 200)
    label.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
