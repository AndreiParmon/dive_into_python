import argparse
import logging

FORMAT = '{levelname} - {asctime} - строка {lineno}: {msg}'

logging.basicConfig(filename='log_task_1.log',
                    format=FORMAT,
                    style='{',
                    level=logging.INFO)

parser = argparse.ArgumentParser(description='Принимаем число')
parser.add_argument('number', type=int, default='1')
args = parser.parse_args()

number = args.number

if number <= 1 or number > 100000:
    logging.error('Число должно быть больше 1 и меньше 100000!')
elif (number % 2 != 0 or number == 2) and (number % 3 != 0 or number == 3):
    logging.info(f'число {number} является простым числом')
else:
    logging.info(f'число {number} является составным числом')
