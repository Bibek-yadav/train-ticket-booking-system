from register import *
from Gui import *
import unittest



class Testing(unittest.TestCase):

    def test_login(self):
        login = Register()
        result = login.login_backend('bibek', 'rollon')
        self.assertEqual((len(result)), 0)

    def test_login1(self):
        login = Register()
        result = login.login_backend('bittu', '123')
        self.assertEqual((len(result)), 1)

    def test_add(self):
        login = Register()
        result = login.getting('yadav', 'exporer', 'bibekyadav', 'lahan', '980778743', 'yadav7@gmail.com')
        self.assertTrue(result)

    def test_add1(self):
        login = Register()
        result = login.getting('yadav', 'explrer', '', 'lahan', '980678743', 'yadav7@gmail.com')
        self.assertFalse(result)

    def test_addtrain1(self):
        login = Railway()
        result = login.register_train('ss', 'ss', '', 'ssf', 'ff', 'iii')
        self.assertFalse(result)

    def test_addtrain2(self):
        login = Railway()
        result = login.register_train('ss', 'ss', 'dd', 'ssf', 'ff', 'iii')
        self.assertTrue(result)

    def test_deltrain1(self):
        login = Railway()
        result = login.delete_item(10)
        self.assertTrue(result)

    def test_deltrain2(self):
        login = Railway()
        result = login.delete_item('ss')
        self.assertFalse(result)

    def test_updtrain1(self):
        login = Railway()
        result = login.update_item('ss','ss', 'ss', 'dd', 'ssf', 'ff', '1')
        self.assertTrue(result)

    def test_updtrain2(self):
        login = Railway()
        result = login.update_item('ss','ss', 'ss', 'dd', 'ssf', 'ff', '')
        self.assertFalse(result)





