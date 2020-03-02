#PENGGUNAAN LIST
#mylist = []
#mylist.append(1)
#mylist.append(2)
#mylist.append(3)
#print(mylist[0])
#print(mylist[1])
#print(mylist[2])
#}
#for x in mylist:
#    print(x)
##################################################

#mylist = [10]
#print(mylist[10])

#############################################
#CONTOH SOAL
number = []
strings = []
names = ["john", "eric", "jessica"]

number.append(1)
number.append(2)
number.append(3)

strings.append("hellow")
strings.append("world")

second_name = names[1]


print(number)
print(strings)
print("the second name of the name list %s " % second_name)
#############################################

number = 1 + 2 * 3 / 4.0
print(number)

reminder = 11 % 3
print(reminder)

#ini adalah pangkat
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#result is hello world because this >""< is blank so they defined to a space character
helloworld = "hello" + " " + "world"
print(helloworld)

#hello 10x
lotsofhellos = "hello " * 10
print(lotsofhellos)


#bukan tambah
even_number = [2,4,6,8]
odd_number = [1,3,5,7]
all_number = odd_number + even_number
print(all_number)

print([1,2,3] * 3) 

###soal
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len (x_list))
print("y_list contains %d objects" % len (y_list))
print("big_list contains %d objects" % len (big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("almost there")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("great")

##hallooooo
name = "Riel"
print("hello %s" % name)
##hallo
name = "riel"
age = 23
print("%s is %d years old." % (name, age))

##soallll
mylist = [1,2,3]
print("a list : %s" % mylist)

data = ("riel", "mard", 54)
format_string = ("hello %s %s. your current money is $%d")
print(format_string % data)

asting = "hello world"
asting2 = 'hello world'

asting = "hello guys!"
print("singel quote ' '")
print(len(asting))

##hurufnya ada di urutan keberapa?
astring = "Hello world!"
print(astring.index("w"))

astring = "hello world!"
print(astring[0:11])

astring = "hello world"
print(astring[3:7:2])

astring = "hello world"
print(astring[3:7])
print(astring[3:7:1])

## <::> untuk reserve
astring = "hello world"
print(astring[::-10])

##INI <UPPER UNTUK HURUF BESAR> <LOWER UNTUK HURUF KECIL>
astring = "hello world"
print(astring.upper())
print(astring.lower())

##MEMBUKTIKKAN BAHWA SEBUAH KATA ITU BERNILAI TREU ATAU FALSE
astring = "hello world"
print(astring.startswith("hello"))
print(astring.endswith("world"))

##memberikan sebuah tanda
astring = "hello world"
afewwords = astring.split(" ")
print(afewwords)

##soal baru

s = "strings are awesome!"
print("length of s = %d" %len(s))

print("the first occurrence of the letter a =%d" % s.index("a"))

print("a occurs %d times" % s.count("a"))
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
#######end soal baru

x = 3
print(x == 2)
print(x == 3)
print(x < 3)



name = "riel"
age = 18
if name == "riel" and age == 18:
    print("your name is riel and your age is 23 years old!")

if name == "riel" or name == "rick":
    print("your name is either riel or rick")

name = "Riel"
if name in ["Riel", "Rick"]:
        print("Your name is either Riel or Rick")



x = 2
if x == 2:
    print("X equal two!")
else:
    print("x does not equal to two")
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)


print(not False)
print((not False) == (False))

###soal baru
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if  number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array)  == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

###end soal


memek = ("KONTOLLLL")
print(memek)

###loop
primes = [2,3,5,7]
for prime in primes:
    print(prime)

###

for x in range(5):#1-4
    print(x)

for x in range(3,6):#3-5
    print(x)

for x in range(3,8,2):#3,5,7
    print(x)

print("test")

count = 0
while count <= 5:
    print(count)
    count += 1

print("anjeng")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("beda")
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print("baru lagi")


count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition\n")


print("ganteng\n")
count = 0 
while count <= 5:
    print(count)
    count += 1 #this meant is same as count = count + 1

print("ganteng\n")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
            break

print("kedua\n")

for x in range(10):
    if x % 2 == 0 :
        continue
    print(x)

print("ganteng\n")

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

for i in range(1,10):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

print("ganteng\n")

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue

    print(number)