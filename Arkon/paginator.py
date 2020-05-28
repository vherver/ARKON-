from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Paginator(PageNumberPagination):
    """
    This is the default REST API paginator
    """

    def __init__(self):
        self.page_size = 10
        self.page_size_query_param = 'page_size'
        self.max_page_size = 100

    def get_paginated_response(self, data):
        response = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data,
            'total_pages': self.page.paginator.num_pages,
            'page': self.page.number,
        }
        return Response(response)
