from itertools import combinations as itertools_combinations, product

def generate_substrings(s: str):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return substrings

def generate_combinations(s: str):
    combs = set()
    for r in range(1, len(s) + 1):
        for comb in itertools_combinations(s, r):  # Sử dụng tên hàm đã đổi
            combs.add(''.join(comb))
    return combs

def generate_case_variants(s: str):
    """ Generate all case variants for the given string """
    variants = set()
    for case_combination in product(*[(char.lower(), char.upper()) for char in s]):
        variants.add(''.join(case_combination))
    return variants

pass_data = "New@12345"

# Generate all case variants of the password
case_variants = generate_case_variants(pass_data)

# Generate all substrings and combinations for each case variant
all_substrings = set()
all_combinations = set()

for variant in case_variants:
    substrings = generate_substrings(variant)
    combs = generate_combinations(variant)  # Đổi tên biến từ 'combinations' sang 'combs'
    all_substrings.update(substrings)
    all_combinations.update(combs)

# print("Substrings:")
# for substring in all_substrings:
#     print(substring)

list_data = []
print("Combinations:")
for combination in all_combinations:
    if combination.startswith('n') or combination.startswith('N'):
        list_data.append(combination)

list_data = [item for item in list_data if len(item) >= 5]        
list_data.sort(key=len)
data_len = len(list_data)
print(f"Filtered and Sorted Combinations (starting with 'n' or 'N'): {data_len}")
for item in list_data:
    print(item)