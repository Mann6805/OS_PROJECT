import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import threading
import time
import random

opt = st.sidebar.radio("Choose your option",options=("Premptive Priority","FCFS Disk Scheduling","Least Recently Used","Reader Writer"))
if opt == "Premptive Priority":

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

  st.title("Preemptive Priority")
  st.write("Priority preemptive scheduling is a CPU scheduling algorithm that selects the process with the highest priority for execution. In the preemptive version of this algorithm, if a new process arrives with a higher priority than the currently executing process, the CPU switches to the new process.")
  st.write("If two processes have the same priority, the algorithm may use additional criteria, such as arrival time, to break the tie.")

  st.markdown("---")
  st.header("Code")
  code="""# Function
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
            print(i)"""
  st.code(code,language="Python")

  st.markdown("---")

  st.header("Calculate: ")
  at = st.text_input(label="Arrival Time",placeholder="eg: 0 2 4 6")
  bt = st.text_input(label="Burst Time",placeholder="eg: 3 4 2 6")
  p = st.text_input(label="Priority",placeholder="#Lower number = Higher Priority")
  if at and bt and p:
    try:
      list_at = list(map(int,at.strip().split(" ")))
      list_bt = list(map(int,bt.strip().split(" ")))
      list_p = list(map(int,p.strip().split(" ")))
    
      if ( (len(list_at) != len(list_bt)) or (len(list_at) != len(list_p)) or (len(list_bt) != len(list_p)) ):
        st.warning("All values should be same")
    
      else:
        processlist = []
        for i in range (0,len(list_bt)):
          new_dict = {}
          new_dict["Priority"] = list_p[i]
          new_dict["Arrival Time"] = list_at[i]
          new_dict["Burst Time"] = list_bt[i]
          new_dict["Completion Time"] = 0
          processlist.append(new_dict)
        result = Priority(processlist)
        str1 = ""
        str2 = ""
        avg_tat = 0
        avg_wt = 0
        for i in result:
          str1 = str1+"+"+str(i["Turnaround Time"])
          avg_tat += i["Turnaround Time"]
          str2 = str2+"+"+str(i["Waiting Time"])
          avg_wt += i["Waiting Time"]
        str1 = str1+" / "+str(len(list_at))
        str2 = str2+" / "+str(len(list_at))
        btn = st.button(label="Calculate", key="priority")
        if btn:
          st.table(result)
          st.write("Average Turnaround Time = "+str1[1:]+"= {:.2f}".format(avg_tat / len(list_at)))
          st.write("Average Waiting Time = "+str2[1:]+"= {:.2f}".format(avg_wt / len(list_at)))
    except:
      st.warning("Check Your Inputs")
elif opt == "FCFS Disk Scheduling":

  def FCFS(arr, head):
      n = len(arr)
      seek_time = 0

      for i in range(n):
          seek = abs(arr[i] - head)      # abs diff between current request and current position of head
          seek_time += seek

          # Move the head to the next request
          head = arr[i]

      return seek_time

  st.title("FCFS Disk Scheduling")
  st.write("Disk scheduling is a fundamental aspect of computer operating systems that involves managing and ordering the access to a computer's disk storage.")
  st.write("Disk scheduling involves deciding the sequence in which disk read/write operations are executed.")
  st.write(" Accessing data from disk involves physical movement of the disk's read/write head, and organizing these accesses efficiently can significantly impact system performance.")
  st.write("The primary goal of disk scheduling algorithms is to minimize the seek time.")

  st.subheader("Seek Time")
  st.write("Time taken by read/write head to reach up to desired track.")
  st.markdown("---")

  st.title("Code")
  code="""def FCFS(arr, head):
            n = len(arr)
            seek_time = 0

            for i in range(n):
                seek = abs(arr[i] - head)      # abs diff between current request and current position of head
                seek_time += seek

                # Move the head to the next request
                head = arr[i]

            return seek_time

            requests = [98, 183, 37, 122, 14, 124, 65, 67]    # Request queue
            initial_head = 53
            seek_time = FCFS(requests, initial_head)

            print("Sequence of Disk Accesses:", requests)
            print("Total Seek Time:", seek_time)"""
  st.code(code,language="Python")

  st.markdown("---")

  st.header("Calculate: ")

  q = st.text_input(label="Enter Request: ",placeholder="eg: 55 67 86 87")
  h = st.text_input(label="Enter intial head ",placeholder="eg: 60")

  if q and h:
    try:
      queue=list(map(int,q.strip().split()))
      head=int(h.strip())
      if queue and head:
        btn = st.button(label="Calculate",key="FCFS")
        seek_time = FCFS(queue,head)
        if btn:
          y = np.arange(len(queue)+1,0,-1)
          x = [head]+queue
          fig = plt.figure()
          plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
          plt.title("FCFS DISK SCHEDULING")
          plt.xlim(min(queue)-20,max(queue)+20)
          plt.yticks([])
          plt.plot(x,y)
          st.write(fig)
          st.write("Total Seek Time: ",str(seek_time))
    except:
      st.warning("Check upur inputs.")
