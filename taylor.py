import argparse
from math import sqrt


def get_args():
    parser = argparse.ArgumentParser(
        description='Calculates taylor series'
    )
    parser.add_argument(
        'argument',
        type=float,
        help='a point where to count a function',
        metavar='argument'
    )
    parser.add_argument(
        'num',
        type=int,
        help='amount of additions in taylor series',
        metavar='num'
    )
    return parser.parse_args().argument, parser.parse_args().num


def taylor_series(argument, number, info=True):
    sum_value = sqrt(3) / 2
    cur_value = sum_value
    for idx in range(1, number):
        cur_value *= (1.5 - idx) * 16 * \
                     ((argument - 0.25) ** 2) / (idx * 3)
        sum_value += cur_value

    actual_value = sqrt(1 - 2*argument + 4*(argument**2))
    difference = abs(sum_value - actual_value)
    if info:
        print(f'{number:3}|{sum_value:24}|{actual_value:24}|{difference:24}')
    else:
        return sum_value


if __name__ == '__main__':
    print(f'Num|'
          f'{"":9}Taylor{"":9}|'
          f'{"":9}Actual{"":9}|'
          f'{"":10}Diff{"":10}')
    taylor_series(*get_args())
