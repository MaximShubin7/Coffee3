import io
import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

t1 = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>781</width>
      <height>491</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>161</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить/Изменить</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

t2 = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
    <class>MainWindow</class>
    <widget class="QMainWindow" name="MainWindow">
        <property name="geometry">
            <rect>
                <x>0</x>
                <y>0</y>
                <width>321</width>
                <height>303</height>
            </rect>
        </property>
        <property name="windowTitle">
            <string>MainWindow</string>
        </property>
        <widget class="QWidget" name="centralwidget">
            <widget class="QWidget" name="verticalLayoutWidget">
                <property name="geometry">
                    <rect>
                        <x>140</x>
                        <y>40</y>
                        <width>160</width>
                        <height>221</height>
                    </rect>
                </property>
                <layout class="QVBoxLayout" name="verticalLayout">
                    <item>
                        <widget class="QLineEdit" name="lineEdit"/>
                    </item>
                    <item>
                        <widget class="QLineEdit" name="lineEdit_2"/>
                    </item>
                    <item>
                        <widget class="QLineEdit" name="lineEdit_3"/>
                    </item>
                    <item>
                        <widget class="QLineEdit" name="lineEdit_4"/>
                    </item>
                    <item>
                        <widget class="QLineEdit" name="lineEdit_5"/>
                    </item>
                    <item>
                        <widget class="QLineEdit" name="lineEdit_6"/>
                    </item>
                    <item>
                        <widget class="QLineEdit" name="lineEdit_7"/>
                    </item>
                </layout>
            </widget>
            <widget class="QLabel" name="label">
                <property name="geometry">
                    <rect>
                        <x>40</x>
                        <y>50</y>
                        <width>91</width>
                        <height>20</height>
                    </rect>
                </property>
                <property name="text">
                    <string>ID</string>
                </property>
            </widget>
            <widget class="QLabel" name="label_2">
                <property name="geometry">
                    <rect>
                        <x>40</x>
                        <y>80</y>
                        <width>91</width>
                        <height>20</height>
                    </rect>
                </property>
                <property name="text">
                    <string>название сорта</string>
                </property>
            </widget>
            <widget class="QLabel" name="label_3">
                <property name="geometry">
                    <rect>
                        <x>40</x>
                        <y>110</y>
                        <width>91</width>
                        <height>16</height>
                    </rect>
                </property>
                <property name="text">
                    <string>степень обжарки</string>
                </property>
            </widget>
            <widget class="QLabel" name="label_4">
                <property name="geometry">
                    <rect>
                        <x>40</x>
                        <y>140</y>
                        <width>91</width>
                        <height>16</height>
                    </rect>
                </property>
                <property name="text">
                    <string>молотый/в зернах</string>
                </property>
            </widget>
            <widget class="QLabel" name="label_5">
                <property name="geometry">
                    <rect>
                        <x>40</x>
                        <y>170</y>
                        <width>91</width>
                        <height>16</height>
                    </rect>
                </property>
                <property name="text">
                    <string>описание вкуса</string>
                </property>
            </widget>
            <widget class="QLabel" name="label_6">
                <property name="geometry">
                    <rect>
                        <x>40</x>
                        <y>200</y>
                        <width>91</width>
                        <height>16</height>
                    </rect>
                </property>
                <property name="text">
                    <string>цена</string>
                </property>
            </widget>
            <widget class="QLabel" name="label_7">
                <property name="geometry">
                    <rect>
                        <x>40</x>
                        <y>230</y>
                        <width>91</width>
                        <height>16</height>
                    </rect>
                </property>
                <property name="text">
                    <string>объем упаковки</string>
                </property>
            </widget>
            <widget class="QPushButton" name="pushButton_2">
                <property name="geometry">
                    <rect>
                        <x>40</x>
                        <y>10</y>
                        <width>75</width>
                        <height>23</height>
                    </rect>
                </property>
                <property name="text">
                    <string>Сохранить</string>
                </property>
            </widget>
        </widget>
        <widget class="QMenuBar" name="menubar">
            <property name="geometry">
                <rect>
                    <x>0</x>
                    <y>0</y>
                    <width>321</width>
                    <height>21</height>
                </rect>
            </property>
        </widget>
        <widget class="QStatusBar" name="statusbar"/>
    </widget>
    <resources/>
    <connections/>
</ui>
'''


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f1 = io.StringIO(t1)
        uic.loadUi(f1, self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.click)
        con = sqlite3.connect("BD")
        cur = con.cursor()
        self.result = cur.execute("SELECT * FROM Coffee").fetchall()
        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])

    def click(self):
        self.ex = Dobav()
        self.ex.show()


class Dobav(QMainWindow):
    def __init__(self):
        super().__init__()
        f2 = io.StringIO(t2)
        uic.loadUi(f2, self)
        self.initUI()

    def initUI(self):
        self.pushButton_2.clicked.connect(self.push)

    def push(self):
        con = sqlite3.connect("BD")
        cur = con.cursor()
        ids = [i[0] for i in cur.execute("SELECT ID FROM Coffee").fetchall()]
        if int(self.lineEdit.text()) in ids:
            cur.execute('''UPDATE Coffee
                        SET (name, step, mz, opis, price, V) = (?, ?, ?, ?, ?, ?)
                        WHERE ID = ?''', (
                self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(),
                self.lineEdit_6.text(), self.lineEdit_7.text(), int(self.lineEdit.text())))
        else:
            cur.execute('''INSERT INTO Coffee VALUES(?,?,?,?,?,?,?)''',
                        (int(self.lineEdit.text()), self.lineEdit_2.text(), self.lineEdit_3.text(),
                         self.lineEdit_4.text(), self.lineEdit_5.text(), int(self.lineEdit_6.text()),
                         int(self.lineEdit_7.text())))
        con.commit()
        self.hide()
        ex.initUI()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
