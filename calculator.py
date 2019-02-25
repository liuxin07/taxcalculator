#!/usr/bin/env python3
import sys
from collections import namedtuple
income_tax = namedtuple('income_tax',['start_line','tax_rate','minus'])
income_tax_table = [
        income_tax(80000,0.45,13505),
        income_tax(55000,0.35,5505),
        income_tax(35000,0.3,2755),
        income_tax(9000,0.25,1005),
        income_tax(4500,0.2,555),
        income_tax(1500,0.1,105),
        income_tax(0,0.03,0)
        ]
social_tax_table = {
        'yanglao':0.08,
        'yiliao':0.02,
        'shiye':0.005,
        'gongshang':0,
        'shengyu':0,
        'gongjijin':0.06
        }

social_tax = sum(social_tax_table.values())
start_income = 3500

def real_income(income):
    income_real = income - social_tax*income
    tax_part = income_real - 3500
    for line in income_tax_table:
        if tax_part > line.start_line:
            tax = tax_part * line.tax_rate - line.minus
            hand_income = income_real - tax
            return '{:.2f}'.format(hand_income)
    return'{:.2f}'.format(income_real)

def main():
    for item in sys.argv[1:]:
        gonghao,gongzi = item.split(':')
        try:
            income = int(gongzi)
        except ValueError:
            print('Parameter Error')
        remain = real_income(income)
        print('{}:{}'.format(gonghao,real_income(income)))


if __name__ == '__main__':
    main()
