'''
Created on 16 de abr de 2018

@author: gdiamante
'''
import unittest
import pyautogui
import time

class Test(unittest.TestCase):

    
    def testName(self):
        pyautogui.moveTo(0,3)
        time.sleep(2)
        pyautogui.moveTo(0,7)
        time.sleep(2)
        pyautogui.moveTo(10,11)
        time.sleep(2)
        pyautogui.moveTo(11,13)
        time.sleep(2)
        pyautogui.moveTo(943,93)
        time.sleep(2)
        pyautogui.moveTo(29,123)
        time.sleep(2)
        pyautogui.moveTo(49,500)
        time.sleep(2)
        pyautogui.moveTo(32,939)
        time.sleep(2)
        pyautogui.moveTo(199,1000)
        time.sleep(2)
        pyautogui.moveTo(1200,30)
        time.sleep(2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()