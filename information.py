import webbrowser
import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QComboBox, QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

# 사전 정의된 음료수 정보
drinks_info = {

    "cola.jpg": {
        "name": {"en": "Cola", "ko": "콜라"},
        "price": {"en": "1500 Won", "ko": "1500원"},
        "availability": {"en": "Available at nearby convenience store", "ko": "근처 편의점에서 구매 가능"},
        "nutritional_info": {"en": "Calories - 140, Sugar - 39g", "ko": "칼로리 - 140, 설탕 - 39g"},
        "link": "https://www.cocacola.co.kr/",
        "location": "37.5665,126.9780"
    },

    "Samdasoo.jpg": {
        "name": {"en": "Samdasoo", "ko": "삼다수"},
        "price": {"en": "1100 Won", "ko": "1100원"},
        "availability": {"en": "Available at nearby convenience store", "ko": "근처 편의점에서 구매 가능"},
        "nutritional_info": {"en": "Calories - 0, Sugar - 0g", "ko": "칼로리 - 0, 설탕 - 0g"},
        "link": "https://www.jpdc.co.kr/samdasoo/index.htm",
        "location": "37.5665,126.9780"
    },

    "Ice americano.jpg": {
        "name": {"en": "Ice americano", "ko": "아이스 아메리카노"},
        "price": {"en": "3000 Won", "ko": "3000원"},
        "availability": {"en": "Available at Carochia, selecto, dessert39 etc.", "ko": "까로치아, 셀렉토, 디저트39 등의 카페에서 구매 가능"},
        "nutritional_info": {"en": "Calories - 5, Sugar - 0g", "ko": "칼로리 - 5, 설탕 - 0g"},
        "link": "https://github.com/anhayoung23/Opensource_team_OMG/blob/main/readme.md",
        "location": "37.5665,126.9780"
    },

    "Ice tea.jpg": {
        "name": {"en": "Ice tea", "ko": "아이스티"},
        "price": {"en": "2300 Won", "ko": "2300원"},
        "availability": {"en": "Available at Carochia, selecto, dessert39 etc.", "ko": "까로치아, 셀렉토, 디저트39 등의 카페에서 구매 가능"},
        "nutritional_info": {"en": "Calories - 100, Sugar - 25g", "ko": "칼로리 - 100, 설탕 - 25g"},
        "link": "https://github.com/anhayoung23/Opensource_team_OMG/blob/main/readme.md",
        "location": "37.5665,126.9780"
    },

    "Yuza tea.jpg": {
        "name": {"en": "Yuza tea", "ko": "유자차"},
        "price": {"en": "3000 Won", "ko": "3000원"},
        "availability": {"en": "Available at Carochia, selecto, dessert39 etc.", "ko": "까로치아, 셀렉토, 디저트39 등의 카페에서 구매 가능"},
        "nutritional_info": {"en": "Calories - 120, Sugar - 30g", "ko": "칼로리 - 120, 설탕 - 30g"},
        "link": "https://github.com/anhayoung23/Opensource_team_OMG/blob/main/readme.md",
        "location": "37.5665,126.9780"
    },

    "Monster Energy Drink.jpg": {
        "name": {"en": "Monster Energy Drink", "ko": "Monster Energy Drink"},
        "price": {"en": "2200 Won", "ko": "2200원"},
        "availability": {"en": "Available at nearby convenience store. Recommend white or green.", "ko": "근처 편의점에서 구매 가능. 하얀색, 초록색 추천."},
        "nutritional_info": {"en": "Calories - 240, Sugar - 60g", "ko": "칼로리 - 240, 설탕 - 60g"},
        "link": "https://github.com/anhayoung23/Opensource_team_OMG/blob/main/readme.md",
        "location": "37.5665,126.9780"
    },

    "Pocari sweat.jpg": {
        "name": {"en": "Pocari sweat", "ko": "포카리 스웨트"},
        "price": {"en": "1800 Won", "ko": "1800원"},
        "availability": {"en": "Available at nearby convenience store", "ko": "근처 편의점에서 구매 가능"},
        "nutritional_info": {"en": "Calories - 80, Sugar - 18g", "ko": "칼로리 - 80, 설탕 - 18g"},
        "link": "https://github.com/anhayoung23/Opensource_team_OMG/blob/main/readme.md",
        "location": "37.5665,126.9780"
    },

    "Banana milk.jpg": {
        "name": {"en": "Banana milk", "ko": "바나나우유"},
        "price": {"en": "1800 Won", "ko": "1800원"},
        "availability": {"en": "Available at nearby convenience store", "ko": "근처 편의점에서 구매 가능"},
        "nutritional_info": {"en": "Calories - 200, Sugar - 25g", "ko": "칼로리 - 200, 설탕 - 25g"},
        "link": "https://github.com/anhayoung23/Opensource_team_OMG/blob/main/readme.md",
        "location": "37.5665,126.9780"
    },

    "Hot chocolate.jpg": {
        "name": {"en": "Hot chocolate", "ko": "핫초코"},
        "price": {"en": "4500 Won", "ko": "4500원"},
        "availability": {"en": "Available at Carochia, selecto, dessert39 etc.", "ko": "까로치아, 셀렉토, 디저트39 등의 카페에서 구매 가능"},
        "nutritional_info": {"en": "Calories - 200, Sugar - 30g", "ko": "칼로리 - 200, 설탕 - 30g"},
        "link": "https://github.com/anhayoung23/Opensource_team_OMG/blob/main/readme.md",
        "location": "37.5665,126.9780"
    },

    "Matcha Latte.jpg": {
        "name": {"en": "Matcha Latte", "ko": "말차라떼"},
        "price": {"en": "4500 Won", "ko": "4500원"},
        "availability": {"en": "Available at Carochia, selecto, dessert39 etc. Carroccia's Matcha Latte is delicious.", "ko": "까로치아, 셀렉토, 디저트39 등의 카페에서 구매 가능. 까로치아가 맛있음."},
        "nutritional_info": {"en": "Calories - 250, Sugar - 35g", "ko": "칼로리 - 250, 설탕 - 35g"},
        "link": "https://github.com/anhayoung23/Opensource_team_OMG/blob/main/readme.md",
        "location": "37.5665,126.9780"
    },
}

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('음료수 인식 데모')
        self.resize(500, 750)

        self.currentLanguage = "en"

        layout = QVBoxLayout()

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.infoLabel = QLabel('음료수 정보가 여기 표시됩니다.')
        layout.addWidget(self.infoLabel)

        self.mapButton = QPushButton('지도에서 보기')
        self.mapButton.clicked.connect(self.openMap)
        self.mapButton.setEnabled(False)
        layout.addWidget(self.mapButton)

        self.btn = QPushButton('이미지 업로드')
        self.btn.clicked.connect(self.loadImage)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        # Language selection
        self.languageSelector = QComboBox()
        self.languageSelector.addItems(["English", "한국어"])
        self.languageSelector.currentIndexChanged.connect(self.updateLanguage)
        layout.addWidget(self.languageSelector)

        self.lastLoadedFilePath = None

    def loadImage(self):
        filePath, _ = QFileDialog.getOpenFileName(self, '이미지 선택', '', "Image files (*.jpg *.png)")
        if filePath:
            self.lastLoadedFilePath = filePath
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
        # 이미지 처리 로직을 여기에 추가합니다.
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 10, 100)  # 변경된 임계값
        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 이미지에 컨투어에 따른 초록색 원을 그리고, 가장 큰 컨투어에는 원형 링을 그립니다.
        for contour in contours:
            # 각 컨투어의 중심에 작은 초록색 원을 그립니다.
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(image, (cX, cY), 5, (0, 255, 0), -1)

        # 가장 큰 컨투어를 찾아서 큰 원형 링을 그립니다.
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(image, center, radius, (0, 255, 0), 2)

        return image

    def updateLanguage(self):
        # Update the interface based on the selected language
        self.currentLanguage = "en" if self.languageSelector.currentText() == "English" else "ko"
        self.updateUIText()  # Update the text of the UI elements
        if self.lastLoadedFilePath:
            self.identifyDrink(self.lastLoadedFilePath)  # Re-identify the drink to update information

    def updateUIText(self):
        # Update text for all UI elements
        self.mapButton.setText("Show in Map" if self.currentLanguage == "en" else "지도에서 보기")
        self.btn.setText("Upload Image" if self.currentLanguage == "en" else "이미지 업로드")
        self.infoLabel.setText(
            "Drink information will be displayed here." if self.currentLanguage == "en" else "음료수 정보가 여기 표시됩니다.")
        # Add similar lines for other UI elements needing language updates

    def identifyDrink(self, filePath):

        # 파일 이름으로 음료수를 식별합니다.
        match = None  # Initialize match to None
        if filePath:
            fileName = filePath.split('/')[-1]
            for drink_image, info in drinks_info.items():
                if fileName.lower() == drink_image.lower():
                    match = info
                    break

        if match:
            language_key = self.currentLanguage
            if language_key not in match['name']:
                self.currentLanguage = 'en'  # Fallback to English if the selected language is not available

            infoText = (
                f"Name: {match['name'][self.currentLanguage]}\n"
                f"Price: {match['price'][self.currentLanguage]}\n"
                f"Availability: {match['availability'][self.currentLanguage]}\n"
                f"Nutritional Info: {match['nutritional_info'][self.currentLanguage]}\n"
                f"Website Link: {match['link']}"
            )
            self.infoLabel.setText(infoText)
            self.currentDrinkLocation = match.get("location", "")
            self.mapButton.setEnabled(True)
        else:
            self.infoLabel.setText("No drink identified." if self.currentLanguage == "en" else "인식된 음료수가 없습니다.")
            self.mapButton.setEnabled(False)

        fileName = filePath.split('/')[-1]
        for drink_image, info in drinks_info.items():
            if fileName.lower() == drink_image.lower():
                # 음료수 정보를 표시합니다.
                infoText = (
                    f"이름: {info['name'][self.currentLanguage]}\n"
                    f"가격: {info['price'][self.currentLanguage]}\n"
                    f"가능 여부: {info['availability'][self.currentLanguage]}\n"
                    f"영양 성분: {info['nutritional_info'][self.currentLanguage]}\n"
                    f"웹사이트 링크: {info['link']}"
                )
                self.infoLabel.setText(infoText)
                self.currentDrinkLocation = info.get("location", "")
                self.mapButton.setEnabled(True)
                return

    def openMap(self):

        if self.currentDrinkLocation:
            # 사용자 위치에서 음료수 위치까지의 경로를 지도에서 보여줍니다.
            url = f"https://www.google.com/maps/dir/{self.currentDrinkLocation}"
            webbrowser.open(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())

