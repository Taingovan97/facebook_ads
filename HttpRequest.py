import requests
import js2py
import postmanproxy

id = '100005188112837'
session = requests.Session()
reponse = session.get("https://www.facebook.com/?id=" + id)




print(session.cookies.get_dict())