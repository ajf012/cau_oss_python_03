"""
class line을 불러온 뒤 __length 값을 set_length(), get_length()를 이용해 받고 
이를 area_rectangle(), area_regular_triangle(), area_ellipse()의 매개변수로 설정하여
각각 직사각형의 넓이, 직각삼각형의 넓이, 타원의 넓이를 구한다.
"""

import figure
"""
figure 모듈 전체를 가져온다.
"""
myline = figure.line(10, 20)
"""
class line을 불러온 뒤 __width=10, __height=20으로 설정한다.
"""
width, height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("please input positive number for width and height")
"""
직사각형 넓이를 구하는 함수를 매개변수로 받은 width나 height의 값이 0이하일 경우 ValueError를 발생시킨다."""

myline.set_length(20, 30)
width, height = myline.get_length()
try:
    triangle = figure.area_regular_triangle(width, height)
    print(triangle)
except ValueError:
    print("please input positive number for width and height")
"""
직각삼각형 넓이를 구하는 함수를 매개변수로 받은 width나 height의 값이 0이하일 경우 ValueError를 발생시킨다."""

myline.set_length(30, 40)
width, height = myline.get_length()
try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("please input positive number for width and height")
"""
타원의 넓이를 구하는 함수를 매개변수로 받은 width나 height의 값이 0이하일 경우 ValueError를 발생시킨다."""