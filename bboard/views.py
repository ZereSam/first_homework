from django.shortcuts import render
import requests


def fetch_data(request):
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    return render(request, 'data.html', {'data': data})





