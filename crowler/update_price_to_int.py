import bson
from eyesmediapydb.mongo_base import MongoClientProvider
from eyesmediapydb.mongo_base import MongoConfig
from eyesmediapydb.__init__ import DefaultDBConfig


# setting my db collection
mongoConfig = MongoConfig(host="13.114.67.48", dbname="nlubot_dictionary", username="nlubot", password="28010606", port= 27017, replicaset=None)
mongoConfig.auth_mode = "SCRAM-SHA-1"
provider = MongoClientProvider(mongoConfig)
db = provider.create_client()
collection = db.dev_parse_source


cursor = collection.find({})
for data in cursor:
    print(data["item_id"])
    collection.update(
        {"item_id": data["item_id"]},
        {
            "$set":
            {
                "item_price": int(data["item_price"])
            }
        }
    )