elif opt == "Least Recently Used":
  
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
  
  st.title("Least Recently Used Page Scheduling")
  st.write("The basic idea behind LRU is to replace the least recently used page when a new page needs to be brought into memory and there is no free space available.")
  st.write("The algorithm aims to maximize the chances of retaining pages that are likely to be accessed again soon.")
  st.subheader("Steps")
  st.write(" 1. Tracking Page Access:\nRecord the order of page accesses.\n2. Replacement Decision: \nWhen memory is full, find the least recently used page.\n3. Eviction:\nRemove the least recently used page from memory.\n4. Update Access Record:\nMove the accessed page to the front for future reference.")
  st.markdown("---")

  st.title("Code")
  code = """def LRU(frames,pages):
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
          print(f"Hit: {hit} Miss: {miss}")"""
  
  st.code(code,language="Python")

  st.markdown("---")

  st.header("Calculate: ")

  frames = st.text_input(label="Enter frames: ",placeholder="eg: 4")
  pages = st.text_input(label="Enter pages: ",placeholder="eg: 7 0 2 4 5 1 2 7 0 0 0")

  if frames and pages:
    try:
      pages=list(map(int,pages.strip().split()))
      frames=int(frames.strip())
      if pages and frames:
        btn = st.button(label="Calculate",key="LRU")
        result,hit,miss = LRU(frames,pages)
        if btn:
          st.table(result)
          st.write(f"Hit ratio: {hit/len(pages)}")
          st.write(f"Miss ratio: {miss/len(pages)}")
    except:
      st.warning("Check upur inputs.")
elif opt == "Reader Writer":
  mutex = threading.Semaphore(1)  
  db = threading.Semaphore(1)  
  reader_count = 0
  iterations = 0 
  operations = []

  def Reader():
      global reader_count, iterations
      while iterations < 5: 
          mutex.acquire()  
          reader_count += 1  
          if reader_count == 1: 
              db.acquire()  
          mutex.release() 
          operations.append("Reading...")
          time.sleep(random.uniform(0.5, 1.5))
          
          mutex.acquire()  
          reader_count -= 1  
          if reader_count == 0: 
              db.release() 
          mutex.release()  
          
          time.sleep(random.uniform(0.5, 1.5))
          iterations += 1 

  def Writer():
      global iterations
      while iterations < 5:  
          time.sleep(random.uniform(0.5, 2.5))
          db.acquire() 
          operations.append("Writing...")
          time.sleep(random.uniform(0.5, 1.5))
          db.release()
          iterations += 1
  st.title("Reader Writer")

  st.markdown("---")

  st.header("Code")
  code="""import threading
          import time
          import random

          mutex = threading.Semaphore(1)  
          db = threading.Semaphore(1)  
          reader_count = 0
          iterations = 0 
          def Reader():
              global reader_count, iterations
              while iterations < 10: 
                  mutex.acquire()  
                  reader_count += 1  
                  if reader_count == 1: 
                      db.acquire()  
                  mutex.release() 
                  print("Reading...")
                  time.sleep(random.uniform(0.5, 1.5))
                  
                  mutex.acquire()  
                  reader_count -= 1  
                  if reader_count == 0: 
                      db.release() 
                  mutex.release()  
                  
                  time.sleep(random.uniform(0.5, 1.5))
                  iterations += 1 

          def Writer():
              global iterations
              while iterations < 10:  
                  time.sleep(random.uniform(0.5, 3.5))
                  db.acquire() 
                  print("Writing...")
                  time.sleep(random.uniform(0.5, 1.5))
                  db.release()
                  iterations += 1  

          reader_thread = threading.Thread(target=Reader)
          writer_thread = threading.Thread(target=Writer)

          reader_thread.start()
          writer_thread.start()

          reader_thread.join()
          writer_thread.join()"""
  st.code(code,language="Python")

  st.markdown("---")

  btn = st.button(label="Start",key="rw")
  if btn:
    reader_thread = threading.Thread(target=Reader)
    writer_thread = threading.Thread(target=Writer)

    reader_thread.start()
    writer_thread.start()

    reader_thread.join()
    writer_thread.join()
    
  for i in operations:
      st.write(i)
      time.sleep(random.uniform(0.5, 1.5))
