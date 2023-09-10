"""
Author: Russ Harrington
Date: 2023-09-10
Assignment HW-01 Testing triangle classification
    Write a function classify_triangle() that takes three  parameters: a, b, and c. 
    The three parameters represent the lengths of the sides of a triangle. 
    The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral, and whether it is a right triangle as well.”
"""

import math
import unittest

#################################
# constants
#################################

EQUILATERAL_TRIANGLE = 'Equilateral'
INVALID_TRIANGLE = 'Invalid'
ISOSCELES_TRIANGLE = 'Isosceles'
RIGHT_ISOSCELES_TRIANGLE = 'Right Isosceles'
RIGHT_SCALENE_TRIANGLE = 'Right Scalene'
SCALENE_TRIANGLE = 'Scalene'


#################################
# Functions
#################################

def classify_triangle(a, b, c):
    """
    Classifies a triangle given three sides:
        - Equilateral Triangle: have all three sides with the same length
        - Isosceles Triangle: have two sides with the same length
        - Scalene Triangle: Three sides with different lengths 
        - Right Triangle: Three sides with lengths a, b, and c where a2 + b2 = c2
        - Invalid if the sum of two sides are not greater than the third side

     Note: Right triangles for the purpose of this exercise have 
            the significant digits rounded to 15 places. 
    """
    # normalize inputs so that c is the largest always
    a, b, c = sorted([a, b, c])

    # identify triangle
    if a + b <= c:
        return INVALID_TRIANGLE
    elif a == b and b == c:
        return EQUILATERAL_TRIANGLE
    elif round(a*a,15) + round(b*b,15) == round(c*c,15):
        if a != b != c:
            return RIGHT_SCALENE_TRIANGLE
        else:
            return RIGHT_ISOSCELES_TRIANGLE
    elif a != b != c:
        return SCALENE_TRIANGLE
    else:
        return ISOSCELES_TRIANGLE


#################################
# Tests Methods
#################################
class TestTriangles(unittest.TestCase):

    def test_valid_equilateral(self):
        self.assertEqual(classify_triangle(1,1,1), EQUILATERAL_TRIANGLE, "Should be an Equilateral Triangle")
        self.assertEqual(classify_triangle(3,3,3), EQUILATERAL_TRIANGLE, "Should be an Equilateral Triangle")
        self.assertEqual(classify_triangle(.1,.1,.1), EQUILATERAL_TRIANGLE, "Should be an Equilateral Triangle")

    def test_valid_scalene(self):
        # test normal scalene
        self.assertEqual(classify_triangle(4,5,6), SCALENE_TRIANGLE, "Should be a Scalene Triangle")
        self.assertEqual(classify_triangle(6,5,4), SCALENE_TRIANGLE, "Should be a Scalene Triangle")
        self.assertEqual(classify_triangle(4,6,5), SCALENE_TRIANGLE, "Should be a Scalene Triangle")
        #test right scalene
        self.assertEqual(classify_triangle(3,4,5), RIGHT_SCALENE_TRIANGLE, "Should be a Scalene Right Triangle")
        self.assertEqual(classify_triangle(5,4,3), RIGHT_SCALENE_TRIANGLE, "Should be a Scalene Right Triangle")
        self.assertEqual(classify_triangle(4,5,3), RIGHT_SCALENE_TRIANGLE, "Should be a Scalene Right Triangle")

    def test_valid_isosceles(self):
        self.assertEqual(classify_triangle(1,1,math.sqrt(2)), RIGHT_ISOSCELES_TRIANGLE, "Should be a Scalene Right Triangle")
        self.assertEqual(classify_triangle(3,3,5), ISOSCELES_TRIANGLE, "Should be an Isosceles Triangle")
        self.assertEqual(classify_triangle(5,3,3), ISOSCELES_TRIANGLE, "Should be an Isosceles Triangle")
        self.assertEqual(classify_triangle(3,5,3), ISOSCELES_TRIANGLE, "Should be an Isosceles Triangle")

    def test_edges(self):
        self.assertEqual(classify_triangle(3,3,6), INVALID_TRIANGLE, "Should be an Invalid Triangle")
        self.assertEqual(classify_triangle(-3,3,6), INVALID_TRIANGLE, "Should be an Invalid Triangle")
        self.assertEqual(classify_triangle(-1,-1,-1), INVALID_TRIANGLE, "Should be an Invalid Triangle")
        self.assertEqual(classify_triangle(0,1,1), INVALID_TRIANGLE, "Should be an Invalid Triangle")
        

#################################
# Main / entry methods
#################################

def main():
    """Main Function"""
    #Run functions
    print('Running function with different parameters')

    a, b, c =[1, 1, 1]
    print('Triangle with sides a={}, b={}, c={} is : {}'.format(a,b,c, classify_triangle(a,b,c)))

    a, b, c =[4, 5, 6]
    print('Triangle with sides a={}, b={}, c={} is : {}'.format(a,b,c, classify_triangle(a,b,c)))

    a, b, c =[3, 4, 5]
    
    print('Triangle with sides a={}, b={}, c={} is : {}'.format(a,b,c, classify_triangle(a,b,c)) )

    a, b, c =[1, 1, math.sqrt(2)]
    print('Triangle with sides a={}, b={}, c={} is : {}'.format(a,b,c, classify_triangle(a,b,c)) )

    a, b, c =[3, 3, 5]
    print('Triangle with sides a={}, b={}, c={} is : {}'.format(a,b,c, classify_triangle(a,b,c)) )
    


    #Run Test Methods
    print('\nRunning Unit Tests:')
    unittest.main(exit=True)


if __name__ == '__main__':
    main()
