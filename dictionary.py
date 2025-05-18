import requests
url="https://api.dictionaryapi.dev/api/v2/entries/en/"
x=input("enter the word you want to search:")
url=url+x
res=requests.get(url)
if res.status_code==200:
   a=(res.json())
   a=a[0]["meanings"]
   a=a[0]["definitions"]
   a=a[0]["definition"]
 
  
   print(a)
  
   print(res.json())
else:
    print("no data found")
