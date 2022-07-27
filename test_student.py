import unittest
from datetime import timedelta
from student import Student


class TestStudent(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     pass

    # @classmethod
    # def tearDownClass(cls):
    #     pass

    def setUp(self):
        self.student = Student('John', 'Doe')

    def tearDown(self):
        pass

    def test_full_name(self):
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_email(self):
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_alert_santa(self):
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extention(2)
        self.assertEqual(self.student.end_date,
                         old_end_date + timedelta(days=2))


if __name__ == '__main__':
    unittest.main()
