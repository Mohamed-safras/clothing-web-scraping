import os
from datetime import datetime

mod_time = os.stat("whether.csv").st_mtime

print(datetime.fromtimestamp(mod_time))

# for dirpath , dirnames,filenames in os.walk(os.getcwd()):
#     print(dirpath)
#     print(dirnames)
#     print(filenames)


with open(os.path.join(os.getcwd(), "os.text"), "w+") as file:
    file.write("hello")
    file.close()

