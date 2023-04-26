import unittest
import os
from NAIST_lecture_CI_CD.CSVPrinter import CSVPrinter

def setupmodule():
    print('Running setUpModule')
def teardownmodule():
    print('Running tearDownModule')

class TestCSVPrinter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Running setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("Running tearDownClass")
    def setUp(self):
        print("Running setUp")
    def tearDown(self):
        print("Running tearDown")
    def test_read_1(self):
        printer = CSVPrinter("./test/sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))