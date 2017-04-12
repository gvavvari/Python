import sys
from multiprocessing import Pool


def pancake_flipper(*args):
    S = args[0][0]
    K = int(args[0][1])
    S_list = [True if s == '+' else False for s in S]
    cnt = 0
    while True:
        try:
            idx = S_list.index(False)
        except ValueError:
            break
        if len(S_list)-idx < K:
            return 'IMPOSSIBLE'
        else:
            for ii in range(idx, idx + K):
                S_list[ii] = not S_list[ii]
            cnt += 1
    return cnt


def main():

    processor_cnt = 6
    pool = Pool(processes=processor_cnt)
    parallel_parameters = []
    x = 0
    for line in sys.stdin:
        if x > 0:
            parallel_parameters.append(line.strip().split())
        x += 1
    algo_output = pool.map(pancake_flipper, parallel_parameters)
    x = 1
    for output_i in algo_output:
        print 'Case #' + str(x) + ': ' + str(output_i)
        x += 1

if __name__ == "__main__":
    main()
