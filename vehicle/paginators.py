from rest_framework.pagination import PageNumberPagination


class VehiclePaginator(PageNumberPagination):
    "Создание разблюдовки при выводе инфо в Постмане"
    page_size = 10
