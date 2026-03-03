pos = 50
count = 0
case = 2
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:   # skip empty lines if any
            continue
        direction = line[0]
        distance = int(line[1:])
        if case == 1:
            if direction == 'R':
                pos = (pos + distance) % 100
            elif direction == 'L':
                pos = (pos - distance) % 100
            if pos == 0:
                count += 1
        if case == 2:
            if direction == 'R':
                d = distance
                step = 1
            elif direction == 'L':
                d = -distance
                step = -1

            for _ in range(distance):
                pos = (pos + step) % 100
                if pos == 0:
                    count += 1

print(count)