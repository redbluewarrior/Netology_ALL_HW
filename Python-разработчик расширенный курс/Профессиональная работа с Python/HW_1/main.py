from application.salary import calculate_salary as sp
from application.db.people import get_employees as pd
import datetime
import numpy

if __name__ == '__main__':
    sp()
    pd()
    print(datetime.date.today())

