from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import CollectionStatus
from sentence_transformers import SentenceTransformer
import pandas as pd
import json
from django.core.management.base import BaseCommand
from django.core.serializers import serialize
from chaabi.models import Product
import pickle


class Command(BaseCommand):
    help = 'Convert products to vector embeddings'

    def handle(self, *args, **options):
        encoder = SentenceTransformer("all-MiniLM-L6-v2")
        json_data = serialize('json', Product.objects.all())
        parsed_data = json.loads(json_data)
        # print(parsed_data[0])
        qdrant = QdrantClient(":memory:")
        qdrant.recreate_collection(
            collection_name="big_basket_products",
            vectors_config=models.VectorParams(
                size=encoder.get_sentence_embedding_dimension(),
                distance=models.Distance.COSINE,
            ),
        )
        for idx, doc in enumerate(parsed_data):
            # print(idx)
            qdrant.upload_records(
                collection_name="big_basket_products",
                records=[
                    models.Record(
                        id=idx, vector=encoder.encode(doc['fields']['vector']).tolist(), payload=doc
                    )
                    
                ],
            )

        # Pickle the Qdrant object
        with open('qdrant.pkl', 'wb') as qdrant_file:
            pickle.dump(qdrant, qdrant_file)

        self.stdout.write(self.style.SUCCESS('Vectors Embedded Successfully'))

