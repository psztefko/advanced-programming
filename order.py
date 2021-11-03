from employee import Employee
from student import Student
from datetime import date


class Order():

    def __init__(self, employee: Employee, student: Student,
                 books: list, order_date: date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Order processed by {self.employee}' \
               f' for {self.student}' \
               f', ordered books: {self.books}' \
               f'. Date {self.order_date}'
