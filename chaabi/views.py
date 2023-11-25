#Endpoints (A URL from where you can access data from)
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Drinks
from .models import Product
from .serializers import DrinkSerializer
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from django.shortcuts import render
from .management.commands.query_search import Command
from .management.commands.query_search import query_handler
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
import re
from transformers import GPT2Model, GPT2Tokenizer, GPT2LMHeadModel

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        #get all drinks
        drinks = Drinks.objects.all()
        #serialize them
        serializer = DrinkSerializer(drinks, many = True)
        #return json
        # return JsonResponse(serializer.data,safe =False)
        # serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request, id, format=None):
    
    try:
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','DELETE'])
def product_list(request,format=None):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    if request.method == 'DELETE':
        products = Product.objects.all()
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def home_page(request):
    return render(request, 'search.html')

@api_view(['POST'])
def query_view(request):
    # Your logic to handle the POST request
    query = request.data.get('query', '')
    # ... perform processing ...
    # print(query)

    # command = Command()
    # hits = command.handle(query)
    hits = query_handler(query)
    result = [hit for hit in hits]
    # return Response({'result': result})
    # print(result)
    # tokenizer = AutoTokenizer.from_pretrained('gpt2')
    # model = AutoModelForCausalLM.from_pretrained('gpt2')
    # pipe = pipeline("text-generation", model = model, tokenizer=tokenizer, max_new_tokens=512, device_map="auto")
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2Model.from_pretrained('gpt2')
    qa_model = pipeline('question-answering', model='distilbert-base-cased-distilled-squad', tokenizer='distilbert-base-cased-distilled-squad')

    context = " ".join([f"{str(i.payload['fields']['vector'])}" for i in result]) 
    # print(context)
    answer = qa_model(question=query, context=context)
    # prompt_template = f"Relevant Context: {context}. <br> <br> The User's Question: {query}"
    # print(prompt_template)
    # response = pipe(prompt_template)
    # for i in result:
    #     print(i.payload['fields']['vector'])
    # # print(context)
    # print(response)
    # print(response[0]["generated_text"])
    # response[0]['generated_text'] = clean_string(response[0]['generated_text'])
    # print(response)


    return Response({'result': answer})

    
def clean_string(input_string):
    # Define a regular expression pattern to match unwanted characters
    pattern = re.compile('[^a-zA-Z0-9,?!:\'.\s]')

    # Use the pattern to replace unwanted characters with an empty string
    cleaned_string = re.sub(pattern, '', input_string)

    return cleaned_string