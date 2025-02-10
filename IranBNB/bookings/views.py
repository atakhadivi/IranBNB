from django.shortcuts import render
from django.http import JsonResponse
from .airbnb_service import search_destination

def destination_search(request):
    query = request.GET.get('query', 'Chicago')  # Default to Chicago if no query is provided
    country = request.GET.get('country', 'USA')

    try:
        destinations = search_destination(query, country)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse(destinations, safe=False)
