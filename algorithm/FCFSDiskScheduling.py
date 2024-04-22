def FCFS(arr, head):
    n = len(arr)
    seek_time = 0

    for i in range(n):
        seek = abs(arr[i] - head)      # abs diff between current request and current position of head
        seek_time += seek
        # Move the head to the next request
        head = arr[i]
    return seek_time
    
# Request queue
requests = [98, 183, 37, 122, 14, 124, 65, 67]
initial_head = 53
seek_time = FCFS(requests, initial_head)

print("Sequence of Disk Accesses:", requests)
print("Total Seek Time:", seek_time)
