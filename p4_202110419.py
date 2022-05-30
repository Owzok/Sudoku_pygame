import requests
uni = str(input())
url = 'http://universities.hipolabs.com/search?country=Peru'

input= {"min":100,"max":1000,"count":10}
data = (requests.get(url)).json()

lst = []

for i in range(len(data)):
    if data[i]['name'] == uni:
        
        lst.append((data[i]['web_pages']))
        print(lst[0][0])
        break