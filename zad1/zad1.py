sqrOfSum = 0
sumOfSqrs = 0

for i in xrange(101):
    sqrOfSum += i
    sumOfSqrs += i ** 2

sqrOfSum = sqrOfSum ** 2

print sqrOfSum - sumOfSqrs
