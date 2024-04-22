from .models import Post
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def q_search(query):
    """Полнотекстовый поиск по заголовку и описанию статей"""
    vector = SearchVector('title', 'content')
    query = SearchQuery(query)
    return Post.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')
