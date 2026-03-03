totalValue = 0
k = 12

with open("input3.txt", "r") as f:
    for line in f:
        lines = line.strip()
        if not lines:
            continue

        max_bank = 0
        stack = []
        drop = len(lines) - k
        for i in lines:
            # We can only remove digits if:
            # 1. We have more removals available (drop > 0)
            # 2. The current stack is not empty
            # 3. The last digit in the stack is smaller than the current digit
            while drop > 0 and stack and stack[-1] < i:
                stack.pop()
                drop -= 1
            # We add the current digit to the stack
            stack.append(i)
            max_bank = "".join(stack[:k])

        print(lines)
        print(max_bank)
        totalValue += int(max_bank)

print(totalValue)
               