# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
ogrenciKayitResimYol=""
seciliSinif=""
seciliSinif2=""
seciliOgrenciTc=""
zaman=""
zaman2=""
kamera=""
import numpy as np 
import cv2
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from skimage import measure

import datetime
import random
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 530, 571, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(22)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 271, 291))
        self.label.setObjectName("label")
        self.labelBilgi2 = QtWidgets.QLabel(self.centralwidget)
        self.labelBilgi2.setGeometry(QtCore.QRect(30, 490, 561, 31))
        self.labelBilgi2.setObjectName("labelBilgi2")
        self.labelTuzBiber = QtWidgets.QLabel(self.centralwidget)
        self.labelTuzBiber.setGeometry(QtCore.QRect(330, 30, 271, 291))
        self.labelTuzBiber.setObjectName("labelTuzBiber")
        self.groupBoxGoster = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxGoster.setGeometry(QtCore.QRect(610, 410, 411, 361))
        self.groupBoxGoster.setTitle("")
        self.groupBoxGoster.setObjectName("groupBoxGoster")
        self.label_6 = QtWidgets.QLabel(self.groupBoxGoster)
        self.label_6.setGeometry(QtCore.QRect(210, 80, 161, 161))
        self.label_6.setObjectName("label_6")
        self.comboBoxOgrenci = QtWidgets.QComboBox(self.groupBoxGoster)
        self.comboBoxOgrenci.setGeometry(QtCore.QRect(10, 40, 161, 31))
        self.comboBoxOgrenci.setObjectName("comboBoxOgrenci")
        self.label_7 = QtWidgets.QLabel(self.groupBoxGoster)
        self.label_7.setGeometry(QtCore.QRect(50, 20, 54, 14))
        self.label_7.setObjectName("label_7")
        self.pushButtonGoster = QtWidgets.QPushButton(self.groupBoxGoster)
        self.pushButtonGoster.setGeometry(QtCore.QRect(20, 90, 91, 31))
        self.pushButtonGoster.setObjectName("pushButtonGoster")
        self.comboBoxSinif = QtWidgets.QComboBox(self.groupBoxGoster)
        self.comboBoxSinif.setGeometry(QtCore.QRect(210, 40, 161, 31))
        self.comboBoxSinif.setObjectName("comboBoxSinif")
        self.label_8 = QtWidgets.QLabel(self.groupBoxGoster)
        self.label_8.setGeometry(QtCore.QRect(240, 20, 54, 14))
        self.label_8.setObjectName("label_8")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.groupBoxGoster)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(20, 220, 151, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.labelSoyad = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.labelSoyad.setObjectName("labelSoyad")
        self.horizontalLayout_8.addWidget(self.labelSoyad)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.groupBoxGoster)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 180, 151, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.labelAd = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.labelAd.setObjectName("labelAd")
        self.horizontalLayout_7.addWidget(self.labelAd)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.groupBoxGoster)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(20, 300, 151, 31))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.labelSinif = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.labelSinif.setObjectName("labelSinif")
        self.horizontalLayout_10.addWidget(self.labelSinif)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.groupBoxGoster)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(20, 260, 151, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.labelTC = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.labelTC.setObjectName("labelTC")
        self.horizontalLayout_9.addWidget(self.labelTC)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxGoster)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 250, 141, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.labelDevamsizlik = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelDevamsizlik.setObjectName("labelDevamsizlik")
        self.verticalLayout_2.addWidget(self.labelDevamsizlik)
        self.groupBoxEkle = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEkle.setGeometry(QtCore.QRect(610, 40, 451, 371))
        self.groupBoxEkle.setObjectName("groupBoxEkle")
        self.labelEkle = QtWidgets.QLabel(self.groupBoxEkle)
        self.labelEkle.setGeometry(QtCore.QRect(220, 20, 211, 221))
        self.labelEkle.setObjectName("labelEkle")
        self.pushButtonResimEkle = QtWidgets.QPushButton(self.groupBoxEkle)
        self.pushButtonResimEkle.setGeometry(QtCore.QRect(40, 100, 82, 25))
        self.pushButtonResimEkle.setObjectName("pushButtonResimEkle")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBoxEkle)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 180, 191, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEditSoyad = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditSoyad.setObjectName("lineEditSoyad")
        self.horizontalLayout_5.addWidget(self.lineEditSoyad)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.comboBoxSinif2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxSinif2.setObjectName("comboBoxSinif2")
        self.horizontalLayout_6.addWidget(self.comboBoxSinif2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEditTC = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditTC.setObjectName("lineEditTC")
        self.horizontalLayout_3.addWidget(self.lineEditTC)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEditAd = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditAd.setObjectName("lineEditAd")
        self.horizontalLayout_4.addWidget(self.lineEditAd)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 420, 260, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonKamera = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonKamera.setObjectName("pushButtonKamera")
        self.horizontalLayout.addWidget(self.pushButtonKamera)
        self.pushButtonHesap = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonHesap.setObjectName("pushButtonHesap")
        self.horizontalLayout.addWidget(self.pushButtonHesap)
        self.pushButtonCek = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonCek.setObjectName("pushButtonCek")
        self.horizontalLayout.addWidget(self.pushButtonCek)
        self.pushButtonCek2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonCek2.setObjectName("pushButtonCek2")
        self.horizontalLayout.addWidget(self.pushButtonCek2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30 ,460,561, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelBilgi = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.labelBilgi.setObjectName("labelBilgi")
        self.horizontalLayout_2.addWidget(self.labelBilgi)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       
# =============================================================================
#        TbleWidgedtın içini tüm öğrenciler ile doldurduk 
# =============================================================================
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogrenciler""") 
        sayac=0
        self.tableWidget.clear()
        for i in im:  
            self.tableWidget.setItem(sayac,0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(sayac,1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(sayac,2, QtWidgets.QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(sayac,3, QtWidgets.QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(sayac,4, QtWidgets.QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(sayac,5, QtWidgets.QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(sayac,6, QtWidgets.QTableWidgetItem(str(i[6])))
            sayac=sayac+1
        vt.close()
# =============================================================================
#   Tc ile ilgili combo boxın içini veri tabanındaki veriler ile doldurduk      
# =============================================================================
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogrenciler""")
        for i in im:         
            self.comboBoxOgrenci.addItem(str(i[4]))
        vt.close()
# =============================================================================
#   Sınıflar ile ilgili combo boxların içini veri tabanındaki veriler ile doldurduk      
# =============================================================================
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM siniflar""")
        for i in im:         
            self.comboBoxSinif.addItem(str(i[1]))
            self.comboBoxSinif2.addItem(str(i[1]))
        vt.close()
# =============================================================================
#         Button ve commbobox click olayları
# =============================================================================
        self.comboBoxOgrenci.activated[str].connect(self.onChanged1)
        self.comboBoxSinif.activated[str].connect(self.onChanged2)
        self.comboBoxSinif2.activated[str].connect(self.onChanged3)
        self.pushButtonKamera.clicked.connect(self.yoklamaResimlerKayit)
        self.pushButtonGoster.clicked.connect(self.ogrenciBilgiGetir)
        self.pushButton.clicked.connect(self.ogrenciKayit)
        self.pushButtonResimEkle.clicked.connect(self.ogrenciResimKayit)
        self.pushButtonKamera.clicked.connect(self.yoklamaResimlerKayit)
        self.pushButtonCek.clicked.connect(self.tuzbiber)
        self.pushButtonHesap.clicked.connect(self.devamsizlikhesapla)
        self.pushButtonCek2.clicked.connect(self.getir)
# =============================================================================
# 
# =============================================================================
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# =============================================================================
# 
# =============================================================================
    def mseE(self):
        tutEslesen=0
        en_kucuk=0
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogrenciler""") 
        imageA = cv2.imread("deneme.png",1)
        for j in im:
            yol="./"+j[1]+".png"
            self.writeTofile(j[5],yol)    
            imageB = cv2.imread(""+yol+"",1)
            yeniA = cv2.resize(imageA,(imageB.shape[0],imageB.shape[1]))
            
            err = np.sum((yeniA.astype("float") - imageB.astype("float")) ** 2)
            err /= float(yeniA.shape[0] * yeniA.shape[1])
            a=err   
            
            if(en_kucuk==0):
                en_kucuk=a
            if(en_kucuk<4000):
                if(tutEslesen==0):
                    en_kucuk=a
                    tutEslesen=j[0]  
            if(a<en_kucuk): 
                en_kucuk=a 
                tutEslesen=j[0]  
        return tutEslesen,en_kucuk

