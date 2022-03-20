import requests
url = input("Please enter the URL : ")

response = requests.head(url)


print("Response Status code: ", response.status_code, '\n')

try:
    if response.headers["Server"]:
        print("Server:" + " " + response.headers['Server'] + '\n')
except KeyError:
    print("Server:   Sorry, information not available" + '\n')

try:
    if response.headers["Date"]:
        print("Date: " + " " + response.headers['Date'] + '\n')
except KeyError:
    print("Date:   Sorry, information not available" + '\n')

try:
    if response.headers["X-Country-Code"]:
        print("X-Country-Code: " + " " + response.headers['X-Country-Code'] + '\n')
except KeyError:
    print("X-Country-Code:   Sorry, information not available" + '\n')

try:
    if response.headers["Connection"]:
        print("Connection: " + " " + response.headers['Connection'] + '\n')
except KeyError:
    print("Connection:   Sorry, information not available" + '\n')

try:
    if response.headers["Content-Length"]:
        print("Content-Length: " + " " + response.headers['Content-Length'] + '\n')
except KeyError:
    print("Content-Length:   Sorry, information not available" + '\n')

try:
    if response.headers["Content-Type"]:
        print("Content-Type: " + " " + response.headers['Content-Type'] + '\n')
except KeyError:
    print("Content-Type:   Sorry, information not available" + '\n')
