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

count = 0
for i in range(2, number // 2 + 1):
    if number % i == 0:
        count += 1
if count <= 0:
    logging.info(f'число {number} является простым числом')
else:
    logging.info(f'число {number} является составным числом')
