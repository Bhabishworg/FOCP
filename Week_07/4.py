from string import ascii_lowercase

counts = {key: 0 for key in ascii_lowercase}

message = input("Enter the message: ")

for char in message.lower():
    if char in ascii_lowercase:
        counts[char] = counts[char] + 1

most_common = sorted(counts.items(), key=lambda item: item[1],reverse=True)[:6]

for total_count in most_common:
    letter, count = total_count
    print(f"{letter} occurs {count} times")