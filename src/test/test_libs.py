import unittest
from src.libs import Libs


class TddLibs(unittest.TestCase):

    def test_authentication(self):
        action = Libs.authentication('morteza', '123')
        self.assertIsInstance(action, list)

        action = Libs.authentication('sara', '225')
        self.assertIsInstance(action, list)

    def test_get_users_list(self):
        self.assertIsInstance(Libs.get_users_list(), list)

    def test_check_user_existence(self):
        sample_data = Libs.check_user_existence(('sample', 'sample@email.local'))
        self.assertIsInstance(sample_data, list)
        self.assertIsInstance(sample_data[0], bool)
        self.assertIsInstance(sample_data[1], bool)

        sample_data = Libs.check_user_existence(('sample@email.local', 'sample'))
        self.assertIsInstance(sample_data, list)
        self.assertIsInstance(sample_data[0], bool)
        self.assertIsInstance(sample_data[1], bool)

    def test_check_data(self):
        sample = Libs.check_data('sample', 'username')
        self.assertTrue(sample)

        sample = Libs.check_data('saample_me2', 'username')
        self.assertTrue(sample)

        sample = Libs.check_data('sample@email', 'email')
        self.assertFalse(sample)

        sample = Libs.check_data('sample_22#@.local', 'email')
        self.assertFalse(sample)

        sample = Libs.check_data('sample_m2@email.local', 'email')
        self.assertTrue(sample)

    def test_create_user(self):
        action = Libs.create_user('sample', '123', 'sample@email.local')
        self.assertIn(action, ('register_suc', 'register_err', 'exist_err'))

        action = Libs.create_user('samp_$_2', '123', 'sample@invalid$local')
        self.assertEquals(action, 'data_err')

if __name__ == "__main__":
    unittest.main()
