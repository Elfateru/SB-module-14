def short_seq_range(string, tpl):
    return min(len(string), len(tpl))


syms_str = 'abc'
# nums_tpl = (10, 20, 30, 40)
nums_tpl = {10: 1, 20: 2, 30: 3, 40: 4}

pairs = ((syms_str[i_elem], nums_tpl[i_elem]) for i_elem in range(short_seq_range(syms_str, nums_tpl)))
print(pairs)
