seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

seconds_sum = seconds_first + seconds_second + seconds_third

seconds_in_minutes = seconds_sum // 60
seconds_in_seconds = seconds_sum % 60

print(f'{seconds_in_minutes}:{seconds_in_seconds :02d}')