# # importing the requests library
import requests
import json
# import pypolyspace.Data as Data
# import pypolyspace.Parsers as Parse
# import pypolyspace.Processors as Proc
import os

# Recuperer les diffs
# URL = "http://localhost:8585/api/review-requests/3/diffs/"
# headers = {"Authorization": "token 5a957c0c8cba9ea9a20356fc6dd4d3df302bc679"
#             }  
# r = requests.get(url = URL,headers=headers)
  
# data = json.loads(r.content)
# print ("Numero de la derniere revision")  
# print(data["total_results"])
# Liste des changes
# URL = "http://localhost:8585/api/review-requests/3/diffs/1/files/3/patched-file/"

# headers = {"Authorization": "token 5a957c0c8cba9ea9a20356fc6dd4d3df302bc679"
#             }  
# r = requests.get(url = URL,headers=headers)
  
# data = r.content
# print ("premier test")  
# print(data)

# r2 = requests.get(url = URL)
# print("deuxieme test")
# print(data)

# # #Ajout de commentaires
# # print("Test ajout de commentaires")
# # URL = "http://localhost:8585/api/review-requests/3/reviews/21/diff-comments/"
# # body= {
# #     "filediff_id" : "3",
# #     "first_line" : "2",
# #     "num_lines" : "2",
# #     "text" : "Une erreur ici"
# # }
# # r = requests.post(url = URL, headers = headers, data=body)
# # # extracting data
# # data = r.content
# # print (type(data))  

# # print(data)
# # #Creer une review draft
# # print("Creer une review draft")
# # URL = "http://localhost:8585/api/review-requests/3/reviews/"
# # body= {
    
# # }
# # r = requests.post(url = URL, headers = headers, data=body)
# # data = r.content
# # print (type(data))  

# # print(data)
# # #Publier une review
# # print("Publier la revue")
# # URL = "http://localhost:8585/api/review-requests/3/reviews/12/"
# # # r=requests.put(url=URL, data={"public" : "true"}, headers = headers)
# # # data = r.content
# # # print (type(data)) 
# # # print(data)


# headers = {"Authorization": "token 5a957c0c8cba9ea9a20356fc6dd4d3df302bc679"
#             } 
# #Creer une review draft
# print("Creer une review draft")
# URL = "http://localhost:8585/api/review-requests/3/reviews/"
# body= {
    
# }
# r = requests.post(url = URL, headers = headers, data=body)
# data = json.loads(r.content)
# print (type(data))  
# print('Review id :')
# print(data['review']['id'])
# reviewId=data['review']['id']

# #Ajout de commentaires
# print("Test ajout de commentaires1")
# URL = "http://localhost:8585/api/review-requests/3/reviews/"+str(reviewId)+"/diff-comments/"
# body= {
#     "filediff_id" : "3",
#     "first_line" : "2",
#     "num_lines" : "2",
#     "text" : "Premier commentaire21"
# }
# r = requests.post(url = URL, headers = headers, data=body)
# # extracting data
# data = json.loads(r.content)
# print (type(data))  

# print(data['diff_comment']['id'])

# print("Test ajout de commentaires2")
# URL = "http://localhost:8585/api/review-requests/3/reviews/"+str(reviewId)+"/diff-comments/"
# body= {
#     "filediff_id" : "3",
#     "first_line" : "5",
#     "num_lines" : "1",
#     "text" : "Deuxieme commentaire"
# }
# r = requests.post(url = URL, headers = headers, data=body)
# # extracting data
# data = json.loads(r.content)
# print (type(data))  
# print(data)
# #Publier la review
# print("Publier la revue")
# URL = "http://localhost:8585/api/review-requests/3/reviews/"+str(reviewId)+"/"
# r=requests.put(url=URL, data={"public" : "true"}, headers = headers)
# data = r.content
# print ("type(data)") 
# print(data["review"]["public"])



# # #Get the diff file of review_request number 3        
#         # URL = "http://localhost:8000/api/review-requests/3/diffs/1/files/3/patched-file/"
#         # headers = {'Authorization': 'token 5a957c0c8cba9ea9a20356fc6dd4d3df302bc679'}  
#         # r = requests.get(url = URL,headers=headers)
#         # data = r.content
#         # logging.info(data)
#         # #Adding a comment on review request number 3
#         # URL = "http://localhost:8000/api/review-requests/3/reviews/14/diff-comments/"
#         # body= {
#         #         "filediff_id" : "3",
#         #         "first_line" : "2",
#         #         "num_lines" : "2",
#         #         "text" : "Test commentaire lundi"
#         # }
#         # r = requests.post(url = URL, headers = headers, data=body)  
#         # data = r.content
#         # logging.info(data) 
#         # #Create a new review draft on review request number 4 and publish it
#         # URL = "http://localhost:8000/api/review-requests/4/reviews/"
#         # body= {
#         #         "public" : "true"
#         # }
#         # r = requests.post(url = URL, headers = headers, data=body)
#         # data = r.content
#         # logging.info(data) 