# =============================================================================
# 
# =============================================================================
    def sisim(self):
        tutEslesen2=0
        en_buyuk=0
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogrenciler""") 
        imageA = cv2.imread("deneme.png",1)
        for j in im:
            yol="./"+j[1]+".png"
            self.writeTofile(j[5],yol)    
            imageB = cv2.imread(""+yol+"",1)
            yeniA = cv2.resize(imageA,(imageB.shape[0],imageB.shape[1]))
            
            (score, diff) = compare_ssim(yeniA, imageB, full=True,multichannel=True)
            diff = (diff * 255).astype("uint8")  
            
            if(en_buyuk==0):
                en_buyuk=score
            if(en_buyuk>0.5):
                if(tutEslesen2==0):
                    en_buyuk=score
                    tutEslesen2=j[0] 
            if(score>en_buyuk):
                en_buyuk=score
                tutEslesen2=j[0]
            return tutEslesen2,en_buyuk
        vt.close()
# =============================================================================
# 
# =============================================================================
    def psnr(self): 
        tutEslesen3=0
        en_buyuk=0
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogrenciler""") 
        imageA = cv2.imread("deneme.png",1)
        for j in im:
            yol="./"+j[1]+".png"
            self.writeTofile(j[5],yol)    
            imageB = cv2.imread(""+yol+"",1)
            yeniA = cv2.resize(imageA,(imageB.shape[0],imageB.shape[1]))
            
            deger=cv2.PSNR(yeniA,imageB)
            
            if(en_buyuk==0):
                en_buyuk=deger
            if(en_buyuk>15.5):
                if(tutEslesen3==0):
                    en_buyuk=tutEslesen3
                    tutEslesen3=j[0] 
            if(deger>en_buyuk):
                en_buyuk=deger
                tutEslesen3=j[0]  
            return tutEslesen3,en_buyuk
        vt.close()
