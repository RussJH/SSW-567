# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    #######################
    # Right Triangle tests
    #######################
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,3,5),'Right','5,3,4 is a Right triangle')
        
    #######################
    # Equilateral Triangle tests
    #######################
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    #######################
    # Isosceles Triangle tests
    #######################
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,3,5 should be an isosceles triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(3,5,3),'Isosceles','3,5,3 should be an isosceles triangle')
    
    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(5,3,3),'Isosceles','3,5,3 should be an isosceles triangle')

    #######################
    # Scalene Triangle tests
    #######################
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 should be scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(6,4,5),'Scalene','6,4,5 should be scalene triangle')
    
    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(5,6,4),'Scalene','5,6,4 should be scalene triangle')

    #######################
    # Invalid Triangle Zero value tests
    #######################
    def testInvalidTriangleZerosA(self):
        self.assertEqual(classifyTriangle(0,1,1),'InvalidInput','0,1,1 is invalid input')
    
    def testInvalidTriangleZerosB(self):
        self.assertEqual(classifyTriangle(1,0,1),'InvalidInput','1,0,1 is invalid input')

    def testInvalidTriangleZerosC(self):
        self.assertEqual(classifyTriangle(1,1,0),'InvalidInput','1,1,0 is invalid input')

    #######################
    # Invalid Triangle Over maximum value tests
    #######################

    def testInvalidTriangleMaxA(self):
        self.assertEqual(classifyTriangle(201,150,150),'InvalidInput','200,150,150 is invalid input')
    
    def testInvalidTriangleMaxB(self):
        self.assertEqual(classifyTriangle(150,201,150),'InvalidInput','200,150,150 is invalid input')

    def testInvalidTriangleMaxC(self):
        self.assertEqual(classifyTriangle(150,150,201),'InvalidInput','150,150,200 is invalid input')

    #######################
    # Invalid Triangle negative value tests
    #######################

    def testInvalidTriangleNegativesA(self):
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','-1,1,1 is invalid input')

    def testInvalidTriangleNegativesB(self):
        self.assertEqual(classifyTriangle(1,-1,1),'InvalidInput','1,-1,1 is invalid input')

    def testInvalidTriangleNegativesC(self):
        self.assertEqual(classifyTriangle(1,1,-1),'InvalidInput','1,1,-1 is invalid input')

    #######################
    # Invalid Args tests
    #######################
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(.1,1,1),'InvalidInput','.1,1,1 has invalid args')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(1,.1,1),'InvalidInput','1,.1,1 has invalid args')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(1,1,.1),'InvalidInput','1,1,.1 has invalid args')


    #######################
    # NotATriangle tests
    #######################
    def testInvalidTriangleShort(self):
        self.assertEqual(classifyTriangle(10,1,1),'NotATriangle','1,1,1 should be NotATriangle')

    def testInvalidTriangleShortB(self):
        self.assertEqual(classifyTriangle(1,10,1),'NotATriangle','1,1,1 should be NotATriangle')

    def testInvalidTriangleShortC(self):
        self.assertEqual(classifyTriangle(1,1,10),'NotATriangle','1,1,1 should be NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

