T = int(input())
for tc in range(1, T+1):
    cards = input()
    card_list = []
    # 카드 목록
    for i in range(0, len(cards), 3):
        card_list.append(cards[i:i+3])
    # 중복 값 확인
    sc, dc, hc, cc = 13, 13, 13, 13
    if len(card_list) != len(set(card_list)):
        print(f"#{tc} ERROR")
    else: # 중복 없을 경우
        for i in card_list:
            if i[0] == "S":
                sc -= 1
            if i[0] == "D":
                dc -= 1
            if i[0] == "H":
                hc -= 1
            if i[0] == "C":
                cc -= 1
        print(f"#{tc} {sc} {dc} {hc} {cc}")