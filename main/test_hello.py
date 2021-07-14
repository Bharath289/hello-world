import unittest

class MyTestCase(unittest.TestCase):
    def test_hello_message(self):
        self.assertEqual("hello, CIS 189",hello_world.hello_message())

if __name__ =='__main__':
    unittest.main()