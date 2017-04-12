import sys


def tidy_number(N):
    intN = int(N)
    list_N = []
    breakCnt = 0
    if intN<10:
        return N
    else:
        for i in xrange(intN, -1, -1):
            list_N = list(str(i))
            breakCnt = 0
            for j in xrange(len(list_N) - 1):
                if int(list_N[j])> int(list_N[j+1]):
                    breakCnt = 1
                    break
            if breakCnt is not 1:
                return i


def main():

    out = tidy_number("111111111111111110")
    # print out
    cnt = 0
    for line in sys.stdin:
        if cnt > 0:
            print 'Case #' + str(cnt) + ': ' + str(tidy_number(line.strip()))
        cnt += 1


if __name__ == "__main__":
    main()