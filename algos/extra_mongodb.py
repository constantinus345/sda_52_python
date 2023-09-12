#https://www.mongodb.com/products/tools
"""
MongoDb - baza de date pentru documente de tip json/dictionar
S.n. informal baze de date tip noSQL
"""
#pip install pymongo
import pymongo

connection_string = "mongodb://localhost:27017"
client = pymongo.MongoClient(connection_string)
db = client["sda52"]
colectie_documente = db["exemplu_1"]
#aceste elemente nu se populeaza in Mongo pana nu introduc un document json

document_1 = {"nume":"Ion", "varsta": 25}
rez = colectie_documente.insert_one(document_1)
#se insereaza un document cu _id unic alocat de Mongodb, ceva de genu ObjectID(6500806964eee213a78e56a6)
document_2 = {"nume":"Ana",
              "prenume":"Ailenei",
              "varsta": 32}
rez = colectie_documente.insert_one(document_2)
document_3 = {"nume":"Elena",
              "prenume":"Ionescu",
              "varsta": 32,
              "adresa":{"strada":"strada 1",
                        "nr": 23}}
rez = colectie_documente.insert_one(document_3)

#facem o cautare simpla in colectia creata
query = {"nume": "Ion"}
rez_query = colectie_documente.find(query)
for r in rez_query:
    print(r)

query = {"nume": "Ana"}
new_values = {"$set":{"prenume":"Vasilescu"}}
rez = colectie_documente.update_one(query, new_values)

query_stergere = {"nume": "Ion"}
rez = colectie_documente.delete_many(query_stergere) #delete many - sterge toate, delete one - doar primul gasit

