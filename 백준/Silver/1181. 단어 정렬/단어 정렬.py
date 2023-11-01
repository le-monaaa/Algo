
words = set()
max_len = 0
N = int(input())
for n in range(N):
    word = input()
    words.add(word)
    if len(word) > max_len:
        max_len = len(word)
word_list = [[] for _ in range(max_len)]
for word in words:
    word_list[len(word)-1].append(word)

for l in word_list:
    l = sorted(l)
    for i in range(len(l)):
        print(l[i])