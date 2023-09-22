|Test ID                  | Input              |  Expected Results        |  Actual Results        | Pass or Fail  |
|-------------------------|--------------------|--------------------------|------------------------|---------------|
|testEquilateralTriangles |1,1,1| Equilateral| Equilateral| Pass|
|testInvalidInputA |.1,1,1|InvalidInput|InvalidInput|Pass|
|testInvalidInputB  |1,.1,1|InvalidInput|InvalidInput|Pass|
|testInvalidInputC  |1,1,.1|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleMaxA  |201,150,150|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleMaxB  |150,201,150|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleMaxC  |150,150,201|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleNegativesA  |-1,1,1|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleNegativesB  |1,-1,1|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleNegativesC  |1,1,-1|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleShort  |10,1,1|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleShortB  |1,10,1|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleShortC  |1,1,10|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleZerosA  |0,1,1|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleZerosB  |1,0,1|InvalidInput|InvalidInput|Pass|
|testInvalidTriangleZerosC  |1,1,0|InvalidInput|InvalidInput|Pass|
|testIsoscelesTriangleA |3,3,5|Isosceles|Isosceles|Pass|
|testIsoscelesTriangleB  |3,5,3|Isosceles|Isosceles|Pass|
|testIsoscelesTriangleC  |5,3,3|Isosceles|Isosceles|Pass|
|testRightTriangleA  |3,4,5|Right|Right|Pass|
|testRightTriangleB  |5,3,4|Right|Right|Pass|
|testRightTriangleC  |4,3,5|Right|Right|Pass|
|testScaleneTriangleA   |4,5,6|Scalene|Scalene|Pass|
|testScaleneTriangleB   |6,5,4|Scalene|Scalene|Pass|
|testScaleneTriangleC   |5,6,4|Scalene|Scalene|Pass|
