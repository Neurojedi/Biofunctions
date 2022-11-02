#!/usr/bin/env python
# coding: utf-8

# In[1]:


from biofunctions.utils.complementary import complementary
# Output: All k-mers shared by these strings, in the form of ordered pairs (x, y) corresponding to starting positions of these k-mers in the respective strings.
def SharedKmers(k, seq1, seq2):
    result = []
    seq_dict = {}
    len_seq1=len(seq1)
    len_seq2=len(seq2)
    for i in range(len_seq1 - k + 1):
        key = seq1[i:i+k]
        if key in seq_dict.keys():
            seq_dict[key].append(i)
        elif complementary(key) in seq_dict.keys():
            seq_dict[complementary(key)].append(i)
        else:
            seq_dict[key] = [i]
    for i in range(len_seq2 - k + 1):
        sub_str = seq2[i:i+k]
        if sub_str in seq_dict.keys():
            for pos in seq_dict[sub_str]:
                result.append([pos, i])
        elif complementary(sub_str) in seq_dict.keys():
            for pos in seq_dict[complementary(sub_str)]:
                result.append([pos, i])
    for r in result:
        print('(' + ', '.join(map(str, r)) + ')')

if __name__ == "__main__":
    k = int(input().rstrip())
    seq1 = input().rstrip()
    seq2 = input().rstrip()
    result = SharedKmers(k, seq1, seq2)

