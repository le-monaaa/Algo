def dfs(L, beginWith):
    global max_sum
    # 종료조건
    if L == 3:
        sum_cards = sum(cards)
        if sum_cards <= M and sum_cards > max_sum:
            max_sum = sum_cards

    else:
        for i in range(beginWith, len(card_list)):
            cards.append(card_list[i])
            dfs(L + 1, i + 1)
            cards.remove(card_list[i])

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

max_sum = 0

cards = []

dfs(0, 0)
print(max_sum)