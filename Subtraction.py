1234567891234567**2 - 1234567891234566**2
#2469135782469133

1234567891234567.0**2 - 1234567891234566.0**2
#2533274790395904.0

x = 1234567891234567.0
y = 1234567891234566.0

result  = (x-y)*(x+y)
print(result)
#2469135782469133.0

#it matches the integer one closely since catastrophic cancellation does not occur here because the
#machine precision and number precision is within bounds this time as we are dealing with smaller
#numbers in (x-y) and (x+y) instead of squares.