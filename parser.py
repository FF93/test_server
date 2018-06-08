import argparse
import subprocess
import time
import os
import signal


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--number', help='number of executions', type=int, default=4)
parser.add_argument('--script', help='experiment to run', type=str, default='main')
parser.add_argument('--size', help='size of the matrix', type=int, default=int(2*1e3))
parser.add_argument('--mode', help='parallel or not', type=str, default='sequential')

args = parser.parse_args()

if args.mode == 'parallel':
    # Execute in parallel

    t = time.time()
    for number in range(args.number):
        print('Printing in parallel form process: %d' % number)

        popen = subprocess.Popen(['python ' + args.script + '.py --number %d' % number +
                          ' --size %s' % args.size + ' --mode parallel'],
                         shell=True)

    popen.wait()

    elapsed_time_parallel = (time.time() - t)
    print("time = ", elapsed_time_parallel)
    os.killpg(os.getpgid(popen.pid), signal.SIGTERM)

else:
    # Execute sequentially

    t = time.time()
    for number in range(args.number):
        print('Printing sequentially number: %s' % number)

        popen = subprocess.Popen(['python ' + args.script + '.py --number %s' % number +
                                  ' --size %s' % args.size],
                         shell=True)
        popen.wait()
    elapsed_time_sequential = (time.time() - t)
    print("time = ", elapsed_time_sequential)
    os.killpg(os.getpgid(popen.pid), signal.SIGTERM)


