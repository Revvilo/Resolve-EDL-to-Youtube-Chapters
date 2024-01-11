import glob, datetime

with open(glob.glob("*.edl")[0], "r") as file:
  file_lines = file.readlines()[3:] # Trim off the first 3 lines of the file
  index = 0
  for line in file_lines:
    if line == '\n':
      continue # Skip blank line
    if not index % 2:
      # Parse timestamp
      raw_timestamp = datetime.datetime.strptime(line[32:37], '%M:%S') # This is ok because the timestamp doesn't move

      # Adds a second and scaling offset to the time if not the first chapter
      #  this compensates for truncating the frames from the timestamp
      #  and compensates for the weird timestamp drift that is coming from somewhere
      nudged_timestamp = raw_timestamp + datetime.timedelta(0, (index != 0) * (1+0.133*index))

      print(nudged_timestamp.strftime('%M:%S'), end=" - ")
    else:
      # Parse name
      print(line.split('|')[2][2:-1]) # Yay dynamic finding of the name
    index = index + 1
  file.close()
  input("\nPress enter to close")