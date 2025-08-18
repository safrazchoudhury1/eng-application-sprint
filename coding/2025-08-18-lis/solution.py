"""
Compute the length of the longest increasing subsequence (LIS) in a list of integers.
This implementation uses a binary search approach (patience sorting) and runs in O(n log n) time.
"""


def length_of_lis(nums):
    """Return the length of the longest increasing subsequence in nums."""
    tails = []
    for num in nums:
        left, right = 0, len(tails)
        # find the insertion point for num in tails
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    return len(tails)


if __name__ == "__main__":
    try:
        # Prompt the user for a sequence of integers
        raw = input("Enter numbers separated by spaces: ").strip()
        seq = [int(x) for x in raw.split() if x]
        result = length_of_lis(seq)
        print(f"Length of LIS: {result}")
    except Exception as e:
        print("Error:", e)
