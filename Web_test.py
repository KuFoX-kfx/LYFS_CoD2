#import requests
#from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
#import time

import socket

# Set up the connection details
server_ip = "146.59.34.100" # Replace with the IP address of your Call of Duty 2 server
server_port = 28960 # Default port for Call of Duty 2 servers

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a request to the server to get information about the current game
request_message = "\xff\xff\xff\xff\x67\x65\x74\x73\x74\x61\x74\x75\x73"
client_socket.sendto(request_message.encode(), (server_ip, server_port))

# Receive the response from the server
response_message, server_address = client_socket.recvfrom(4096)
print(response_message.decode())

# Close the socket
client_socket.close()




#ua = UserAgent()
#headers = {'User-Agent': str(ua.random)}
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36', 
#    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#    'Referer': 'https://www.gametracker.com'
#        }
#url = 'https://www.gametracker.com/server_info/146.59.34.100:28960/'

# Create a session
#session = requests.Session()
#time.sleep(1)
#response = session.get(url, headers=headers)
#time.sleep(1)
#cookies = response.cookies
#time.sleep(1)
#initial_request = session.get(url, headers=headers)
#time.sleep(1)
#response = requests.get(url, headers=headers, cookies=cookies)
#time.sleep(1)
#soup = BeautifulSoup(response.text, 'lxml')
#
#print(soup)
#print(headers)
#print(response)

#import requests
#from bs4 import BeautifulSoup
#
## Define the URL and headers
#url = "https://www.gametracker.com"
#headers = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#    "Referer": "https://www.gametracker.com",
#}
#
## Create a session
#session = requests.Session()
#
## Make an initial request to obtain cookies and bypass initial bot protection measures
#initial_request = session.get(url, headers=headers)
#
## Perform any necessary actions to bypass further bot protection mechanisms, if required
#
## Make subsequent requests with the updated headers and cookies
#response = session.get(url, headers=headers)
#
## Check if the request was successful
#if response.status_code == 200:
#    # Use BeautifulSoup to parse the HTML content
#    soup = BeautifulSoup(response.content, "html.parser")
#    # Perform parsing operations on the 'soup' object here
#    # Extract the desired data using BeautifulSoup's features
#
#    # Example: Print the title of the website
#    title = soup.title.string
#    print("Title:", title)
#else:
#    print(response.status_code)
#    print("Failed to retrieve the webpage.")
#
## Close the session
#session.close()
#



