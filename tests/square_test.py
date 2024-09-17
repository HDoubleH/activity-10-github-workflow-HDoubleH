import unittest 
from square import Square

class SquareTestCase(unittest.TestCase): 

    # TODO #1
    # pre-condition: a square instantiated with a negative side 
    # post-condition: the square's side is set to 1
    def testNegativeSide(self):
        pass

    # TODO #2
    # pre-condition: a square instantiated with side set to zero
    # post-condition: the square's side is set to 1
    def testZeroSide(self):
        pass

    # TODO #3    
    # pre-condition: a square instantiated with side set to 1
    # post-condition: the square's side is set to 1
    def testUnitarySide(self):
        pass

    # TODO #4
    # pre-condition: a square instantiated with side set to 1
    # post-condition: the square's area is 1
    def testUnitarySideForArea(self):
        pass

    # TODO #5
    # pre-condition: a square instantiated with side set to 1
    # post-condition: the square's perimeter is 4
    def testUnitarySideForPerimetyer(self):
        pass

    # TODO #6
    # pre-condition: a square instantiated with side set to 2
    # post-condition: the square's area is 4
    def testArbitrarySideForArea(self):
        pass

    # TODO #7
    # pre-condition: a square instantiated with side set to 2
    # post-condition: the square's perimeter is 8
    def testArbitrarySideForPerimetyer(self):
        pass

if __name__ == '__main__':
    unittest.main(start_dir='src')