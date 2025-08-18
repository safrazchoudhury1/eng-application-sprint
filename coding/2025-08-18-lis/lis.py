# Longest Increasing Subsequence (LIS) algorithm - dynamic programming with binary search
import bisect


def length_of_lis(nums):
    """
    Compute the length of the longest strictly increasing subsequence.
    """
    subseq = []
    for x in nums:
        # Find insertion position of x in the current subsequence
        idx = bisect.bisect_left(subseq, x)
        if idx == len(subseq):
            subseq.append(x)
        else:
            subseq[idx] = x
    return len(subseq)


if __name__ == "__main__":
    import sys

    # Read integers from standard input
    data = [int(x) for x in sys.stdin.read().split()]
    print(length_of_lis(data))
