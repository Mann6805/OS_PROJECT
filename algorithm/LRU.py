def LRU(frames,pages):
  hit = 0
  miss = 0
  cur_frame = []
  track = []
  result = []
  for i in pages:
    if i in cur_frame:
      track.remove(i)
      track.append(i)
      hit+=1
      result.append({
        "Page" : i,
        "Frames" : cur_frame.copy(),
        "Hit/State" : "Hit"
      })
    else:
      if len(cur_frame) == frames:
        element = track.pop(0)
        index = cur_frame.index(element)
        cur_frame[index] = i
      else:
        cur_frame.append(i)
      track.append(i)
      miss+=1
      result.append({
        "Page" : i,
        "Frames" : cur_frame.copy(),
        "Hit/State" : "Miss"
      })
  return result, hit, miss

frames = 4
pages = [7, 0, 1, 3, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]

ans,hit,miss = LRU(frames,pages)
print(f"Hit: {hit} Miss: {miss}")