import pymongo
print("Getting Started with pyMongo ")

class pyMongoClass():
    def __init__(self):
        # Creating a client which can be used by functions to execute database operations
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['firstDatabaase']

    def list_databases(self):
        all_databases = self.client.list_database_names()
        for db in all_databases:
            print(f"Collections in Database : {db} are : ")
            print(self.client[db].list_collection_names())
        print(all_databases)
    def add_table(self, table_name, data_dictionary):
        # A single dictionary with table name will be passed
        collection = self.db[table_name]
        collection.insert_one(data_dictionary)



    def insert_multiple_rows(self, table_name, data_list):
        '''

        Insert many
        data_list = [{'_id':1,'Name':'Rahul','Age':21},{'_id':2,'Name':'Rohit','Age':22},{'_id':3,'Name':'Gopal','Age':20},{'_id':4,'Name':'Rahul Mann','Age':21}]
        '''
        # A list of dictionaries will be passed
        collection = self.db[table_name]
        collection.insert_many(data_list)

    def find_one(self, find_dict, table_name = 'firstCollection'):
        '''Used to find one single entry, This function gets collection name and two dictionaries, one which has details to find from collection and second which columns to include and exclude.
                find_dict = {'Name': 'Rahul'}
                colmns_to_be_included = {'Age':0,'_id':0} '''
        collection = self.db[table_name]
        return collection.find_one(find_dict)

    def find(self, find_dict,columns= {}, table_name = 'firstCollection'):
        '''Used to find multiple entries, This function gets collection name and two dictionaries, one which has details to find from collection and second which columns to include and exclude.
        find_dict = {'Name': 'Rahul'}
        colmns_to_be_included = {'Age':0,'_id':0} '''
        collection = self.db[table_name]
        return [i for i in collection.find(find_dict, columns)]

    def update(self, table_name='firstCollection'):
        '''Used to update multiple entries'''
        collection = self.db[table_name]
        current_data = {'Name': "Udit"}
        next_data = {"$set": {"Age": 26}}
        collection.update_many(current_data,next_data)

    def delete(self, table_name='firstCollection'):
        '''Used to update multiple entries'''
        collection = self.db[table_name]
        to_delete = {'Name': "Udit"}

        collection.delete_many(to_delete)
    def find_with_parameters(self, table_name = 'firstCollection'):
        '''Used to find multiple entries with lte : less than or equal to parameter'''

        collection = self.db[table_name]
        print( [i for i in collection.find({'Age': {'$lte': 27}}, {'Name':0})])

if __name__ == '__main__':
    db = pyMongoClass()

    # insert one
    # data_dict = {'Name': 'Udit Singh', 'Age': 25}
    # db.insert_multiple_rows(table_name='firstCollection', data_dict = data_dict)

    # insert many
    # list_of_data = [{'_id':1,'Name':'Rahul','Age':21},{'_id':2,'Name':'Rohit','Age':22},{'_id':3,'Name':'Gopal','Age':20},{'_id':4,'Name':'Rahul Mann','Age':21}]
    # db.insert_multiple_rows('firstCollection',list_of_data)

    # find
    # find_dict = {'Name': 'Rahul'}
    # colmns_to_be_included = {'Age':0,'_id':0} # Setting age and id = 0 so that they wont get retrieved.
    # print(db.find(find_dict=find_dict,columns=colmns_to_be_included))

    db.find_with_parameters()


