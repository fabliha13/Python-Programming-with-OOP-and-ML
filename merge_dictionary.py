d1 = {"a":2, "b":5, "c":8}

d2 = {"d":9, "c":4, "e":3}

final_dict = {}

for k,v in d1.items():
    if k not in final_dict:
        final_dict[k] = v

    else:
        final_dict[k] += v

for k,v in d2.items():
    if k not in final_dict:
        final_dict[k] = v

    else:
        final_dict[k] += v

print(final_dict)
