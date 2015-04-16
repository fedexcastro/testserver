import unittest
from server import Server


class TestMySQLServer(unittest.TestCase):

    def setUp(self):
        self.server = Server()

    def tearDown(self):
        self.server.shut_down()

    def test_register(self):
        expected_msg = u"<html><head></head><body>Thank you for registering ironman</body></html>"
        result = self.server.handle_request({'action': 'register',
                                             'username': 'ironman',
                                             'password': 'superhero',
                                             'format': 'html',
                                             'db': 'default'})
        self.assertEqual(result, expected_msg, u"Invalid output")
        # This is not enough, I should open the db and do a query like:
        # SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'ironman')
        # And if returns a 1 then, the user was created.

    def test_register_invalid_db(self):
        pass

    def test_login(self):
        expected_msg = u"<html><head></head><body>Login OK</body></html>"
        result = self.server.handle_request({'action': 'login',
                                             'username': 'ironman',
                                             'password': 'superhero',
                                             'format': 'html',
                                             'db': 'default'})
        self.assertEqual(result, expected_msg, u"Invalid output")

    def test_login_invalid_username(self):
        pass

    def test_login_invalid_password(self):
        pass

    def test_login_empty_username_and_password(self):
        pass

    def test_execute_sql(self):
        pass

    def test_execute_invalid_sql(self):
        pass

    def test_output_json_format(self):
        pass

    def test_output_html_format(self):
        pass

if __name__ == '__main__':
    unittest.main()