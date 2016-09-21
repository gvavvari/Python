"""
@author: gopi vinod avvari
@date: Sept 21, 2016
@title: Pattern-Matching Paths
"""

import sys
import heapq


def detect_pattern(path, pattern_data):

    """
    - for each path given, we check among all given patterns for the best matching pattern
    - if there is/are wild card/s, we call thorough test function to find the best match
    """

    # probable patterns is a heap which stores all possible patterns prioritized with the left most *'s location
    probable_patterns = []
    # iterate over each pattern from the patterns list
    for pattern_i in pattern_data:
        # if path and pattern_i fields match, then the best pattern is detected
        if path == pattern_i:
            # return the best pattern
            return ','.join(pattern_i)
        # if number of fields in path and pattern_i match +
        # there is an * in the pattern_i, then it can be a probable pattern
        if len(path) == len(pattern_i) and '*' in pattern_i:
            # do a more closer test to check if pattern_i is a probable pattern
            # qualified pattern function returns if a pattern is qualified, number of wild characters in it
            qualify, wild_cnt = qualified_pattern(path, pattern_i)
            if qualify:
                # add the qualified pattern to the min prioritized heap
                heapq.heappush(probable_patterns, (wild_cnt, pattern_i))
    if len(probable_patterns) == 1:
        # if only one probable pattern is found, then it is the best match pattern
        return ','.join(probable_patterns[0][1])
    elif len(probable_patterns) > 1:
        # if there are multiple probable patterns, then, we do a thorough test
        return thorough_test(probable_patterns)
    else:
        return 'NO MATCH'


def qualified_pattern(path, pattern):

    """
    - function to check if the given pattern is a probable candidate to be a best match
    - a qualified pattern will have asterisk which is a wildcard and can match any string in the path
    """

    # wild_cnt stores count of wild card fields in a pattern
    wild_cnt = pattern.count('*')
    # similar items store the fields that match in path and pattern
    similar_items = [i for i, j in zip(path, pattern) if i == j]
    # a pattern is qualified if the number of fields that match plus the *'s count equals the path field count
    return len(path) == wild_cnt + len(similar_items), wild_cnt


def thorough_test(pattern_heap):

    """
    - we find the best-matching pattern which matches the path using the fewest wildcards
    - if there is tie, we call recursive test to determine the best path
    """

    # the pattern with least number of wild cards is popped out of heap
    element = heapq.heappop(pattern_heap)
    # least number of wild cards from any pattern in the list of probable pattern
    min_wild = element[0]
    # the pattern with least number of wild card
    min_wild_patterns = [element[1]]
    # pop other patterns with same number of minimum wild cards
    while len(pattern_heap) and pattern_heap[0][0] == min_wild:
        element = heapq.heappop(pattern_heap)
        # store all patterns having minimum number of wild cards
        min_wild_patterns.append(element[1])
    if len(min_wild_patterns) == 1:
        # if only one pattern is stored, we return it
        return ','.join(min_wild_patterns[0])
    else:
        best_idx_left = 0
        # if multiple number of patterns are stored, we do a recursive test to find the best match
        return recursive_test(min_wild_patterns, best_idx_left)


def recursive_test(patterns, best_idx_left):

    """
    - prefer the pattern whose leftmost wildcard appears in a field further to the right
    - if multiple patterns' leftmost wildcards appear in the same field position, do recursion
    """

    # list to store the patterns eligible for next recursion
    best_patterns = []
    for pattern_i in patterns:
        # iterate to find the left most index of wild card in a pattern
        for idx in xrange(best_idx_left, len(pattern_i)):
            letter = pattern_i[idx]
            if letter == '*':
                idx_left = idx
                # if the left most wild card's location more then the current best,
                # we consider this as the current best left most index and save the pattern
                if idx_left > best_idx_left:
                    best_idx_left = idx_left
                    best_patterns = [pattern_i]
                # if the left most wild card's location is same to the current one,
                # we add that pattern to the best pattern
                elif idx_left == best_idx_left:
                    best_patterns.append(pattern_i)
                break
    if len(best_patterns) == 1:
        # if only one pattern is stored, we return it
        return ','.join(best_patterns[0])
    else:
        # if multiple patterns have same best left most index, repeat recursion from next index on those patterns
        return recursive_test(best_patterns, best_idx_left+1)


def main():

    """
    - the input is read, parsed and segregated into path data and pattern data
    - function to match the best pattern for each path is called
    - best pattern is printed if there is one or NO MATCH is printed
    """
    try:
        # read the input data into file_info
        file_info = [line.rstrip('\n') for line in sys.stdin]
        # read total number of patterns
        total_patterns = int(file_info[0])
        # read patterns data
        patterns = file_info[1:total_patterns + 1]
        # organize pattern data by removing comma and using generators instead of iterators
        pattern_data = [pattern_i.split(',') for pattern_i in patterns]
        # read total number of paths
        total_paths = int(file_info[total_patterns+1])
        # read total number of paths
        paths = file_info[total_patterns + 2:total_patterns + total_paths + 2]
        # organize pattern data by removing / and removing space and using generators instead of iterators
        path_data = [path_i.strip('/').split('/') for path_i in paths]
        for path in path_data:
            # for each path, detect the best match in patterns using detect_pattern function
            print detect_pattern(path, pattern_data)
    except ValueError:
        print 'Error in the input data/simulation'
        quit()


if __name__ == "__main__":
    main()
