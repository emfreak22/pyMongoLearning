import pymongo
print("Getting Started with pyMongo ")

class pyMongoClass():
    def __init__(self):
        # Creating a client which can be used by functions to execute database operations
        client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = client['firstDatabaase']

    def add_table(self, table_name, data_dictionary):
        # A single dictionary with table name will be passed
        collection = self.db[table_name]
        collection.insert_one(data_dictionary)

    def insert_multiple_rows(self, table_name, data_list):
        # A list of dictionaries will be passed
        collection = self.db[table_name]
        collection.insert_many(data_list)

if __name__ == '__main__':
    # data_dict = {'Name': 'Udit Singh', 'Age': 25}
    # db = pyMongoClass()
    # db.insert_multiple_rows(table_name='firstCollection', data_dict = data_dict)

    list_of_data = [{'_id':1,'Name':'Rahul','Age':21},{'_id':2,'Name':'Rohit','Age':22},{'_id':3,'Name':'Gopal','Age':20},{'_id':4,'Name':'Rahul Mann','Age':21}]
    db = pyMongoClass()
    db.insert_multiple_rows('firstCollection',list_of_data)