import pandas as pd
import json
from django.core.management.base import BaseCommand
from chaabi.models import Product

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        df = pd.read_csv("bigBasketProducts.csv")
        json_data = df.to_json(orient="records")
        parsed_data = json.loads(json_data)
        # print(parsed_data[55])
        # print(parsed_data[56])
        for idx, doc in enumerate(parsed_data):
            # print(idx)
            if doc["description"] is None:
                # print(doc)
                doc["description"] = doc["category"] +" " + doc["sub_category"]
            
            if doc["rating"] is None:
                doc["rating"] = 0.0

            if doc["brand"] is None:
                doc["brand"] = "Not Available"
            
            if doc["product"] is None:
                doc["product"] = "Not Available"
            
            Product.objects.create(
                index = doc["index"],
                product = doc["product"],
                category = doc["category"],
                sub_category = doc["sub_category"],
                brand = doc["brand"],
                sale_price = doc["sale_price"],
                market_price = doc["market_price"],
                type = doc["type"],
                rating = doc["rating"],
                description = doc["description"],
                vector = f"Product named {doc['product']} is of type {doc['type']} belonging to category {doc['category']} and subcategory {doc['sub_category']}. Also it has a brand {doc['brand']}. It's Market price is {doc['market_price']} and Sales Price is {doc['sale_price']}. USer Ratings are {doc['rating']} and has the following description {doc['description']}"
            )
        
        self.stdout.write(self.style.SUCCESS('Data Imported Successfully'))

        