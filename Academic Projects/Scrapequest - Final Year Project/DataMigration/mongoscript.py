import csv
from pymongo import MongoClient
from pymongo.errors import BulkWriteError


client = MongoClient("mongodb+srv://sharams:Su9860797972@atlascluster.abktl4t.mongodb.net/")

db = client["SCRAPEQUEST"]

def process_collection(file_path, collection_name, headers):
    collection = db[collection_name]
    # Drop the collection if it already exists
    db.drop_collection(collection_name)
    
    documents = []
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for each in reader:
                row = {field: each.get(field, "").strip() for field in headers}
                documents.append(row)
                # Insert in batches of 100
                if len(documents) == 100:
                    collection.insert_many(documents)
                    count += len(documents)
                    documents = []

        # Insert any remaining documents
        if documents:
            collection.insert_many(documents)
            count += len(documents)

        print(f"Total {count} documents inserted into {collection_name}")
    except FileNotFoundError:
        print(f"Error: File not found {file_path}")
    except csv.Error as e:
        print(f"CSV read error: {e}")
    except BulkWriteError as bwe:
        print(f"Bulk write error: {bwe.details}")
    except Exception as e:
        print(f"An error occurred: {e}")

collections = [
    ('../ScrapeBots/ProjectData/ADB.csv', 'ADB', ['Name of the Project', 'Link to the project', 'Project Status', 'Project Description']),
    ('../ScrapeBots/ProjectData/SDC.csv', 'SDC', ['Name of the Project', 'Link to the project', 'Duration of the Project', 'Project Details']),
    ('../ScrapeBots/ProjectData/UKAID.csv', 'UKAID', ['Name of the Project', 'Link to the project', 'Project Details', 'Start Date']),
    ('../ScrapeBots/ProjectData/UNDP.csv', 'UNDP', ['Name of the Project', 'Link to the project']),
    ('../ScrapeBots/ProjectData/WB.csv', 'WB', ['Name of the Project', 'Link to the project', 'Procurement Details', 'Link to the Procurement','Date of Publishment']),
    ('../ScrapeBots/ProjectData/USAID.csv', 'USAID', ['Name of the Project', 'Duration of the Project', 'Sector']),
    ('../ScrapeBots/ProjectData/UNFAO.csv', 'UNFAO', ['Name of the Project', 'Duration of the Project','Link to the project']),
    ('../ScrapeBots/ProjectData/JICA.csv', 'JICA', ['Name of the Project', 'Link to the project']),
]

for file_path, collection_name, headers in collections:
    process_collection(file_path, collection_name, headers)


    