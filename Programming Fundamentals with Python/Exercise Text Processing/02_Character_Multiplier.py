user_input = input().split()
first_string, second_string = str(user_input[0]), str(user_input[1])

if len(first_string) <= len(second_string):
    shorter_string = [ord(x) for x in first_string]
    longer_string = [ord(x) for x in second_string]
else:
    shorter_string = [ord(x) for x in second_string]
    longer_string = [ord(x) for x in first_string]
diff = len(longer_string) - len(shorter_string)
for num in range(diff):
    shorter_string.append(1)

result = 0
for index in range(len(longer_string)):
    result += shorter_string[index] * longer_string[index]
print(result)

