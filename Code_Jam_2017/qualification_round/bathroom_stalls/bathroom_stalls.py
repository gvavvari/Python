import sys
import heapq


class stall_complex:

    def __init__(self, offset, length):
        self.offset = offset
        self.length = length
        self.max_min_val = (self.length-1)/2
        self.min_max_val = self.length/2


def bathroom_stalls(val):
    N = int(val[0])
    K = int(val[1])
    data = []
    element = stall_complex(0, N)
    push_data(data, element)
    max_min = element.max_min_val
    min_max = element.min_max_val
    for i in range(K):
        neg_max_min, neg_min_max, offset, element = heapq.heappop(data)
        max_min = - neg_max_min
        min_max = - neg_min_max
        if len(data) and max_min == data[0][0]:
            new_element = stall_complex(offset, min_max)
            push_data(data, new_element)
            new_element = stall_complex(offset + min_max + 1, element.length - min_max)
            push_data(data, new_element)
        else:
            new_element = stall_complex(offset, max_min)
            push_data(data, new_element)
            new_element = stall_complex(offset + max_min + 1, element.length - max_min - 1)
            push_data(data, new_element)
    y = min_max
    z = max_min
    return y, z


def push_data(data, element):
    if element.length > 0:
        heapq.heappush(data, (-element.max_min_val, -element.min_max_val, element.offset, element))


def main():

    x = 0
    for line in sys.stdin:
        if x > 0:
            out1, out2 = bathroom_stalls(line.strip().split())
            print 'Case #' + str(x) + ': ' + str(out1) + ' ' + str(out2)
        x += 1


if __name__ == "__main__":
    main()
