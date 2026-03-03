count = 0
with open("input2.txt", "r") as f:
    text = f.read().strip()
    parts = [p.strip() for p in text.split(",") if p.strip()]
    for part in parts:
        numbers = [p.strip() for p in part.split("-") if p.strip()]
        nums = list(range(int(numbers[0]), int(numbers[1]) + 1))
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