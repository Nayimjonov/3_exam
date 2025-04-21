from rest_framework.pagination import PageNumberPagination


class DealerPagination(PageNumberPagination):
    page_size = 20
