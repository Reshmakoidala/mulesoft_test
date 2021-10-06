#importing mongoclient module which helps in establishing connectivity with database server
from pymongo import MongoClient

#establishing connection
client = MongoClient('localhost', 27017)

# creating a database name MyDatabase
db = client['MyDatabase']

#creating collection inside database
movies = db["MyMoviecollection"]

#creating document inside collection
list = [
  { "mname": "Amy", "actor":"rajesh","actress": "shriya","year":"2000","director":"satya"},
  { "mname": "Hallowen", "actor":"ram" ,"actress": "sam","year":"2001","director":"tarun"},
  { "mname": "midnight",  "actor":"raja","actress": "samantha","year":"2002","director":"vyshu"},
  { "mname": "Sandy",  "actor":"ajay","actress": "anjali","year":"2000","director":"bhuvan"},
  { "mname": "Bentard", "actor":"arya", "actress": "sridevi","year":"2003","director":"vamsi"},
  { "mname": "Royalpalace",  "actor":"chaitu","actress": "geetanjali","year":"2004","director":"derick"},
  { "mname": "sye",  "actor":"akhil","actress": "thamannah","year":"2005","director":"kiran"},
  { "mname": "Venom",  "actor":"ravi","actress": "nabanatesh","year":"2006","director":"ganesh"},
  { "mname": "Ben",  "actor":"ayan","actress": "ishwarya","year":"2007","director":"narendra"},
  { "mname": "webstork", "actor":"sirish", "actress": "amruthaiyyar","year":"2008","director":"harsha"},
  { "mname": "Chuck", "actor":"vasu" ,"actress": "tabu","year":"2009","director":"kile"},
  { "mname": "Viola",  "actor":"vikram","actress": "meena","year":"2010","director":"sri"},
]

#inserting the multiple data  into the database
x = movies.insert_many(list)

#findone method returns first occurrence in the selection
y= movies.find_one()
print(y)

#To select data from a collection we use the find method.
#find method returns all occurrences in the selection
for i in movies.find():
	print(i)


