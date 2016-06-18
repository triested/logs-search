import urllib.request
import json

while True:
	url_input = input("Enter the first player's logs.tf profile URL: ")
	id_index = url_input.find("/profile/")
	if id_index == -1:
		print("URL not recognized. Please try again.")
		continue
	steam_id_64 = url_input[id_index + 9: id_index + 26]
	if len(steam_id_64) != 17:
		print("URL not recognized. Please try again.")
		continue
	else:
		url1 = "http://logs.tf/json_search?&player=" + steam_id_64
		break

while True:
	url_input = input("Enter the second player's logs.tf profile URL: ")
	id_index = url_input.find("/profile/")
	if id_index == -1:
		print("URL not recognized. Please try again.")
		continue
	steam_id_64 = url_input[id_index + 9: id_index + 26]
	if len(steam_id_64) != 17:
		print("URL not recognized. Please try again.")
		continue
	else:
		url2 = "http://logs.tf/json_search?&player=" + steam_id_64
		break


json1 = urllib.request.urlopen(url1)
output_string1 = json1.read().decode('utf-8')
data1 = json.loads(output_string1)

#url2 = 'http://logs.tf/json_search?&player=76561198064873161'
json2 = urllib.request.urlopen(url2)
output_string2 = json2.read().decode('utf-8')
data2 = json.loads(output_string2)


for i in reversed(data1['logs']):
	for j in reversed(data2['logs']):
		if i['id'] == j['id']:
			print(i['title'])
			print("http://logs.tf/" + str(i['id']))


