import cv2
import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

# 사전 정의된 음료수 정보
drinks_info = {
    "cola.jpg": {
        "name": "콜라",
        "price": "1500원",
        "availability": "근처 편의점에서 구매 가능",
        "link": "https://www.cocacola.co.kr/",
        "location": "37.5665,126.9780"  # 음료수 위치 예시
    },
    
    "Samdasoo.jpg": {
        "name": "삼다수",
        "price": "1100원",
        "availability": "근처 편의점에서 구매 가능",
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },
        
    "Ice americano.jpg": {
        "name": "아이스 아메리카노",
        "price": "3000원",
        "availability": "근처 카페에서 구매 가능",
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },
    
     "Ice tea.jpg": {
        "name": "아이스티",
        "price": "2300원",
        "availability": "근처 카페에서 구매 가능",
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },

     "Yuza tea.jpg": {
        "name": "유자차",
        "price": "3000원",
        "availability": "근처 카페에서 구매 가능",
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },

     "Monster Energy Drink.jpg": {
        "name": "Monster Energy Drink",
        "price": "2200원",
        "availability": "근처 편의점에서 구매 가능",
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },

     "Pocari sweat.jpg": {
        "name": "포카리 스웨트",
        "price": "1800원",
        "availability": "근처 편의점에서 구매 가능",
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },

    "Banana milk.jpg": {
        "name": "바나나우유",
        "price": "1800원",
        "availability": "근처 편의점에서 구매 가능",
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },

    "Hot chocolate.jpg": {
        "name": "핫초코",
        "price": "4500원",
        "availability": "근처 카페에서 구매 가능",
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },
        
    "Macha Latte.jpg": {
        "name": "말차라떼",
        "price": "4500원",
        "availability": "근처 카페에서 구매 가능",
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },
}

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('음료수 인식 데모')
        self.resize(500, 750)

        layout = QVBoxLayout()

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.infoLabel = QLabel('음료수 정보가 여기 표시됩니다.')
        layout.addWidget(self.infoLabel)

        self.userLocationInput = QLineEdit('사용자 위치 (위도, 경도)')
        layout.addWidget(self.userLocationInput)

        self.mapButton = QPushButton('지도에서 보기')
        self.mapButton.clicked.connect(self.openMap)
        self.mapButton.setEnabled(False)
        layout.addWidget(self.mapButton)

        btn = QPushButton('이미지 업로드')
        btn.clicked.connect(self.loadImage)
        layout.addWidget(btn)

        self.setLayout(layout)

    def loadImage(self):
        filePath, _ = QFileDialog.getOpenFileName(self, '이미지 선택', '', "Image files (*.jpg *.png)")
        if filePath:
            self.displayImage(filePath)
            self.identifyDrink(filePath)

    def displayImage(self, filePath):
        image = cv2.imread(filePath)
        processed_image = self.processImage(image)
        height, width, channel = processed_image.shape
        bytesPerLine = 3 * width
        qImg = QImage(processed_image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self.imageLabel.setPixmap(QPixmap.fromImage(qImg))

    def processImage(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 10, 100)  # 변경된 임계값
        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(image, (cX, cY), 10, (0, 255, 0), -1)

        return image

    def identifyDrink(self, filePath):
        for drink_image, info in drinks_info.items():
            if drink_image in filePath:
                infoText = f"이름: {info['name']}\n가격: {info['price']}\n{info['availability']}\n웹사이트 링크: {info['link']}"
                self.infoLabel.setText(infoText)
                self.currentDrinkLocation = info.get("location", "")
                self.mapButton.setEnabled(True)
                break
        else:
            self.infoLabel.setText("인식된 음료수가 없습니다.")
            self.mapButton.setEnabled(False)

    def openMap(self):
        user_location = self.userLocationInput.text()
        if self.currentDrinkLocation and user_location:
            url = f"https://www.google.com/maps/dir/{user_location}/{self.currentDrinkLocation}"
            webbrowser.open(url)

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())

