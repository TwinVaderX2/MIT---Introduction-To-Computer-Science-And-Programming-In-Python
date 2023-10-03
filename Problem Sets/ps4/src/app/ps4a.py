# Problem Set 4A
# Name: Phillip van Staden
# Code from link: https://www.youtube.com/watch?v=eMp4Rb8DcTI used to find solution


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # change word into list of char
    ls = [i for i in sequence]

    # list of all permutations
    all_perm = []

    # base case - one char length
    if len(ls) <= 1:
        return ls

    # recursion case = if length of word is more than one char length, keep first char and find permutation of the remaining
    else:
        for i in range(len(ls)):
            temp = ls.copy()
            first = temp.pop(i)
            all_perm = all_perm + [first + j for j in get_permutations(temp)]
        return all_perm


if __name__ == '__main__':

    print(get_permutations('ab'))


