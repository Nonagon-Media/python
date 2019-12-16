"""Working with lists."""

friends = ["Dan", "Ben", "Doc", "Fizz", "Noodles", "Doc"]
lucky_numbers = [4, 8, 15, 16, 23, 42]

friends.sort()
print(friends)
print(friends[0])
print(friends[-1])
print(friends[2:])
print(friends[1:4])
friends[1] = "Chuck"
print(friends[1])

print(min(lucky_numbers))
print(max(lucky_numbers))

friends.extend(lucky_numbers)
print(friends)
friends.append("Doug")
print(friends)
friends.insert(1, "JenMo")
print(friends)
friends.remove("Chuck")
# friends.clear()
print(friends)
friends.pop()
print(friends)

print(friends.index("Fizz"))

# This throws an error
# print(friends.index("Mort"))

# Should be 2
print(friends.count("Doc"))

lucky_numbers.reverse()
print(lucky_numbers)

# This has been removed and doesnt work
# numbers2 = lucky_numbers.copy()
numbers2 = list(lucky_numbers)
print(numbers2)
