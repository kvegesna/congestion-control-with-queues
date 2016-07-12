import matplotlib.pyplot as plt


with open('output.txt','r') as f:
    lines = f.read().split("\n")
    lines1 = f.read().split("\n")

print("Number of lines is {}".format(len(lines)))

word = '2.00'
word1 = '4.00'
word2 = '6.00'
word3 = '8.00'
word4 = '10.0'

for i,line in enumerate(lines):
    if word in line: # or word in line.split() to search for full words
        print("Word \"{}\" found in line {}".format(word, i+1))
        str1= line
        print (str)
        str2 = line.split()[5]
        print (line.split()[5])

    if word1 in line:
        print("Word \"{}\" found in line {}".format(word1, i+1))
        str3= line
        print (str)
        str4 = line.split()[5]
        print (line.split()[5])

    if word2 in line:
        print("Word \"{}\" found in line {}".format(word2, i+1))
        str5= line
        print (str)
        str6 = line.split()[5]
        print (line.split()[5])

    if word3 in line:
        print("Word \"{}\" found in line {}".format(word3, i+1))
        str7= line
        print (str)
        str8 = line.split()[5]
        print (line.split()[5])

    if word4 in line:
        print("Word \"{}\" found in line {}".format(word4, i+1))
        str9= line
        print (str)
        str10 = line.split()[5]


x = [2, 4, 6, 8, 10]
y = [[str2, str4, str6, str8, str10], [5, 6, 7, 8, 9]]
csfont = {'fontname':'Helvetica Neue'}
labels = ['foo', 'bar', 'baz']
csfont = {'fontname':'Helvetica Neue'}
plt.title('Advantages of Bandwidth Limiting using iPerf and 10 MB Limit',**csfont)
plt.xlabel('Bandwidth Limit in MBps', **csfont)
plt.ylabel('Throughput in Mbps', **csfont)
labels = ['Without Queues', 'Without Queues']

for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)

plt.legend()
plt.show()
