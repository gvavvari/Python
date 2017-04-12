import sys


def pancake_flipper(val):
    S = val[0]
    K = int(val[1])
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
    x = 0
    for line in sys.stdin:
        if x > 0:
            out = pancake_flipper(line.strip().split())
            print 'Case #' + str(x) + ': ' + str(out)
        x += 1

if __name__ == "__main__":
    main()
