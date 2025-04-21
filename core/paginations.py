from rest_framework.pagination import PageNumberPagination


class DealerPagination(PageNumberPagination):
    page_size = 20

class ResultPagination(PageNumberPagination):
    page_size = 20

class CarPagination(PageNumberPagination):
    page_size = 20

class MakePagination(PageNumberPagination):
    page_size = 20

class BodyTypePagination(PageNumberPagination):
    page_size = 20

class FeaturePagination(PageNumberPagination):
    page_size = 20

