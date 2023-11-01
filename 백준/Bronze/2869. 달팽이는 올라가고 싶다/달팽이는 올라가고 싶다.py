A, B, V = map(int, input().split()) # A:하루에 오르는 거리 B:미끄러지는 거리 V: 목표 높이
day = 1
result = (V-B)/(A-B)
if result != int(result):
    print(int(result)+1)
else:
    print(int(result))