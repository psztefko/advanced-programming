from student import Student
from library import Library
from order import Order
from employee import Employee
from book import Book
from datetime import date
from property import Property
from house import House

#task_1
s1 = Student('John', 60)
s2 = Student('Alice', 40)
s3 = Student('Bea', 80)

#task_2
l1 = Library('Katowice', 'Uniwersytecka', '40-001', '10-18', '111222333')
l2 = Library('Krakow', 'Szpitalna', '32-540', '8-16', '123456789')

b1 = Book(l1, date(2003, 8, 29), 'Author_name1', 'Author_surname1', 420)
b2 = Book(l1, date(2007, 11, 20), 'Author_name2', 'Author_surname2', 360)
b3 = Book(l1, date(2005, 3, 15), 'Author_name3', 'Author_surname3', 530)
b4 = Book(l2, date(2010, 7, 13), 'Author_name4', 'Author_surname4', 124)
b5 = Book(l2, date(2015, 1, 25), 'Author_name5', 'Author_surname5', 910)

e1 = Employee('Employee_name1', 'Employee_last_name1', date(2018, 3, 12), date(1998, 3, 10), 'Katowice', '1 maja', '40-006', '123123123')
e2 = Employee('Employee_name2', 'Employee_last_name2', date(2015, 2, 19), date(1994, 4, 1), 'Katowice', '3 maja', '40-008', '123123123')
e3 = Employee('Employee_name3', 'Employee_last_name3', date(2020, 1, 4), date(2002, 8, 21), 'Katowice', 'Mariacka', '40-002', '123123123')

o1 = Order(e1, s1, (b1, b2, b3), date(2021, 10, 26))
o1 = Order(e3, s3, (b1, b4, b5), date(2021, 10, 27))


# task_3

p1 = Property(35, 2, 1800, 'Centrum')
h1 = House(p1.area, p1.rooms, p1.price, p1.address, 200)

print(h1.__str__())


