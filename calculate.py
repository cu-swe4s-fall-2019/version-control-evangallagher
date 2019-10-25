import math_lib as ml
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Divide and add two variables')

    parser.add_argument('-a',
                        type=int,
                        help='Variable a',
                        required=True)

    parser.add_argument('-b',
                        type=int,
                        help='Variable b',
                        required=True)

    args = parser.parse_args()

    print(str(args.a) + ' + ' + str(args.b) +
          ' = ' + str(ml.add(args.a, args.b)))

    print(str(args.a) + ' / ' + str(args.b) +
          ' = ' + str(ml.div(args.a, args.b)))


if __name__ == '__main__':
    main()
