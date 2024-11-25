
print("Read entire file content using read():")
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)


print("\nRead file line by line using readline():")
with open('example.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line.strip())  
        line = f.readline()


print("\nRead all lines into a list using readlines():")
with open('example.txt', 'r') as f:
    lines = f.readlines()
    print(lines)


print("\nIterate over file object directly:")
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())


print("\nRead the file in binary mode:")
with open('example.jpg', 'rb') as f: 
    binary_content = f.read()
    print(binary_content[:20])  


print("\nUsing seek() and tell() to control file pointer:")
with open('example.txt', 'r') as f:
    f.seek(10) 
    print("Current file pointer position:", f.tell())
    content = f.read(5) 
    print("Next 5 bytes:", content)
