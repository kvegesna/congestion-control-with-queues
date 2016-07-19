__author__ = 'kvegesna'
import matplotlib.pyplot as plt

word0 = '0.00-1.00'
word = '5.00-6.00'
word1 = '27.00-28.00'
word2 = '43.00-44.00'
word3 = '60.00-61.00'
word4 = '74.00-75.00'
word5 = '89.00-90.00'


with open('output.txt', 'r') as f:
    lines = f.read().split("\n")

with open('output1.txt', 'r') as f1:
    lines1 = f1.read().split("\n")


#print("Number of lines is {}".format(len(lines)))


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
            print ("lol")
            print (fltstrholder)

            if (fltstrholder < 10):
                fltstrholder *= 1000
            total += fltstrholder
            x += 1
            i += 1
        #print(line.split()[4])
        #print(total)
        avg = total / 10000
        print(avg)
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
        str6 = line.split()[5]
        while x < 10:
            holder = lines[i]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)
            total += fltstrholder
            x += 1
            i += 1
        avg2 = total / 10000
        x = 0
        total = 0

    if word3 in line:
        #print("Word \"{}\" found in line {}".format(word3, i + 1))
        str7 = line
        str8 = line.split()[5]
        while x < 10:
            holder = lines[i]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)

            total += fltstrholder
            x += 1
            i += 1
        avg3 = total / 10000
        x = 0
        total = 0

    if word4 in line:
        #print("Word \"{}\" found in line {}".format(word3, i + 1))
        str7 = line
        str8 = line.split()[5]
        while x < 9:
            holder = lines[i]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)
            print(fltstrholder)
            total += fltstrholder
            x += 1
            i += 1
        avg4 = total / 10000
        x = 0
        total = 0

    if word5 in line:
        #print("Word \"{}\" found in line {}".format(word3, i + 1))
        str7 = line
        str8 = line.split()[5]
        while x < 8:
            holder = lines[i]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)

            total += fltstrholder
            x += 1
            i += 1
        avg5 = total / 10000
        x = 0
        total = 0



for j, line1 in enumerate(lines1):
    if word0 in line1:  # or word in line11.split() to search for full words
        print("Word \"{}\" found in line {}".format(word, j + 1))
        str1 = line1
        print(str1)
        str2 = line1.split()[4]
        total = 0
        x = 0
        while x < 10:
            holder = lines1[j]
            print(holder)
            strholder = holder.split()[4]
            fltstrholder = float(strholder)
            if (fltstrholder < 1):
                fltstrholder *= 1000
            total += fltstrholder
            x += 1
            j += 1
        #print(line1.split()[4])
        #print(total)
        average0 = total / 10000
        x = 0
        total = 0

    if word in line1:  # or word in line1.split() to search for full words
        # print("Word \"{}\" found in line1 {}".format(word, i + 1))
        str1 = line1
        #print(str)
        str2 = line1.split()[4]
        total = 0
        x = 0
        while x < 10:
            holder = lines1[j]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)

            if (fltstrholder < 10):
                fltstrholder *= 1000
            total += fltstrholder
            x += 1
            j += 1
        #print(line1.split()[4])
        #print(total)
        average = total / 10000
        #print(avg)
        x = 0
        total = 0

    if word1 in line1:
        #print("Word \"{}\" found in line1 {}".format(word1, i + 1))
        #print("x is ")
        #print(x)
        str3 = line1
        #print(str)
        str4 = line1.split()[5]
        #print(line1.split()[5])
        while x < 10:
            holder = lines1[j]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)
            #print(fltstrholder)
            total += fltstrholder
            x += 1
            j += 1
        average1 = total / 10000
        x = 0
        #print(avg1)
        total = 0

    if word2 in line1:
        # print("Word \"{}\" found in line1 {}".format(word2, i + 1))
        str5 = line1
        #print(str)
        str6 = line1.split()[5]
        #print(line1.split()[5])
        while x < 10:
            holder = lines1[j]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)
            #print (fltstrholder)
            total += fltstrholder
            x += 1
            j += 1
        average2 = total / 10000
        x = 0
        #print(avg2)
        total = 0

    if word3 in line1:
        #print("Word \"{}\" found in line1 {}".format(word3, i + 1))
        str7 = line1
        #print(str)
        str8 = line1.split()[5]
        #print(line1.split()[5])
        while x < 10:
            holder = lines1[j]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)

            total += fltstrholder
            x += 1
            j += 1
        average3 = total / 10000
        x = 0
        #print(avg3)
        total = 0
    if word4 in line1:
        #print("Word \"{}\" found in line1 {}".format(word3, i + 1))
        str7 = line1
        #print(str)
        str8 = line1.split()[5]
        #print(line1.split()[5])
        while x < 10:
            holder = lines1[j]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)

            total += fltstrholder
            x += 1
            j += 1
        average4 = total / 10000
        x = 0
        #print(avg3)
        total = 0

    if word5 in line1:
        #print("Word \"{}\" found in line1 {}".format(word3, i + 1))
        str7 = line1
        #print(str)
        str8 = line1.split()[5]
        #print(line1.split()[5])
        while x < 10:
            holder = lines1[j]
            strholder = holder.split()[4]
            fltstrholder = float(strholder)

            total += fltstrholder
            x += 1
            j += 1
        average5 = total / 10000
        x = 0
        #print(avg3)
        total = 0
        
x = [0, 2, 4, 6, 8, 10, 12]
y = [[0.98, avg, avg1, avg2, avg3, avg4, avg5], [average0, average, average1, average2, average3, average4, average5 ]]
axes = plt.gca()
axes.set_xlim([0, 12])
axes.set_ylim([0,1])
csfont = {'fontname': 'Helvetica Neue'}
plt.title('Advantages of Bandwidth Limiting using Queues and 5 MB Limit', **csfont)
plt.xlabel('UDP Congestion in Mbps', **csfont)
plt.ylabel('TCP Throughput in Mbps', **csfont)
labels = ['Without Queues', 'With Queues']

for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)

plt.legend()
plt.show()




