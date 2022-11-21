from sys import argv

list = argv[1:]
sorted_list = sorted(list, key=lambda s : len(s))

if len(list) != 0:
    print("The shortest word is ", sorted_list[0])
else:
    print("Please provide some arguments")
