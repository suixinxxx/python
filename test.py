# # import copy
# # a =1
# # b=copy.deepcopy(a)
# #
# # a,b= 2,3
# # m = a if a>b else b
# # print (m)
#
# # -*- coding: utf-8 -*-
#
# import re
#
#
# class CheckUserInfo:
#
#     def check_mail(self, mail):
#         flag = False
#         str = '^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
#         if re.match(str, mail):
#             flag = True
#
#         return flag
#
#     def check_pwd_len(self, pwd):
#         '''密码长度不超过8位'''
#         return len(pwd)>=8
#
#     def check_pwd_contain_leter(self, pwd):
#         '''密码包含大小写英文字母'''
#         flag = False
#         pattern = re.compile('[A-Z][a-z]+')
#         match = pattern.findall(pwd)
#
#         if match:
#             flag = True
#         return flag
#
#     def check_pwd_contain_num(self, pwd):
#         '''密码包含数字'''
#         flag = False
#         pattern = re.compile('[0-9]+')
#         match = pattern.findall(pwd)
#         if match:
#             flag = True
#         return flag
#
# # -*- coding: utf-8 -*-
#
# import unittest
#
# #from com.unit_test.check_user_info import CheckUserInfo
#
# class CheckUserInfoTestCase(unittest.TestCase):
#
#     def __init__(self, *args, **kwargs):
#         super(CheckUserInfoTestCase, self).__init__(*args, **kwargs)
#         self.check_user_info = CheckUserInfo()
#
#     @classmethod
#     def setUpClass(cls):
#         print('setUpClass\n\n')
#
#     @classmethod
#     def tearDownClass(cls):
#         print('tearDownClass')
#
#     def setUp(self):
#         print('setUp')
#
#     def tearDown(self):
#         print('tearDown\n')
#
#     def test_check_mail(self):
#         print('test_check_mail')
#         self.assertEqual(True, self.check_user_info.check_mail('aa@bb'))
#         self.assertEqual(False, self.check_user_info.check_mail('aa.bb'))
#
#     def test_check_pwd_len(self):
#         print('test_check_pwd_len')
#         self.assertEqual(True, self.check_user_info.check_pwd_len('12345678'))
#         self.assertEqual(False, self.check_user_info.check_pwd_len(''))
#         self.assertEqual(False, self.check_user_info.check_pwd_len('1'))
#         self.assertEqual(True, self.check_user_info.check_pwd_len('123456789'))
#
#     def test_check_pwd_contain_letter(self):
#         print('test_check_pwd_contain_leter')
#         self.assertEqual(True, self.check_user_info.check_pwd_contain_leter('1qazXSW@'))
#         self.assertEqual(False, self.check_user_info.check_pwd_contain_leter('12345678'))
#         self.assertEqual(False, self.check_user_info.check_pwd_contain_leter(''))
#
#     def test_check_pwd_contain_num(self):
#         print('test_check_pwd_contain_num')
#         self.assertEqual(True, self.check_user_info.check_pwd_contain_num('1qazXSW@'))
#         self.assertEqual(False, self.check_user_info.check_pwd_contain_num('qwertasdfg'))
#         self.assertEqual(False, self.check_user_info.check_pwd_contain_num(''))
#
#     def aaa(self):
#         print('test_check_pwd_contain_num')
#         self.assertEqual(True, self.check_user_info.check_pwd_contain_num('1qazXSW@'))
# if __name__ == '__main__':
#     unittest.main()

