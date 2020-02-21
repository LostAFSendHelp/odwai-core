# 
# Master class, contains all surfaces functions: get, static/realtime, simulate
# Called by odwai_app to present functions to GUI
# Calls: detector for static/realtime; frame for get; simulator for simulation
# 

from tkinter import *
from odwai_frame import CustomFrame as cf

from PyQt5 import QtWidgets

import odwai_detector as dtct
import odwai_simulator as simulator
import threading

class Master:
    
    def __init__(self, top, left, width, height):
        self.captureTop = top
        self.captureLeft = left
        self.captureWidth = width
        self.captureHeight = height
        self.skip_check = False
        self.p1 = { "x": 0, "y": 0 }
        self.p2 = { "x": 0, "y": 0 }
        self.string = "{} x {}"
        self.detector = dtct.Detect_img()

    def callCapture(self):
        "this thing calls the capture function - on the whole screen, it's not optimized, will be replaced later"
        self.detector.capture_n_detect(self.captureTop, self.captureLeft, self.captureWidth, self.captureHeight, self.skip_check)
        if self.skip_check:
            self.callTbSimulate()

    def btnCaptureClick(self):
        "what happens on a click on btnCapture"
        captureThread = threading.Thread(target=self.callCapture, args=())
        captureThread.start()
        self.string = "{} x {}"

    def callTbSimulate(self):
        print(self.detector.objects)
        simulator.tb_simulator(self.detector.objects["tb"])
        simulator.btn_simulator(self.detector.objects["btn"])

    def callRealtime(self):
        "this thing calls the capture function - on the whole screen, it's not optimized, will be replaced later"
        self.detector.capture_n_detect_realtime(self.captureTop, self.captureLeft, self.captureWidth, self.captureHeight)

    # def btnRealtimeClick(self):
    #     "what happens on a click on btnCapture"
    #     captureThread = threading.Thread(target=self.callRealtime, args=())
    #     captureThread.start()

    def btnGetClick(self):
        "get something fun"
        self.__run(self.p1, self.p2)
        self.captureTop = min(self.p1["y"], self.p2["y"])
        self.captureLeft = min(self.p1["x"], self.p2["x"])
        self.captureWidth = abs(self.p1["x"]-self.p2["x"])
        self.captureHeight = abs(self.p1["y"]-self.p2["y"])
        print(self.string)

    def __get_values(self, cf):
        self.p1 = cf.point1
        self.p2 = cf.point2
        
    def __run(self, point1, point2):
        app = QtWidgets.QApplication(sys.argv)
        window = cf(point1, point2)
        window.show()
        app.aboutToQuit.connect(lambda: self.__get_values(window))
        app.exec_()