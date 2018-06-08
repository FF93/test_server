import numpy as np


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--number', help='number of process executed', type=int, default=1)
    parser.add_argument('--size', help='size of the matrix', type=int, default=int(1e3))
    parser.add_argument('--mode', help='parallel or not', type=str, default='sequential')

    args = parser.parse_args()
    print("With mode ", args.mode, "decompose matrix number ", args.number, "of size ", args.size)

    size = args.size

    A = np.random.randn(size, size)
    np.linalg.svd(A)
