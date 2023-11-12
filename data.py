from typing import Any
from pymongo import MongoClient,errors
from JobAppData import JobAppData
import sys

class JobAppDao:
    def __init__(self) -> None:
        try:
            uri = "mongodb+srv://cluster0.5jai7nf.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
            client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='X509-cert.pem')
        except errors.ConfigurationError:
            print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
            sys.exit(1)
        db = client['JonApplicationData']
        collection = db['ApplicationsData']
        self.collection = collection

    def insert_jobapp(self, jobAppData: JobAppData) -> Any:
        update_operation = {"$set": jobAppData.to_dict()}
        query = {
            "userId": jobAppData.userId,
            "emailId": jobAppData.emailId,
            "jobTitle": jobAppData.jobTitle,
            "companyName": jobAppData.companyName
        }
        self.collection.find_one_and_update(query, update_operation, upsert=True, return_document=True)

    def find_all_jobapp(self, userId, emailId, skip, limit, sortfields):

        result = self.collection.aggregate([
            {"$match": {
                "userId": userId,
                "emailId": emailId
            }},
            {"$sort": sortfields},
            {"$skip": skip},
            {"$limit": limit}
        ])
        return self.parse_cursor(result)
    
    def update_job_app(self, jobAppData:JobAppData) ->None:
        query = {
            "userId": jobAppData.userId,
            "emailId": jobAppData.emailId,
            "jobTitle": jobAppData.jobTitle,
            "companyName": jobAppData.companyName
        }
        update_operation = {
            "$set": {
                "jobStatus": jobAppData.jobStatus
            }
        }
        return self.collection.find_one_and_update(query, update_operation, return_document=True)

    def parse_cursor(self, cursor):
        jobApps = []
        for jobApp in cursor:
            jobApps.append({
                "emailId":jobApp['emailId'],
                "companyName":jobApp['companyName'],
                "jobTitle":jobApp['jobTitle'],
                "jobUrl":jobApp['jobUrl'],
                "createdDate": jobApp['createdDate']
            })
        return jobApps
