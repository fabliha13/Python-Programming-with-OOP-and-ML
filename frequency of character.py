sen = "She sells sea shell in the sea shore."

# freq = {}

# for ch in sen:
#     if ch not in freq:
#         freq[ch] = 1
#     else:
#         freq[ch] += 1

# print(freq)

from collections import Counter
freq = Counter(sen)

print(freq)

