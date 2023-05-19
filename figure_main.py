"""
class line을 불러온 뒤 __length 값을 set_length(), get_length()를 이용해 받고 
이를 area_square(), area_regular_triangle(), area_circle()의 매개변수로 설정하여
각각 정사각형의 넓이, 정삼각형의 넓이, 원의 넓이를 구한다.
"""
import figure
"""
figure 모듈 전체를 가져온다.
"""

myline = figure.line(10)
"""
class line을 불러온 뒤 __length=10으로 설정한다.
"""

square = figure.area_square(myline.get_length())
print(square)
"""
get_length()를 이용하여 __length의 값을 받고
이를 정사각형의 넓이를 구하는 함수 area_square()의 
매개변수로 설정하여 정사각형의 넓이를 구한다.
"""

myline.set_length(20)
regular_triangle = figure.area_regular_triangle(myline.get_length())
print(regular_triangle)
"""
set_length()를 이용하여 __length의 값을 수정하고
get_length()를 이용하여 __length의 값을 받은 뒤
이를 정삼각형의 넓이를 구하는 함수 area_regular_triangle()의
매개변수로 설정하여 정삼각형의 넓이를 구한다.
"""

myline.set_length(30)
circle = figure.area_circle(myline.get_length())
print(circle)
"""
set_length()를 이용하여 __length의 값을 수정하고
get_length()를 이용하여 __length의 값을 받은 뒤
이를 원의 넓이를 구하는 함수 area_circle()의 
매개변수로 설정하여 원의 넓이를 구한다.
"""