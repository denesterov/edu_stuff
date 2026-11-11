s = open('24_28943.txt').read()
for c in 'EIOUY':
    s = s.replace(c, 'A')
arr = s.split('A')

# если исходная строка не заканчивалась на гласную, то последняя подстрока из split нас не устраивает
# (но датасет с kompege не вскрывает эту проблему :-) ответ правильный в люобм случае)
if s[-1] != 'A': 
    arr.pop()

mn = 10_000_000
for ss in arr:
    for l in range(52, min(len(ss) + 1, mn + 1)):
        sss = ss[-l:]
        c20 = sss.count('20')
        if c20 == 26:
            if len(sss) <= mn:
                mn = len(sss)
                break
        elif c20 > 26: # оптимизация
            break

print(mn + 1) # еденичку на гласную в конце, которую съел split
