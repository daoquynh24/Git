from rest_framework.pagination import PageNumberPagination


class IndexPagination(PageNumberPagination):
    page_size = 256
    page_size_query_param = 'page_size'
    max_page_size = 256