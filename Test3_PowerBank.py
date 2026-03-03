totalValue = 0

with open("input3.txt", "r") as f:
    for line in f:
        s = line.strip()
        if not s:
            continue

        max_bank = 0
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                val = 10 * int(s[i]) + int(s[j])
                if val > max_bank:
                    max_bank = val

        totalValue += max_bank

print(totalValue)
               