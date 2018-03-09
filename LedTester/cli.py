# -*- coding: utf-8 -*-
#!/bin/python

"""Console script for ledTester."""
import sys
import click
click.disable_unicode_literals_warning = True

# Counter Function - counts all the leds on (1) after all commands completed
def countLights(N, a2d):
    count = 0
    for i in range(N):
        for j in range(N):
            if a2d[i][j] == 1:
                count += 1 

    return count

# On function turns leds from 0 to 1 in the range of given coordinates
def turnOn(x1, x2, y1, y2, a2d):
    for i in range(x1, x2 +1):
        for j in range(y1, y2 +1):
            a2d[i][j] = 1
   # for a in a2d:
    #    print(a)
    #print('\n')

    return

# Off Function turns leds from 1 to 0 in range of coordinates gives
def turnOff(x1, x2, y1, y2, a2d):
    for i in range(x1, x2 +1):
        for j in range(y1, y2 +1):
            a2d[i][j] = 0
    #for a in a2d:
      #  print(a)
   # print('\n')
    return

# Switch function swaps lights from 1 to 0 and vice versa, in range of coordainates given.
def switch(x1, x2, y1, y2, a2d):
    for i in range(x1, x2 +1):
        for j in range(y1, y2 +1):
            if a2d[i][j] == 0:
                a2d[i][j] = 1
            elif a2d[i][j] == 1:
                a2d[i][j] = 0
  #  for a in a2d:
     #   print(a)
   # print('\n')
    return


@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    print("input", input)

    N, instructions = parseFile(input)

    ledTester = LEDTester(N)

    for instruction in instructions:
        ledTester.apply(instruction)

    print('#occupied: ', ledTester.countOccupied()) 
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover