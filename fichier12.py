# importing the requests library
import requests
import json
#Liste des changes
# api-endpoint
# URL = "http://localhost:8585/api/review-requests/3/diffs/1/files/3/patched-file/"

# headers = {"Authorization": "token 5a957c0c8cba9ea9a20356fc6dd4d3df302bc679"
#             }  
# # sending get request and saving the response as response object
# r = requests.get(url = URL,headers=headers)
  
# # extracting data
# data = r.content
# print (type(data))  

# print(data)
# r2 = requests.get(url = URL)
# print("deuxieme test")
# print(data)
# #Ajout de commentaires
# print("Test ajout de commentaires")
# URL = "http://localhost:8585/api/review-requests/3/reviews/21/diff-comments/"
# body= {
#     "filediff_id" : "3",
#     "first_line" : "2",
#     "num_lines" : "2",
#     "text" : "Une erreur ici"
# }
# r = requests.post(url = URL, headers = headers, data=body)
# # extracting data
# data = r.content
# print (type(data))  

# print(data)
# #Creer une review draft
# print("Creer une review draft")
# URL = "http://localhost:8585/api/review-requests/3/reviews/"
# body= {
    
# }
# r = requests.post(url = URL, headers = headers, data=body)
# data = r.content
# print (type(data))  

# print(data)
# #Publier une review
# print("Publier la revue")
# URL = "http://localhost:8585/api/review-requests/3/reviews/12/"
# # r=requests.put(url=URL, data={"public" : "true"}, headers = headers)
# # data = r.content
# # print (type(data)) 
# # print(data)


headers = {"Authorization": "token 5a957c0c8cba9ea9a20356fc6dd4d3df302bc679"
            } 
#Creer une review draft
print("Creer une review draft")
URL = "http://localhost:8585/api/review-requests/3/reviews/"
body= {
    
}
r = requests.post(url = URL, headers = headers, data=body)
data = json.loads(r.content)
print (type(data))  
print('Review id :')
print(data['review']['id'])
reviewId=data['review']['id']

#Ajout de commentaires
print("Test ajout de commentaires1")
URL = "http://localhost:8585/api/review-requests/3/reviews/"+str(reviewId)+"/diff-comments/"
body= {
    "filediff_id" : "3",
    "first_line" : "2",
    "num_lines" : "2",
    "text" : "Premier commentaire21"
}
r = requests.post(url = URL, headers = headers, data=body)
# extracting data
data = json.loads(r.content)
print (type(data))  

print(data['diff_comment']['id'])

print("Test ajout de commentaires2")
URL = "http://localhost:8585/api/review-requests/3/reviews/"+str(reviewId)+"/diff-comments/"
body= {
    "filediff_id" : "3",
    "first_line" : "5",
    "num_lines" : "1",
    "text" : "Deuxieme commentaire"
}
r = requests.post(url = URL, headers = headers, data=body)
# extracting data
data = json.loads(r.content)
print (type(data))  
print(data)
#Publier la review
print("Publier la revue")
URL = "http://localhost:8585/api/review-requests/3/reviews/"+str(reviewId)+"/"
r=requests.put(url=URL, data={"public" : "true"}, headers = headers)
data = r.content
print ("type(data)") 
print(data["review"]["public"])
