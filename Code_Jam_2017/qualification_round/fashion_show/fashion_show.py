import sys


class grid:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.type_p = []
        self.type_x = []
        self.type_o = []

    def add_para(self, style, idx, idy):
        if style == '+':
            self.type_p.append((idx, idy))
        elif style == 'x':
            self.type_x.append((idx, idy))
        elif style == 'o':
            self.type_o.append((idx, idy))


def fashion_show(data):

    points = data.N*2
    new_elem = data.N - min(len(data.type_p), len(data.type_x)) - len(data.type_o)
    if len(data.type_x) < len(data.type_p):
        pass
    elif len(data.type_x) > len(data.type_p):
        pass
    else:
        pass

    return points, new_elem


def main():
    cnt = 0
    cnt_max = int(sys.stdin.readline())
    while cnt < cnt_max:
        line = sys.stdin.readline()
        N, M = map(int, line.strip().split())
        data = grid(N, M)
        if M > 0:
            for ii in range(M):
                line = sys.stdin.readline()
                style, idx, idy = line.strip().split()
                data.add_para(style, idx, idy)

        out = fashion_show(data)
        print 'Case #' + str(cnt) + ': ' + str(out[0]) + ' ' + str(out[1])

        cnt += 1

if __name__ == "__main__":
    main()
