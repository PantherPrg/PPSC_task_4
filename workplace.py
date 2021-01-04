def robotTracker(record):
  # write your code here
  dirList = [0, 0, 0, 0] # [x, y, -x, -y]
  start = [int(record[0].split()[0]), int(record[0].split()[1])]
  dirList[0] = start[0]
  dirList[1] = start[1]

  dirListPlacer = 0

  for step in record[1:]:
    step = step.split()

    if step[0] == "forward":
      dirList[dirListPlacer] += int(step[1])
    elif step[0] == "left":
      dirListPlacer = (dirListPlacer + (int(step[1]) // 90)) % 4
    elif step[0] == "right":
      dirListPlacer = (dirListPlacer - (int(step[1]) // 90) + 4) % 4

  answer = " ".join([str(dirList[0] - dirList[2]), str(dirList[1] - dirList[3])])

  return answer + "\n"
