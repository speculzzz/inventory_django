from django.shortcuts import render
from django.core.cache import cache


def home_view(request):
    # Redis test
    cache_key = 'home_page_visits'
    visits = cache.get(cache_key, 0)
    cache.set(cache_key, visits + 1, timeout=60)  # Store for 1 minute

    return render(request, 'home.html', {
        'items_link': '/items/',
        'polls_link': '/polls/',
        'visits_count': visits + 1,  # Counter at the context
    })
