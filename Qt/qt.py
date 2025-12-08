import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QDialog, QMainWindow,
    QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel
)
from PyQt5.QtCore import pyqtSignal


# ------------------------------
#      Login Form (QDialog)
# ------------------------------
class LoginForm(QDialog):
    login_success = pyqtSignal()     # сигнал об успешном логине

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(250, 150)

        # Widgets
        self.label = QLabel("Введите пароль:")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Войти")
        self.btn_login.clicked.connect(self.check_password)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.password)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def check_password(self):
        if self.password.text() == "123":   # простой пример
            self.login_success.emit()       # отправляем сигнал
            self.accept()
        else:
            self.label.setText("Неверный пароль!")


# ------------------------------
#      Calculator (QMainWindow)
# ------------------------------
class CalculatorForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 200)

        # Центральный виджет
        central = QWidget()
        self.setCentralWidget(central)

        # Поля ввода
        self.num1 = QLineEdit()
        self.num2 = QLineEdit()

        # Кнопки
        self.btn_sum = QPushButton("Сложить")
        self.btn_sum.clicked.connect(self.sum_numbers)

        # Результат
        self.result_label = QLabel("Результат: ")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Число 1:"))
        layout.addWidget(self.num1)
        layout.addWidget(QLabel("Число 2:"))
        layout.addWidget(self.num2)
        layout.addWidget(self.btn_sum)
        layout.addWidget(self.result_label)

        central.setLayout(layout)

    def sum_numbers(self):
        try:
            a = float(self.num1.text())
            b = float(self.num2.text())
            self.result_label.setText(f"Результат: {a + b}")
        except ValueError:
            self.result_label.setText("Ошибка: введите числа!")


# ------------------------------
#          MAIN APP
# ------------------------------
class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # Создаем формы
        self.login = LoginForm()
        self.calc = CalculatorForm()

        # Подписываемся на сигнал успешного входа
        self.login.login_success.connect(self.show_calculator)

        self.login.show()
        sys.exit(self.app.exec_())

    def show_calculator(self):
        self.calc.show()


if __name__ == "__main__":
    App()

