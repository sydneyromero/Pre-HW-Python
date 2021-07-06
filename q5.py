def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
      
listed_range = [-5, -4, -3, -2, -1, 1]
print(is_consecutive(listed_range))