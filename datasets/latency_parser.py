import sys

start_data = []
end_data = []

with open(sys.argv[1]) as start:
  start_data = start.readlines()
  
with open(sys.argv[2]) as end:
  end_data = end.readlines()

seqnums = []
start_times = []
end_times = []
latencies = []

#timestamps seem to be in ns
for i in range(len(end_data)):
  if ("Final" not in end_data[i]):
    item = end_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    seqnums.append(item[0][15:])
  

for i in range(len(start_data)):
  if ("Final" not in start_data[i]):
    item = start_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    if (item[0][11:] in seqnums):
      start_times.append(float(item[1][:-1])/1000000000)

#there will be more data in start_data than end_data due to retransmissions
for i in range(len(end_data)):
  if ("Final" not in end_data[i]):
    item = end_data[i].split(',')
    end_times.append(float(item[1][:-1])/1000000000)
    #else:
      #end_times.append(0)

    
for i in range(len(start_times)):
  latencies.append(end_times[i] - start_times[i])

#print start_times
#print end_times
print latencies















  
  

