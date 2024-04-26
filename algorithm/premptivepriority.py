# Function
def Priority(processlist):
    
  relist = [] #list to store completed process
  queue = []  #to store process which needs to wait

    # sorted all process according to Arrival Time and Priority
  processlist = sorted(processlist, key = lambda x: (x["Arrival Time"],x["Priority"]))
  for x in processlist:
    x["Burst Time1"] = x["Burst Time"]

  # Active process store process which is getting used by CPU
  activeprocess = processlist.pop(0)
  time = activeprocess["Arrival Time"]

  # Loop will run until all process get completed
  while queue or processlist or activeprocess["Burst Time"] != 0:

  # If there are any process left in processlist
    if processlist:

      # increase time and decrease Burst Time until next process comes
      if (time != processlist[0]["Arrival Time"] and activeprocess["Burst Time"] != 0):
        activeprocess["Burst Time"] -= 1 
        time+=1 

      else:

        # If activeprocess Priority is higher than processlist then it is getting append in processlist
        if(activeprocess["Priority"] <= processlist[0]["Priority"]):
          queue.append(processlist.pop(0))
          queue = sorted(queue, key = lambda x: (x["Priority"],x["Arrival Time"])) #sorting array on basis of Priority and Arrival Time
        else:

          # If queue is empty then it pushes activeprocess in queue
          if not queue:
            queue.append(activeprocess)
            activeprocess = processlist.pop(0)
            queue = sorted(queue, key = lambda x: (x["Priority"],x["Arrival Time"]))

          # If queue is not empty then we have to take process which has more Priority
          else:

            # If Priority of process in queue is higher than processlist then it will become activeprocess
            if (queue[0]["Priority"] < processlist[0]["Priority"]):
              activeprocess = queue.pop(0)
              queue.append(processlist.pop(0))
              queue = sorted(queue, key = lambda x: (x["Priority"],x["Arrival Time"]))
            else:
              queue.append(activeprocess)
              activeprocess = processlist.pop(0)
              queue = sorted(queue, key = lambda x: (x["Priority"],x["Arrival Time"]))

        # If queue have some process but procesllist don't
    else:
          
      # Checking already sorted queue 
      if queue:
        if (activeprocess["Burst Time"] != 0):
          activeprocess["Burst Time"]-=1
          time+=1
        else:
          activeprocess=queue.pop(0)

      # If last process is running and queue is empty
      elif activeprocess["Burst Time"] != 0:
        activeprocess["Burst Time"]-=1
        time+=1

      # Append every completed process
      if (activeprocess["Burst Time"] == 0 and activeprocess["Completion Time"] == 0):
        activeprocess["Completion Time"] = time
        activeprocess["Turnaround Time"] = time - activeprocess["Arrival Time"]
        activeprocess["Waiting Time"] = activeprocess["Turnaround Time"] - activeprocess["Burst Time1"]
        relist.append(activeprocess)
        # If active prcoess is completed and cpu is in idle state then it will make process in queue as activeprocess or make the next process in processlist as activeprocess
        if processlist and time != processlist[0]["Arrival Time"]:
          if not queue:
            time = processlist[0]["Arrival Time"]
            activeprocess = processlist.pop(0)
          else:
            activeprocess = queue.pop(0)
  relist = sorted(relist, key = lambda x: (x["Arrival Time"],x["Priority"]))
  for x in relist:
    x["Burst Time"] = x["Burst Time1"]
    x.pop("Burst Time1")
  return relist

# Defining process using dictionary
process1 = {
  "Priority" : 4,
  "Arrival Time" : 6,
  "Burst Time" : 34,
  "Completion Time": 0,
}

process2 = {
  "Priority" : 2,
  "Arrival Time" : 10,
  "Burst Time" : 1,
  "Completion Time": 0,
}

process3 = {
  "Priority" : 5,
  "Arrival Time" : 11,
  "Burst Time" : 25,
  "Completion Time": 0,
}

process4 = {
  "Priority" : 1,
  "Arrival Time" : 8,
  "Burst Time" : 31,
  "Completion Time": 0,
}

# Making a list of process
list = [process1,process2,process3,process4]

#calling function
result = Priority(list)
for i in result:
  print(i)