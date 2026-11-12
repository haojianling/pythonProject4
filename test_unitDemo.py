import unittest
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("")
    def setUp(self) -> None:
        print("setup")
    def tearDown(self) -> None:
        print("teardown")
    def test_case01(self):
        print("testcase01")
        # self.assertEqual(1,2,"判断相等")
        self.assertIn('h','this')
class demo1(unittest.TestCase):
    def test_case_demo1(self):
        print("test_case-demo1")
    def test_case_demo2(self):
        print("test_case_demo2")
if __name__ == '__main__':
    # unittest.mian()
    suit=unittest.TestSuite()
    suit.addTest(demo("test_case01"))
    unittest.TextTestRunner().run(suit)
