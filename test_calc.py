import unittest
import calc


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(2, 8), 10)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        
if __name__ == '__main__':
    unittest.main() 