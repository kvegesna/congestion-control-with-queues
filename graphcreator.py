__author__ = 'kvegesna'
import matplotlib.pyplot as plt

with open('output.txt', 'r') as f:
    lines = f.read().split("\n")
    lines1 = f.read().split("\n")

#print("Number of lines is {}".format(len(lines)))

word0 = '0.00-1.00'
word = '5.00-6.00'
word1 = '27.00-28.00'
word2 = '43.00-44.00'
word3 = '60.00-61.00'
word4 = '70.00-71.00'

for i, line in enumerate(lines):
    if word0 in line:  # or word in line.split() to search for full words
        # print("Word \"{}\" found in line {}".format(word, i + 1))
        str1 = line
        #print(str)
        str2 = line.split()[4]
        total = 0
        x = 0
        while x < 10:
            holder = lines[i]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)
            if (fltstrholder < 1):
                fltstrholder *= 1000
            total += fltstrholder
            x += 1
            i += 1
        #print(line.split()[4])
        #print(total)
        avg0 = total / 10000
        x = 0
        total = 0

    if word in line:  # or word in line.split() to search for full words
        # print("Word \"{}\" found in line {}".format(word, i + 1))
        str1 = line
        #print(str)
        str2 = line.split()[4]
        total = 0
        x = 0
        while x < 10:
            holder = lines[i]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)

            if (fltstrholder < 10):
                fltstrholder *= 1000
            total += fltstrholder
            x += 1
            i += 1
        #print(line.split()[4])
        #print(total)
        avg = total / 10000
        #print(avg)
        x = 0
        total = 0

    if word1 in line:
        #print("Word \"{}\" found in line {}".format(word1, i + 1))
        #print("x is ")
        #print(x)
        str3 = line
        #print(str)
        str4 = line.split()[5]
        #print(line.split()[5])
        while x < 10:
            holder = lines[i]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)
            #print(fltstrholder)
            total += fltstrholder
            x += 1
            i += 1
        avg1 = total / 10000
        x = 0
        #print(avg1)
        total = 0

    if word2 in line:
        # print("Word \"{}\" found in line {}".format(word2, i + 1))
        str5 = line
        print(str)
        str6 = line.split()[5]
        print(line.split()[5])
        while x < 10:
            holder = lines[i]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)
            print (fltstrholder)
            total += fltstrholder
            x += 1
            i += 1
        avg2 = total / 10000
        x = 0
        print(avg2)
        total = 0

    if word3 in line:
        print("Word \"{}\" found in line {}".format(word3, i + 1))
        str7 = line
        print(str)
        str8 = line.split()[5]
        print(line.split()[5])
        while x < 11:
            holder = lines[i]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)
            total += fltstrholder
            x += 1
            i += 1
        avg3 = total / 10000
        x = 0
        print(avg3)
        total = 0

x = [0, 2, 4, 6, 8]
y = [[avg0, avg, avg1, avg2, avg3], [0, 0.1, 0.2, 0.3, 0.4, ]]
axes = plt.gca()
axes.set_xlim([0, 10])
axes.set_ylim([0,0.75])
csfont = {'fontname': 'Helvetica Neue'}
plt.title('Advantages of Bandwidth Limiting using iPerf and 10 MB Limit', **csfont)
plt.xlabel('UDP Congestion(MBps)', **csfont)
plt.ylabel('TCP Throughput(MBps)', **csfont)
labels = ['Without Queues', 'With Queues']

for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)

plt.legend()
plt.show()
