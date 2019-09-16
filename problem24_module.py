from tqdm import tqdm

problem_name = "Lexicographic permutations"

problem_definition = ""

n_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def swap(lst, n1, n2):
    if n1 == n2:
        return
    lst[n1], lst[n2] = lst[n2], lst[n1]

def solve():
    permu_list = n_list.copy()
    head  = 10
    for i in tqdm(range(int(1e5))):
        permu_list = n_list.copy()
        if head > 9:
            head = 0
        swap(permu_list, head, 0)
        head = head + 1
        for i in reversed(range(10)):
            swap(permu_list, i, i - 1)
    return permu_list