# import statistics as s

from statistics import variance as v, mean as m # using * we can import all the features

example_list = [4, 7, 9, 2, 4, 3, 6, 9, 1, 2, 0, 5, 8]

# x = s.mean(example_list)
# y = s.median(example_list)

x = v(example_list)
y = m(example_list)

print(x, y) # - We can perform various statistics operation here
