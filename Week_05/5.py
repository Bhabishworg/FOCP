from sys import argv
from statistics import mean

try:
    list = argv[1:]
    new_list = [int(i) for i in list]

    max_value = max(new_list)
    min_value = min(new_list)
    mean_value = mean(new_list)

except IndexError:
    print("No string provided")
   
except ValueError:
    print("No Argument Provided")

except NameError:
    print("No Argument Provided")

else:
    print("The max Value is", max_value)
    print("The min Value is", min_value)
    print("The mean Value is", mean_value
