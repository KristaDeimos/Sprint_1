times = '1h 45m,360s,25m,30m 120s,2h 60s'

for time in times.split(','):
    parts = time.split()
    res = 0
    for part in parts:
        if 'h' in part:
            res += int(part[:-1]) * 60
        if 'm' in part:
            res += int(part[:-1])
        if 's' in part:
            res += int(part[:-1]) // 60

print(res)