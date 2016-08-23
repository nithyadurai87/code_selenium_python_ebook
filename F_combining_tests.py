
import unittest
from D_classmethod import SearchTests
from E_homepage_elements import HomePageTest

x = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
y = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
z = unittest.TestSuite([x, y])
unittest.TextTestRunner(verbosity=2).run(z)
