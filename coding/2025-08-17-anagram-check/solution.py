# Determine if two strings are anagrams ignoring case and non-alphanumeric chars.


def clean(s: str) -> str:
    return "".join(ch.lower() for ch in s if ch.isalnum())


def is_anagram(a: str, b: str) -> bool:
    A, B = clean(a), clean(b)
    if len(A) != len(B):
        return False
    freq = {}
    for ch in A:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in B:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
    return True


if __name__ == "__main__":
    try:
        s1 = input().rstrip("\n")
        s2 = input().rstrip("\n")
    except EOFError:
        print("NO")
    else:
        print("YES" if is_anagram(s1, s2) else "NO")
