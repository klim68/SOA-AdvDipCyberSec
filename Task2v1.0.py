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
        print("Date: " + " " + response.headers["Date"])
except KeyError:
    print("Date:   Sorry, information not available")

try:
    if response.headers["X-Country-Code"]:
        print("X-Country-Code: ")
except KeyError:
    print("X-Country-Code:   Sorry, information not available" )

try:
    if response.headers["Connection"]:
        print("Connection: " )
except KeyError:
    print("Connection:   Sorry, information not available")

try:
    if response.headers["Content-Length"]:
        print("Content-Length: " )
except KeyError:
    print("Content-Length:   Sorry, information not available" )

try:
    if response.headers["Content-Type"]:
        print("Content-Type: ")
except KeyError:
    print("Content-Type:   Sorry, information not available")