# =============================================================================
# Öğrenci bilgilerini getirmek için kullandığımız fonksiyonumuz
# =============================================================================
    def ogrenciBilgiGetir(self):
        vt2 = sqlite3.connect('ogrenciler.db')
        im2 = vt2.cursor()     
        im2.execute("""SELECT * FROM ogrenciler WHERE ogrenciler.tc='"""+str(self.seciliOgrenciTc)+"""'""") 
        for i in im2:         
            self.labelAd.setText(str(i[1]))
            self.labelTC.setText(str(i[4]))
            self.labelSinif.setText(str(i[3]))
            self.labelSoyad.setText(str(i[2]))
            self.labelDevamsizlik.setText(str(i[6]))
            yol="./"+i[1]+".png"
            self.writeTofile(i[5],yol)
            self.label_6.setPixmap(QtGui.QPixmap(yol))
        vt2.close()
# =============================================================================
#  Ekle kısmındaki sınıf combo box için    
# =============================================================================
    def onChanged2(self, text):
        self.seciliSinif2 = text   
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogrenciler where sinif='"""+str(text)+"""'""")
        self.comboBoxOgrenci.clear()
        for i in im:         
            self.comboBoxOgrenci.addItem(str(i[4]))
        vt.close()
# =============================================================================
# Göster kısmındaki sınıf combo box için
# =============================================================================
    def onChanged3(self, text):
        self.seciliSinif = text    
# =============================================================================
# Tc combo box için 
# =============================================================================
    def onChanged1(self, text):
        self.seciliOgrenciTc = text   
# =============================================================================
# Öğrenciyi kayıt etmek için kullandıığımız fonk
# =============================================================================
    def ogrenciKayit(self):
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        deger1=self.lineEditAd.text()
        deger2=self.lineEditSoyad.text()
        deger3=self.seciliSinif    
        deger4=self.lineEditTC.text()
        deger6="0"
        deger5=self.convertToBinaryData(".\\"+self.ogrenciKayitResimYol)
        im.execute("""INSERT INTO  ogrenciler (ad, soyad, sinif, tc, resim, devamsizlik) VALUES (?,?,?,?,?,?)""",(deger1,deger2,deger3,deger4,sqlite3.Binary(deger5),deger6))   
        vt.commit()
        vt.close()
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogrenciler""") 
        sayac=0
        self.tableWidget.clear()
        for i in im:          
            self.tableWidget.setItem(sayac,0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(sayac,1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(sayac,2, QtWidgets.QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(sayac,3, QtWidgets.QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(sayac,4, QtWidgets.QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(sayac,5, QtWidgets.QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(sayac,6, QtWidgets.QTableWidgetItem(str(i[6])))
            sayac=sayac+1
        vt.close()
# =============================================================================
# Yoklama almak için resmin tutulması kısmı 
# =============================================================================
    def yoklamaResimlerKayit(self):
        self.zaman = datetime.datetime.today()
        self.zaman2 = QtCore.QDate.currentDate()
        sonuc=0
        kameraAcik = True
        faceCascade=cv2.CascadeClassifier( "C:\\Users\\pc\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
#        goz_cast=cv2.CascadeClassifier( "C:\\Users\\pc\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml")
        kamera = cv2.VideoCapture(0)
        while (kameraAcik):

            ret,kare=kamera.read()
            gri=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gri, 1.1, 4)   
            for (x, y, w, h) in faces:
                cv2.rectangle(kare, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow('img', kare)
            for (x, y, w, h) in faces:
                cv2.rectangle(kare, (x, y), (x + w, y + h), (0, 255, 0), 2)
                crop_img = kare[y:y + h, x:x + w]
                save_file_name = ('deneme.png')

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite(save_file_name,crop_img)
                self.label.setPixmap(QtGui.QPixmap(save_file_name))
                tutEslesen,en_kucuk= self.mseE()
                tutEslesen2,en_buyuk=self.sisim()
                tutEslesen3,en_buyuk2=self.psnr()
                en_kucuk=100-en_kucuk/100
                en_buyuk=en_buyuk*100
                en_buyuk2=en_buyuk2*100/30
                print(tutEslesen)
                print(tutEslesen2)
                print(tutEslesen3)
                if(en_kucuk>en_buyuk and en_kucuk>en_buyuk2):
                    d="Mse En Doğru-Bulunan Kişi="
                    sonuc=tutEslesen
                    print(sonuc)
                elif(en_buyuk>en_kucuk and en_buyuk>en_buyuk2):
                    d="sisim En Doğru-Bulunan Kişi="
                    sonuc=tutEslesen2
                    print(sonuc)
                elif(en_buyuk2>en_kucuk and en_buyuk2>en_buyuk):
                    d="psnr En Doğru-Bulunan Kişi="
                    sonuc=tutEslesen3
                    print(sonuc)
                print(sonuc)
                if(tutEslesen==tutEslesen2==tutEslesen3):
                    d2="Hepsi Aynı Kişiyi Buldu Veya Eşleştiremedi\t"
                elif(tutEslesen==tutEslesen2):
                    d2="Mse İle Ssim Aynı Kişiyi Buldu Veya Eşleştiremedi\t"
                elif(tutEslesen2==tutEslesen3):
                    d2="Ssim Ve Psnr Aynı Kişiyi Buldu Veya Eşleştiremedi\t"
                elif(tutEslesen==tutEslesen3):
                    d2="Mse Ve Psnr Aynı Kişiyi Buldu Veya Eşleştiremedi\t"
                else:
                    d2="Hepsi Farklı Sonuçlar Verdi \t"
                d3=str("Mse= %"+str(en_kucuk)+" ")
                d4=str("Ssim= %"+str(en_buyuk)+" ")
                d5=str("Psnr= %"+str(en_buyuk2)+" ")
                
                if(sonuc!=0):
                    print("girdi1")
                    vt = sqlite3.connect('ogrenciler.db')
                    im = vt.cursor()
                    im.execute("""SELECT * FROM ogrenciler where id='"""+str(sonuc)+"""'""")
                    for i in im:         
                        d6=str(i[1])
                    vt.close()  
                
                if(sonuc!=0):
                    print("girdi2")
                    vt2 = sqlite3.connect('ogrenciler.db')
                    im2 = vt2.cursor()

                    im2.execute("""INSERT INTO  devamsizlikDurum (ogrenciId, tarih, geldiGelmedi) VALUES ('"""+str(sonuc)+"""', '"""+str(self.zaman2.toString(QtCore.Qt.ISODate))+"""' , '"""+"1"+"""')""")   
                    vt2.commit()
                    vt2.close()     
                    vt.close()
                    print("girdi2")
                    vt2 = sqlite3.connect('ogrenciler.db')
                    im2 = vt2.cursor()
                   
                    im2.execute("""INSERT INTO  tarihkayit (tarih) VALUES ('"""+str(self.zaman2.toString(QtCore.Qt.ISODate))+"""')""")   
                    vt2.commit()
                    vt2.close()     
                    vt.close()
               
                if(sonuc!=0):
                    self.labelBilgi.setText(d+d6+d2)
                    self.labelBilgi2.setText(d3+d4+d5)
                sonuc=0
            if cv2.waitKey(33) == ord('a'):
                cv2.imwrite(save_file_name,crop_img)       
                break
       
        kamera.release()
        cv2.destroyAllWindows()
# =============================================================================
# Öğrencinin kayıt kısmında resmin çekilip tutulması işlemleri için
# =============================================================================
    def ogrenciResimKayit(self):


        kameraAcik = True
        faceCascade=cv2.CascadeClassifier( "C:\\Users\\pc\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
#        goz_cast=cv2.CascadeClassifier( "C:\\Users\\pc\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml")

        kamera = cv2.VideoCapture(0)


        while (kameraAcik):
            ret,kare=kamera.read()
            gri=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gri, 1.1, 4)     
            for (x, y, w, h) in faces:
                cv2.rectangle(kare, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow('img', kare)
            for (x, y, w, h) in faces:
                cv2.rectangle(kare, (x, y), (x + w, y + h), (0, 255, 0), 2)
                crop_img = kare[y:y + h, x:x + w]
                save_file_name = (str(self.lineEditAd.text()) + str(self.lineEditTC.text()) + '.png')

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite(save_file_name,crop_img)       
                break
        kamera.release()
        cv2.destroyAllWindows()
        self.labelEkle.setPixmap(QtGui.QPixmap(save_file_name))        
        self.ogrenciKayitResimYol=((str(self.lineEditAd.text())) + str(self.lineEditTC.text())+ ".png")
# =============================================================================
# Resmi blob data olarak kaydetmek için binary yaptık
# =============================================================================
    def convertToBinaryData(self,filename):
        #Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData
# =============================================================================
# Resmi blob veriden okumak için binary okunmak için yaptık
# =============================================================================
    def writeTofile(self,data, filename):
        with open(filename, 'wb') as file:
            file.write(data)
# =============================================================================
# Tuz biber
# =============================================================================
    def tuzbiber(self):
        img = cv2.imread('./deneme.png')
        yukseklik = img.shape[0]
        en = img.shape[1]
        print("en buyuklugu",en)      
        for j in range(0, 5000):
            x = random.randint(0, yukseklik - 1)
            y = random.randint(0, en - 1)
            islem = random.randint(0, 1)
            if (islem == 1):
                img[x, y] = 0
            else:
                img[x, y] = 255
                
        cv2.imwrite('./deneme.png', img)
        self.labelTuzBiber.setPixmap(QtGui.QPixmap("deneme.png"))
        tutEslesen,en_kucuk= self.mseE()
        tutEslesen2,en_buyuk=self.sisim()
        tutEslesen3,en_buyuk2=self.psnr()
        en_kucuk=100-en_kucuk/100
        en_buyuk=en_buyuk*100
        en_buyuk2=en_buyuk2*100/30
        print(tutEslesen)
        print(tutEslesen2)
        print(tutEslesen3)
        if(en_kucuk>en_buyuk and en_kucuk>en_buyuk2):
            d="Mse En Doğru"
            sonuc=tutEslesen
            print(sonuc)
        elif(en_buyuk>en_kucuk and en_buyuk>en_buyuk2):
            d="sisim En Doğru"
            sonuc=tutEslesen2
            print(sonuc)
        elif(en_buyuk2>en_kucuk and en_buyuk2>en_buyuk):
            d="psnr En Doğru"
            sonuc=tutEslesen3
            print(sonuc)
        print(sonuc)
        if(tutEslesen==tutEslesen2==tutEslesen3):
            d2="Hepsi Aynı Kişiyi Buldu Veya Eşleştiremedi\t"
        elif(tutEslesen==tutEslesen2):
            d2="Mse İle Ssim Aynı Kişiyi Buldu Veya Eşleştiremedi\t"
        elif(tutEslesen2==tutEslesen3):
            d2="Ssim Ve Psnr Aynı Kişiyi Buldu Veya Eşleştiremedi\t"
        elif(tutEslesen==tutEslesen3):
            d2="Mse Ve Psnr Aynı Kişiyi Buldu Veya Eşleştiremedi\t"
        else:
            d2="Hepsi Farklı Sonuçlar Verdi \t"
        d3=str("Mse= %"+str(en_kucuk)+" ")
        d4=str("Ssim= %"+str(en_buyuk)+" ")
        d5=str("Psnr= %"+str(en_buyuk2)+"")      
        sonuc=0
        self.labelBilgi.setText(d+d2)
        self.labelBilgi2.setText(d3+d4+d5) 
# =============================================================================
#         Devamsızlık hesaplama kısmı
# =============================================================================
    def devamsizlikhesapla(self):
        zaman = QtCore.QDate.currentDate()
        vt2 = sqlite3.connect('ogrenciler.db')         
        im1=vt2.cursor()
        im1.execute("""SELECT * FROM devamsizlikDurum where tarih='"""+str(zaman.toString(QtCore.Qt.ISODate))+"""'""")
        for j in im1:
            vt = sqlite3.connect('ogrenciler.db')         
            im=vt2.cursor()
            print(str(j[1]))
            im.execute("""UPDATE ogrenciler SET devamsizlik = devamsizlik +1 WHERE ogrenciler.id='"""+str(j[1])+"""'""")   
            vt.commit()
            vt.close()
        vt2.close() 
# =============================================================================
#         devamsızlıkları getirmek için
# =============================================================================
    def getir(self):
        self.tableWidget.clear()
        vt = sqlite3.connect('ogrenciler.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM devamsizlikDurum""") 
        sayac=0
        self.tableWidget.clear()
        for i in im:          
            self.tableWidget.setItem(sayac,0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(sayac,1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(sayac,2, QtWidgets.QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(sayac,3, QtWidgets.QTableWidgetItem(str(i[3])))
            sayac=sayac+1
        vt.close()
# =============================================================================
#         
# =============================================================================
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Camera"))
        self.label_6.setText(_translate("MainWindow", "Resim"))
        self.label_7.setText(_translate("MainWindow", "Öğrenciler"))
        self.pushButtonGoster.setText(_translate("MainWindow", "Göster"))
        self.label_8.setText(_translate("MainWindow", "Sınıflar"))
        self.label_9.setText(_translate("MainWindow", "Soyad"))
        self.label_10.setText(_translate("MainWindow", "Ad"))
        self.label_13.setText(_translate("MainWindow", "Sinif"))
        self.label_12.setText(_translate("MainWindow", "TC"))
        self.label_5.setText(_translate("MainWindow", "Öğrencinin Geldiği Gün Sayısı"))
        self.labelEkle.setText(_translate("MainWindow", "Resim cek"))
        self.pushButtonResimEkle.setText(_translate("MainWindow", "Resim cek"))
        self.pushButtonHesap.setText(_translate("MainWindow", "Devamsızlık Hesapla"))
        self.pushButtonCek2.setText(_translate("MainWindow", "Devamsızlık Getir"))
        self.label_3.setText(_translate("MainWindow", "Soyad"))
        self.label_11.setText(_translate("MainWindow", "Sinif"))
        self.label_4.setText(_translate("MainWindow", "TC"))
        self.label_2.setText(_translate("MainWindow", "Ad"))
        self.pushButton.setText(_translate("MainWindow", "Öğrenci Ekle"))
        self.pushButtonKamera.setText(_translate("MainWindow", "Kamera Aç"))
        self.pushButtonCek.setText(_translate("MainWindow", "Tuz Biber"))
# =============================================================================
# 
# =============================================================================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# =============================================================================
# 
# =============================================================================
