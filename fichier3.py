# api-endpoint
URL = "http://localhost:8585/api/review-requests/3/diffs/1/files/3/patched-file/"

headers = {'Authorization': 'token 8b395c24de9363275d04697e73dc41dd5b6ad9a2'}  
# sending get request and saving the response as response object
r = requests.get(url = URL,headers=headers)
  
# extracting data in json format
data = r.content
