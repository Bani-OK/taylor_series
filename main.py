import argparse
from math import sqrt

import taylor


def get_args():
    parser = argparse.ArgumentParser(
        description='Gets info about taylor series'
    )
    parser.add_argument(
        'argument',
        type=float,
        help='a point where to count a function',
        metavar='argument'
    )
    return parser.parse_args().argument


def get_epsilons(argument):
    answer = []
    i = 1
    target = 0.1
    while i < 100000:
        taylor_value = taylor.taylor_series(argument, i, False)
        actual_value = sqrt(1 - 2 * argument + 4 * (argument ** 2))
        diff = abs(actual_value - taylor_value)
        if diff < target:
            if target == 0.1:
                answer.append(i)
                target = 1.0e-3
            elif target == 1.0e-3:
                answer.append(i)
                target = 1.0e-6
            elif target == 1.0e-6:
                answer.append(i)
                break
        i += 1
    return answer


def main(argument):
    if argument > 0.68 or argument < -0.18:
        print('At this point taylor series dose not '
              'approximate my function but infinity')
        return
    print(f'Num|'
          f'{"":9}Taylor{"":9}|'
          f'{"":9}Actual{"":9}|'
          f'{"":10}Diff{"":10}')
    print('-' * 78)
    numbers = {1, 5, 10, 25, 50}
    numbers.update(get_epsilons(argument))
    for num in sorted(list(numbers)):
        taylor.taylor_series(argument, num)


if __name__ == '__main__':
    main(get_args())
