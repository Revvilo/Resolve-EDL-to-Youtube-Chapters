import glob, datetime

with open(glob.glob("*.edl")[0], "r") as file:
  file_lines = file.readlines()[3:]
  index = 0
  for line in file_lines:
    if line == '\n':
      continue
    if not index % 2:
      # Parse timestamp
      raw_timestamp = datetime.datetime.strptime(line[32:37], '%M:%S')
      nudged_timestamp = raw_timestamp + datetime.timedelta(0,(index != 0) * 1)
      # print(raw_timestamp)
      # if nudged_timestamp == 60: nudged_timestamp = 59
      print(nudged_timestamp.strftime('%M:%S'), end=" - ")
    else:
      # Parse name
      print(line[24:-5])
    index = index + 1
  file.close()
  input("\nPress enter to close")