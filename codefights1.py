def makeArrayConsecutive2(statues):
    minItem = min(statues)
    maxItem = max(statues)
    ans = 0
    for i in range(minItem, maxItem + 1):
        if i not in statues:
            ans += 1

    return (ans)

statues = [6,3]
print(makeArrayConsecutive2(statues))
