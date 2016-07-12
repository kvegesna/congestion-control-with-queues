import matplotlib.pyplot as plt


with open('output.txt','r') as f:
    lines = f.read().split("\n")


print("Number of lines is {}".format(len(lines)))

word = '2.00' # dummy word. you take it from input

# iterate over lines, and print out line numbers which contain
# the word of interest.
for i,line in enumerate(lines):
    if word in line: # or word in line.split() to search for full words
        print("Word \"{}\" found in line {}".format(word, i+1))
        str= line
        print (str)
        str2 = line.split()[5]
        print (line.split()[5])
        variable = []


        break

x = [2, 4, 6, 8, 10]
y = [ [0, 10, 20, 30, 90], [50, 60, 70, 80, 90]]
csfont = {'fontname':'Helvetica Neue'}
labels = ['foo', 'bar', 'baz']
csfont = {'fontname':'Helvetica Neue'}
plt.title('Advantages of Bandwidth Limiting using iPerf and 10 MB Limit',**csfont)
plt.xlabel('Bandwidth Limit in MBps', **csfont)
plt.ylabel('Throughput in Mbps', **csfont)
labels = ['With Queues', 'Without Queues']

for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)

plt.legend()
plt.show()




