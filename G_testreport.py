
import unittest
import HTMLTestRunner
import os
from D_classmethod import SearchTests
from E_homepage_elements import HomePageTest

dir = os.getcwd()

x = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
y = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
z = unittest.TestSuite([x, y])
outfile = open("SmokeTestReport.html", "w")
r = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report',description='Smoke Tests')
r.run(z)
