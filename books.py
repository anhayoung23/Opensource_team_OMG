import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

# 사전 정의된 도서 정보
books_info = {
    "Python Crash Course": {
        "author": "Eric Matthes",
        "genre": "Programming",
        "year": 2015,
        "rating": 4.8
    },
    "The Great Gatsby": {
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "year": 1925,
        "rating": 4.2
    },
    # 추가 도서 정보를 여기에 계속해서 추가할 수 있습니다.
}

class BookInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('도서 정보 조회 어플리케이션')
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.inputLabel = QLabel('도서 이름:')
        layout.addWidget(self.inputLabel)

        self.inputField = QLineEdit()
        layout.addWidget(self.inputField)

        self.outputLabel = QLabel('도서 정보가 여기 표시됩니다.')
        layout.addWidget(self.outputLabel)

        searchButton = QPushButton('도서 조회')
        searchButton.clicked.connect(self.searchBook)
        layout.addWidget(searchButton)

        self.setLayout(layout)

    def searchBook(self):
        book_name = self.inputField.text()
        if book_name in books_info:
            book_info = books_info[book_name]
            info_text = (
                f"도서명: {book_name}\n"
                f"저자: {book_info['author']}\n"
                f"장르: {book_info['genre']}\n"
                f"발행년도: {book_info['year']}\n"
                f"평점: {book_info['rating']}"
            )
            self.outputLabel.setText(info_text)
        else:
            self.outputLabel.setText("도서를 찾을 수 없습니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    book_app = BookInfoApp()
    book_app.show()
    sys.exit(app.exec_())

