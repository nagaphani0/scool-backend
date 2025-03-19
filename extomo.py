# import pandas as pd
from pymongo import MongoClient


class DatabaseClass:
    def __init__(self):
        mongo_uri = 'mongodb+srv://naga:naga@mycluster.sehv2.mongodb.net/'  # Replace with your MongoDB URI
        client = MongoClient(mongo_uri)
        self.vvismdb = client["vvism"]
        self.student_coll = self.vvismdb["studentColl"]

    def get_profile(self,data):
        roll_number = data.get('roll_number')
        password = data.get('password')

        record=self.student_coll.find_one({'roll_number': roll_number, 'password': password})
        record['_id'] = str(record['_id'])
        return record
        
    def get_all_records(self):
        records = []  # List to store all records

        print("Data in the collection:")
        for doc in self.student_coll.find():
            doc['_id'] = str(doc['_id'])
            records.append(doc)  
            # print(doc) 

        return records 

    def insert_record(self,data):
        for record in data:
            try:
                self.student_coll.insert_one(record)
                print(f"Inserted record: {record}")
            except Exception as e:
                print(f"Failed to insert record: {record}. Error: {e}")


    def reset_password(self,data):
        if not data:
            return {'error': 'No data provided'}

        roll_number = data.get('roll_number')
        current_password = data.get('current_password')
        new_password = data.get('new_password')

        if not roll_number or not current_password or not new_password:
            return {'error': 'Roll number, current password, and new password are required'}

        record = self.student_coll.find_one({'roll_number': roll_number, 'password': current_password})

        if not record:
            return {'error': 'Invalid roll number or current password'}, 401

        # Update the password
        result = self.student_coll.update_one(
            {'roll_number': roll_number},
            {'$set': {'password': new_password}}
        )

        if result.modified_count > 0:
            return {'message': 'Password reset successfully'}, 200
        else:
            return {'error': 'Failed to reset password'}, 500



# df = pd.read_excel('demo.xlsx', sheet_name='Sheet1')

# data = df.to_dict(orient='records')

# DatabaseClass().insert_record(data)