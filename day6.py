from get_data import get_data_as_list



def get_bank_index_with_most_blocks(banks):
    "Returns the index of the bank with the most blocks."
    return max(enumerate(banks), key=lambda i_bank : i_bank[1])[0] # Gets the smallest indexed bank in case of multiple at max.

def redistribute_bank(index, banks):
    "Redistributes the index:th bank contents over all the banks."
    banks = list(banks)
    blocks = banks[index]
    banks[index] = 0
    for i in range(index+1, index+1+blocks):
        banks[i % len(banks)] += 1
    return banks

def balance_banks(banks):
    "Balances the banks. Returns (banks, cycles)"
    seen_states = set()
    cycles = 0

    while tuple(banks) not in seen_states:
        seen_states.add(tuple(banks))
        redis_index = get_bank_index_with_most_blocks(banks)
        banks = redistribute_bank(redis_index, banks)
        cycles += 1
        
    return banks, cycles



if __name__ == '__main__':
    data = get_data_as_list(6, int)

    _, cycles = balance_banks(data)
    print("Task 1: Required {} balancing cycles.".format(cycles))