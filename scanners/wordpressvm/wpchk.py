#############
# https://github.com/BlueStrawBerrys
############

import requests

a = input("Enter Combo: ")

x = open("output.txt", "r")
for line in a:
    a = requests.get(line + "/wp-login.php")
    if a.status_code == 200:
        print(line + "/wp-login.php" + " Wordpress Found")
        x.write(line + "/wp-login.php")
    else:
        print(line + 'Dead')