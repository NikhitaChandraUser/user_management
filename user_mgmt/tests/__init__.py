import sys
from os.path import abspath, dirname, join

package_path = abspath(dirname(dirname(__file__)))
sibling_dir = 'mgmt'

sys.path.insert(0, join(package_path, sibling_dir))


# import unittest, test_group, test_user, test_all_users_and_groups, test_json_reader, test_excel_reader, test_xls_writer,\
#     test_sync, test_privs
#
# test_cases = [test_group, test_user, test_all_users_and_groups, test_json_reader, test_excel_reader, test_xls_writer,
#               test_sync, test_privs]
#
#
# def my_module_suite():
#     loader = unittest.TestLoader()
#     suite = unittest.TestSuite()
#     for test_case in test_cases:
#         suite.addTests(loader.loadTestsFromModule(test_case))
#     return suite
#