# baseUrl = "http://localhost:8585/api/"
# headers = {'Authorization': 'token 5a957c0c8cba9ea9a20356fc6dd4d3df302bc679'}
# def createReviewDraft(reviewRequestId):
#         URL = str(baseUrl)+"review-requests/"+str(reviewRequestId)+"/reviews/"
#         body= {
#             "body_top" : "Resultat de l'analyse PolySpace"
#         }
#         r = requests.post(url = URL, headers = headers, data=body)
#         data = json.loads(r.content)
         
#         print("Creating review number : ")
#         print(data['review']['id'])
#         id=data['review']['id']
#         return id

# def AddComment(reviewRequestId,reviewId):
#         URL = str(baseUrl)+"review-requests/"+str(reviewRequestId)+"/reviews/"+str(reviewId)+"/diff-comments/"
#         body= {
#             "filediff_id" : "3",
#             "first_line" : "2",
#             "num_lines" : "2",
#             "text" : "Erreur ici!!"
#             }   
#         r = requests.post(url = URL, headers = headers, data=body)
#         data = json.loads(r.content)
#         print("Adding comments")  
#         print(data)
#         commentId=data['diff_comment']['id']
#         return commentId

# def publishReview(reviewRequestId,reviewId):
#         URL = str(baseUrl)+"review-requests/"+str(reviewRequestId)+"/reviews/"+str(reviewId)+"/"
#         r=requests.put(url=URL, data={"public" : "true"}, headers = headers)
#         data = json.loads(r.content)
#         print("Review published : ") 
#         print(data["review"]["public"])





# reviewRequestId=3
# print('Review requestt %s was published!',
#         reviewRequestId)
# reviewId=createReviewDraft(reviewRequestId)
# commentId=AddComment(reviewRequestId,reviewId)        
# published=publishReview(reviewRequestId,reviewId)





#Tester nombre de files
URL = "http://localhost:8585/api/review-requests/3/diffs/1/files/"
headers = {'Authorization': 'token 5a957c0c8cba9ea9a20356fc6dd4d3df302bc679'}  
r=requests.get(url=URL,headers = headers)
data = json.loads(r.content)
print(data["total_results"])
numberOfFiles=data["total_results"]
for x in range(numberOfFiles):
  print(data["files"][0]['dest_file'])
a=(data["files"][0]['id'],data["files"][0]['dest_file'])
print(a)


# class MyJsonConverter(object):
    
#     @staticmethod
#     def run(report):
#         assert isinstance(report, Data.Report)
#         assert len(report.Runs) == 1
#         run = report.Runs[0]
#         print("Have {} findings from Polyspace".format(len(run.Findings)))
#         for f in run.Findings:
#             print("New finding at {}, message='{}', rule='{}'".format(f['location'], f['message'], f['rule']))
#         myrep = dict(polyspace_result=report, comment="my custom json")
#         ret = json.dumps(myrep, indent=True, sort_keys=True, default=lambda o: o.__dict__)
       
#         return ret


# def main():
#   #Tester convertisseur SARIF---->JSON
#   rule_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),"pypolyspace", "data", "ruleData", "ruleData.csv")
      
#   parser = Parse.SarifReader("result_list.sarif", rulefile=rule_data)

#   report = parser.run()
#   print("Parser info: {}".format(parser.info))

#   myfilter = Proc.FilterFindings(filter_func=lambda f: not Proc.FilterFindings.is_metric(f))
#   report = myfilter.run(report)
#   myfilter = Proc.FilterRules(filter_func=lambda r: Proc.FilterRules.is_referenced(r))
#   report = myfilter.run(report)

    
#   converter = MyJsonConverter()
#   myoutput = converter.run(report)
#   data = json.loads(myoutput)
#   print("Final output: {}".format(myoutput))
#   print(data["polyspace_result"] ["Runs"][0] ["Findings"][0]['data']['message'])
#   print(len(data["polyspace_result"] ["Runs"][0] ["Findings"]))
#   return 0
# if __name__ == "__main__":
#     main()
print("bonjour")
textList = ["One", "Two", "Three", "Four", "Five"]
with open('example.txt','w') as outF: 
    for line in textList:
    # write line to output file
        outF.write(line)
        outF.write("\n")
outF.close()


