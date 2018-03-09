# -*- coding: utf-8 -*-
#!/bin/python

"""Console script for ledTester."""
import sys
import click
click.disable_unicode_literals_warning = True
import argparse
import urllib.request



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

# Split function splits up data from input file provides commands and coordinates, 
# removes unnecessary words,
# replaces new lines with commas, trips white spaces at start of line and last command
def split(line):

    newCommand = line
    #newCommand = newCommand.replace(" ", ",")
    newCommand = newCommand.replace("through", "")
    newCommand = newCommand.replace("\n", ",")
    if line.startswith(" "):
        newCommand = newCommand.strip()
    if newCommand.endswith(" "):
        #newCommand = newCommand.replace(" ", "\n")
        newCommand = newCommand.strip()
    x1 = ""
    x2 = ""
    y1 = ""
    y2 = ""
    cmd = ""
    #print (line)

    if newCommand.startswith('turn on'):
        cmd = "turn on"
        newCommand= newCommand.replace("turn on", "")
    if newCommand.startswith('turn off'):
        cmd = "turn off"
        newCommand=  newCommand.replace("turn off", "")
    if newCommand.startswith('switch'):
        cmd = "switch"
        newCommand = newCommand.replace("switch", "")

    if cmd != "":
        newCommand = newCommand.replace(",", " ")
        val = [int(s) for s in newCommand.split() if s.isdigit()]

        x1 = val[0]
        x2 = val[2]
        y1 = val[1]
        y2 = val[3]

    return cmd, x1, x2, y1, y2

# Sanitize function checks if coordinates are less than 0 or more than grid range
def sanitize(x1, x2, y1, y2, N):
    if int(x1) < 0:
        x1 = 0
    if int(x2) < 0:
        x2 = 0
    if int(y1) < 0:
        y1 = 0
    if int(y2) < 0:
        y2 = 0
    if int(x1) >= N:
        x1 = N - 1
    if int(x2) >= N:
        x2 = N - 1
    if int(y1) >= N:
        y1 = N - 1
    if int(y2) >= N:
        y2 = N - 1

    return x1, x2, y1, y2

# Main function, takes input,
# Stores data from input in buffer
# determines grid size by first line, builds 2 dimensional array of 0's
# Compares commands and calls appropriate functions
# compares if coordinates from line are appropriate to use i.e x1 < x2 etc
def main() -> object:
    # create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input


    # read file in to buffer in utf 8 format
    uri = filename
    req = urllib.request.Request(filename)
    response = urllib.request.urlopen(req)
    buffer = response.read().decode('utf-8')


    a2d = []
    # set size of grid, read each line from file (sep by return)
    for line in buffer.split('\n'):

            if line == "":
                break

            if line.isdigit():
                N = int(line)
                a2d = [[0] * N for _ in range(N)]

            else:

                command, x1, x2, y1, y2 = split(line)

                if command == "turn on":

                    x1, x2, y1, y2 = sanitize(x1, x2, y1, y2, N)
                    

                    if int(x1) <= int(x2) and int(y1) <= int(y2):
                        turnOn(int(x1), int(x2), int(y1), int(y2), a2d)
                    

                elif command == "turn off":

                    x1, x2, y1, y2 = sanitize(x1, x2, y1, y2, N)
                    

                    if int(x1) <= int(x2) and int(y1) <= int(y2):
                        turnOff(int(x1), int(x2), int(y1), int (y2), a2d)
                    

                elif command == "switch":

                    x1, x2, y1, y2 = sanitize(x1, x2, y1, y2, N)
                    

                    if int(x1) <= int(x2) and int(y1) <= int(y2):
                        switch(int(x1), int(x2), int(y1), int(y2), a2d)
                    
                    
# Prints count of lights on and filename
    count = countLights(N, a2d)
    print("Number of lights on ", count)
    print(filename)
    return

if __name__ == '__main__':
    main()
