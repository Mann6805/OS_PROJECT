# Function
def priority(processlist):
  relist = [] #list to store completed process
  queue = []  #to store process which needs to wait

  # sorted all process according to arrivaltime and priority
  processlist = sorted(processlist, key = lambda x: (x["arrivaltime"],x["priority"]))
  for x in processlist:
    x["bursttime1"] = x["bursttime"]

  # Active process store process which is getting used by CPU
  activeprocess = processlist.pop(0)
  time = activeprocess["arrivaltime"]

  # Loop will run until all process get completed
  while queue or processlist or activeprocess["bursttime"] != 0:

    # If there are any process left in processlist
    if processlist:

      # increase time and decrease bursttime until next process comes
      if (time != processlist[0]["arrivaltime"] and activeprocess["bursttime"] != 0):
        activeprocess["bursttime"] -= 1 
        time+=1 

      else:

        # If activeprocess priority is higher than processlist then it is getting append in processlist
        if(activeprocess["priority"] <= processlist[0]["priority"]):
          queue.append(processlist.pop(0))
          queue = sorted(queue, key = lambda x: (x["priority"],x["arrivaltime"])) #sorting array on basis of priority and arrivaltime
        else:

          # If queue is empty then it pushes activeprocess in queue
          if not queue:
            queue.append(activeprocess)
            activeprocess = processlist.pop(0)
            queue = sorted(queue, key = lambda x: (x["priority"],x["arrivaltime"]))

          # If queue is not empty then we have to take process which has more priority
          else:

            # If priority of process in queue is higher than processlist then it will become activeprocess
            if (queue[0]["priority"] < processlist[0]["priority"]):
              activeprocess = queue.pop(0)
              queue.append(processlist.pop(0))
              queue = sorted(queue, key = lambda x: (x["priority"],x["arrivaltime"]))
            else:
              queue.append(activeprocess)
              activeprocess = processlist.pop(0)
              queue = sorted(queue, key = lambda x: (x["priority"],x["arrivaltime"]))

    # If queue have some process but procesllist don't
    else:
      
      # Checking already sorted queue 
      if queue:
        if (activeprocess["bursttime"] != 0):
          activeprocess["bursttime"]-=1
          time+=1
        else:
          activeprocess=queue.pop(0)

      # If last process is running and queue is empty
      elif activeprocess["bursttime"] != 0:
          activeprocess["bursttime"]-=1
          time+=1

    # Append every completed process
    if (activeprocess["bursttime"] == 0 and activeprocess["ctime"] == 0):
      activeprocess["ctime"] = time
      activeprocess["turnaroundtime"] = time - activeprocess["arrivaltime"]
      activeprocess["waitingtime"] = activeprocess["turnaroundtime"] - activeprocess["bursttime1"]
      relist.append(activeprocess)
      # If active prcoess is completed and cpu is in idle state then it will make process in queue as activeprocess or make the next process in processlist as activeprocess
      if processlist and time != processlist[0]["arrivaltime"]:
        if not queue:
          time = processlist[0]["arrivaltime"]
          activeprocess = processlist.pop(0)
        else:
          activeprocess = queue.pop(0)

  # Printing relist  
  relist = sorted(relist, key = lambda x: (x["arrivaltime"],x["priority"]))
  for x in relist:
    x["bursttime"] = x["bursttime1"]
    x.pop("bursttime1")
    print(x)

# Defining process using dictionary
process1 = {
  "priority" : 4,
  "arrivaltime" : 6,
  "bursttime" : 34,
  "ctime": 0,
}

process2 = {
  "priority" : 2,
  "arrivaltime" : 10,
  "bursttime" : 1,
  "ctime": 0,
}

process3 = {
  "priority" : 5,
  "arrivaltime" : 11,
  "bursttime" : 25,
  "ctime": 0,
}

process4 = {
  "priority" : 1,
  "arrivaltime" : 8,
  "bursttime" : 31,
  "ctime": 0,
}

# Making a list of process
list = [process1,process2,process3,process4]

#calling function
priority(list)