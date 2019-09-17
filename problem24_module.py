from tqdm import tqdm

problem_name = "Lexicographic permutations"

problem_definition = '''A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
    012 021 102 120 201 210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''

n_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def swap(elements, i, j):
    elements[i], elements[j] = elements[j], elements[i]

def reverse(elements, i, j):
    for offset in range((j - i + 1) // 2):
        swap(elements, i + offset, j - offset)

lst = [1,2,3,4,5,6,7,8,9,0]

def next_permutation(elements):
    last_index = len(elements) - 1
    if last_index < 1:
        return

    i = last_index - 1
    while i >= 0 and not elements[i] < elements[i + 1]:
        i -= 1

    # If there is no greater permutation, return to the first one.
    if i < 0:
        reverse(elements, 0, last_index)
    # When there is possible permutation
    else:
        j = last_index
        while j > i + 1 and not elements[j] > elements[i]:
            j -= 1

        swap(elements, i, j)
        reverse(elements, i + 1, last_index)

def solve():
    permu_list = n_list.copy()
    for _ in tqdm(range(int(1e6) - 1), desc="Working on Solution: "):
        next_permutation(permu_list)
    return str().join(str(e) for e in permu_list)

def solve_out(length):
    permu_list = n_list.copy()
    for _ in tqdm(range(int(1e6)), desc="Working on Solution: "):
        next_permutation(permu_list)
    print(str().join(str(e) for e in permu_list))
    