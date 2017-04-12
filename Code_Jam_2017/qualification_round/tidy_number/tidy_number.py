import sys


def tidy_number(N):
    str_N = list(str(N))
    len_N = len(str_N)
    current_best = int(str_N[-1])
    for idx in range(len(str_N)):
        s = str_N[len_N - idx -1]
        if int(s) == current_best:
            continue
        if current_best == 0 or int(s) > current_best:
            str_N[len_N - idx -1] = str(int(str_N[len_N - idx -1]) - 1)
            str_N[len_N - idx:] = ['9']*idx
        current_best = int(str_N[len_N - idx -1])
    output_str = "".join(str_N)
    return int(output_str)


def main():

    cnt = 0
    for line in sys.stdin:
        if cnt > 0:
            print 'Case #' + str(cnt) + ': ' + str(tidy_number(line.strip()))
        cnt += 1


if __name__ == "__main__":
    main()
