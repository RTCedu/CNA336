# This code provides basic HTTP, web, and API requests
# Zachary Rubin, zrubin@rtc.edu
# CNA 336 Spring 2018

import os
import urllib.request
hostname = "https://www.google.com"
hostname_get = "http://financials.morningstar.com/ajax/exportKR2CSV.html?t="
query = str(input("Enter a query"))
#query2 = str(input("Enter a second part"))
#hostname_get = hostname_get + query + "&oq=" + query2

# Uncomment this to do an infinite ping loop
#while True:
#    response = os.system("ping " + hostname)
#    print(response)

# Uncomment this to use URL lib to pull Google's main page
#contents = urllib.request.urlopen(hostname)
#print (contents.read())

contents = urllib.request.urlopen(hostname_get+query)
response = contents.read()
response_decoded_string = response.decode("utf-8")
start_location = response_decoded_string.find("5-Year Average")
end_location = response_decoded_string.find("10-Year Average")
#print(response_decoded_string)
edited_response = response_decoded_string[start_location:end_location]
five_year_list = edited_response.split(",")
print(five_year_list[1])
integer_list = []
for n in five_year_list:
    try:
        integer_list.append(float(n))
    except ValueError:
        print("Not a valid number. It's too dangeorous to continue")
        os.system("shutdown /p")


print (integer_list)
