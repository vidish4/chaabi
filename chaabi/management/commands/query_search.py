from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import CollectionStatus
from sentence_transformers import SentenceTransformer
import pandas as pd
import json
from django.core.management.base import BaseCommand
from django.core.serializers import serialize
from chaabi.models import Product
# from qdrant.api import Qdrant
import pickle

class Command(BaseCommand):
    help = 'Perform a query search in Qdrant'

    def handle(self, *args, **options):
        # Your Qdrant setup code here

        with open('qdrant.pkl', 'rb') as qdrant_file:
            qdrant = pickle.load(qdrant_file)

        encoder = SentenceTransformer("all-MiniLM-L6-v2")
        # Take user input for the query text
        # query_text = input("Enter your query text: ")
        # print(query_text)
        # Encode the query text to get the query vector
        # query_vector = encoder.encode(query_text).tolist()

        # Perform a search in the "big_basket_products" collection
        # hits = qdrant.search(
        #     collection_name="big_basket_products",
        #     query_vector=query_vector,
        #     limit=5,
        # )
        # Handle and display the results
        # for result in hits:
        #     self.stdout.write(self.style.SUCCESS(f"Record ID: {result.id}, Payload: {result.payload}"))
        # for hit in hits:
        #     print(hit)
        return query_handler(qdrant,encoder)

def query_handler(query_text):
    # Your Qdrant setup code here

        with open('qdrant.pkl', 'rb') as qdrant_file:
            qdrant = pickle.load(qdrant_file)

        encoder = SentenceTransformer("all-MiniLM-L6-v2")
        # Take user input for the query text
        # query_text = input("Enter your query text: ")
        # print(query_text)
        # Encode the query text to get the query vector
        query_vector = encoder.encode(query_text).tolist()

        # Perform a search in the "big_basket_products" collection
        hits = qdrant.search(
            collection_name="big_basket_products",
            query_vector=query_vector,
            limit=1,
        )
        # Handle and display the results
        # for result in hits:
        #     self.stdout.write(self.style.SUCCESS(f"Record ID: {result.id}, Payload: {result.payload}"))
        # for hit in hits:
        #     print(hit)
        return hits