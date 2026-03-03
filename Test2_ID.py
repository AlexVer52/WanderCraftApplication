count = 0
case = 2
with open("input2.txt", "r") as f:
    text = f.read().strip()
    parts = [p.strip() for p in text.split(",") if p.strip()]
    for part in parts:
        numbers = [p.strip() for p in part.split("-") if p.strip()]
        nums = list(range(int(numbers[0]), int(numbers[1]) + 1))
        if case == 1:
            for num in nums:
                num2 = str(num)
                if len(num2) % 2 == 0: 
                    mid = len(num2) // 2 
                    left_half = num2[:mid] 
                    right_half = num2[mid:] 
                    if left_half == right_half: 
                        count += num 
                    else: continue
        if case == 2:
            for num in nums:
                num2 = str(num)
                n = len(num2)
                for k in range(1, n//2 + 1):
                    if n % k != 0:
                        continue
                    block = num2[:k]
                    times = n//k
                    # Since block is a string, we can multiply it and obtain the origial number as a string
                    if block * times == num2:
                        count += num
                        break
print(count)