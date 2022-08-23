from statistics import median, mode

# mean
list1 = [12,15,23,34,54,33,23,21]

mean = sum(list1)/len(list1)

# print(mean)

# median

list2 = [12,24,43,45,64,23,53]
list2.sort()

if len(list1) % 2 ==0:
    m1 = list1[len(list1)//2]
    m2 = list2[len(list2)//-1]
    medien = (m1+m2)/2
else:
    medien = list1[len(list1)//2]

# print(medien)

# mode 

list1 = [12,16,20,20,20,12,30,25,23]
frequency = {}
for i in list1:
    # print(i)
    frequency.setdefault(i,0)
    # print(frequency.setdefault(i,0))
    frequency[i]+=1

frequent = max(frequency.values())

for i,j in frequency.items():
    if j == frequent:
        mode = i
print(mode)