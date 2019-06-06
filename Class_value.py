from counter import Counter

tally = Counter()
tally.reset()
tally.click()
tally.click()

result = tally.get_value()
print("Value: ", result)

tally.click()
result = tally.get_value()
print("Value: ", result)


tally.click()
result = tally.get_value()
print("Value: ", result)
