import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from tas_kagıt_makas import *
import random as rd
from durum_kontrol import *

secenekler = ["Taş", "Kağıt", "Makas"]
bilgisayar_secimi = any
tur_sayaci = 0
oyuncu_skoru = 0
ai_skoru = 0
sonucText = ""
oyun = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

tur_sayisi = ui.tursayisi
oyuncu_secimi = ""

def defaultState():
    global sonucText
    global tur_sayaci
    global ai_skoru
    global oyuncu_skoru
    ui.btnTas.setDisabled(True)
    ui.btnKagit.setDisabled(True)
    ui.btnMakas.setDisabled(True)
    ui.btnoyunabasla.setDisabled(False)
    ui.tursayisi.setDisabled(False)
    sonucText = ""
    ai_skoru = 0
    oyuncu_skoru = 0
    tur_sayaci = 0

def onRunningState():
    ui.btnTas.setDisabled(False)
    ui.btnKagit.setDisabled(False)
    ui.btnMakas.setDisabled(False)
    ui.btnoyunabasla.setDisabled(True)
    ui.tursayisi.setDisabled(True)

def makasClick():
    runBusiness("Makas")


def tasClick():
    runBusiness("Taş")


def kagitClick():
    runBusiness("Kağıt")

defaultState()

ui.btnKagit.clicked.connect(kagitClick)
ui.btnMakas.clicked.connect(makasClick)
ui.btnTas.clicked.connect(tasClick)


def getChoosenSit(name):
    if (name == "Taş"):
        return Tas()
    elif (name == "Makas"):
        return Makas()
    elif (name == "Kağıt"):
        return Kagit()


def checkWinner(choosenByUser: SituationBase, choosenByPc: SituationBase):
    if (choosenByUser.WinSit == choosenByPc.LoseSit):
        global oyuncu_skoru
        oyuncu_skoru +=1
        return "Siz Kazandınız"

    elif (choosenByUser.LoseSit == choosenByPc.WinSit):
        global ai_skoru
        ai_skoru += 1
        return "Bilgisayar Kazandı"
    else:
        return "Berabere"


def runBusiness(choosen):
    global bilgisayar_secimi
    global tur_sayaci
    global sonucText
    global final_res
    global ai_skoru
    global oyuncu_skoru
    
    bilgisayar_secimi = ""
    # Tur sayısı
    try:
        tur_sayisi = int(ui.tursayisi.text())
    except:
        print("Lütfen bir Sayı Giriniz !")
    tur_sayaci += 1

    bilgisayar_secimi = rd.choice(secenekler)

    choosenByPc = getChoosenSit(bilgisayar_secimi)
    choosenByUser = getChoosenSit(choosen)

    if choosen not in secenekler:
        print("Lütfen sadece taş, kağıt veya makasdan birini seçiniz!")
        return

    winner = checkWinner(choosenByUser, choosenByPc)


    sonucText += f"---------TUR {tur_sayaci}----------" + "\n" + f"Kazanan :  {winner}" + "\n" + f"Sonuç: " + "\n" + f"Siz: {oyuncu_skoru}" + "\n" + f"----Bilgisayar: {ai_skoru}----" + "\n"
 
       
    ui.sonuclar.setText(sonucText)

    if tur_sayaci == tur_sayisi: 
        defaultState()
        return

def oyun_basla():
    ui.sonuclar.setText(sonucText)
    onRunningState()


ui.btnoyunabasla.clicked.connect(oyun_basla)
sys.exit(oyun.exec_())
