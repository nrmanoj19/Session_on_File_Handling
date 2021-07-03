f = open("Sample1.txt")
print("File opened successfully!!!")
with f:
    print(f.read())
    f.close()
print("File Closed")

f = open("Sample1.txt")
print("File opened successfully!!!")
with f:
    print(f.readline())
    f.close()
print("File Closed")

f = open("Sample1.txt")
print("File opened successfully!!!")
with f:
    file_data = f.read()
    # print(file_data)
    f1 = open("Sample2.txt", "w")
    with f1:
        f1.write(file_data)
        f1.write("\nEnd of file")
        f1.close()
    f.close()
print("File Closed")

try:
    f = open("Sample1.txt")
    with f:
        raise Exception
        # print(f.read())
except:
    print("Exception occurred!!!")
finally:
    print("File closed!!!")
    f.close()


try:
    a = 5
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Zero Division error")
finally:
    print("Done!!!")

import logging
logging.basicConfig(filename="my_log.log", level=logging.WARNING)
logging.error("Error")
logging.critical("Critical")
logging.warning("Warning")
logging.debug("Debug")
logging.info("info")

f = open("Sample1.txt")
print("File opened successfully!!!")
with f:
    for each_line in f:
        print(each_line)
    f.close()
print("File Closed")