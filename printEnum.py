#!/usr/bin/env python

def correct(string):
  return string.replace("3dmeeple", "threedmeeple").replace("3dstairs", "threedstairs").replace("catch", "catch1").replace("private", "private1").replace("static", "static1")

data = [line.rstrip('\n').split(" ") for line in open('sorted')]

# Correct names
number = 1
data[0][0]=correct(data[0][0])
i=1
while i < len(data):
  data[i][0]=correct(data[i][0])
  # If a name occures more than one time, increase number
  if data[i][0] == data[i - number][0]:
    number += 1
    data[i][0] = data[i][0] + str(number)
  else:
    number = 1
  i += 1

# Print enum class
print "enum GameIcon {"
print

# Print cases
for line in data:
  print "case " + line[0]

# Print relative paths
print
print "var relativePath: String {"
print "switch self {"
for line in data:
  print "case ." + line[0] + ":"
  print "return \"" + line[1][2:] + "\""
print "}"
print "}"

print
print "}"
