import time
import sys
counter=0
for x in range(0,10):
    with open("test.txt", "a+", encoding='utf-8') as f:
        f.write(str(str(counter) + "\n"))
        
        print(x)
        time.sleep(1)
        sys.stdout.flush()
    counter= counter + 1