import sys
evenNumbers = [element
               for element in range(800)
               if element % 2 == 0
               ]

evenNumbersGenerator = (element**2
                        for element in range(101)
                        )

print(sum(evenNumbersGenerator))


