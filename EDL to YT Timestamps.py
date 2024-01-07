import os, glob

with open(glob.glob("*.edl")[0], "r") as file:
  file_lines = file.readlines()[3:]
  index = 0
  for line in file_lines:
    if line == '\n':
      continue
    if not index%2:
      # Parse timestamp
      raw_timestamp = line[33:37]
      print(raw_timestamp[0:-1] + str(int(raw_timestamp[-1:])+((index != 0)*1)))
    else:
      # Parse name
      print(line[24:-5])
    index = index + 1
  file.close()
  input("\nPress enter to close")