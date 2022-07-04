from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet

from api.models import Data

from dadata import Dadata


@admin.register(Data)
class AddressAdmin(admin.ModelAdmin):
    result = ['result__icontains']
    search_fields = ['result']

    # убираем кнопку "Добавить" в админке
    def has_add_permission(self, request):
        return False

    def get_search_results(self, request: WSGIRequest, queryset: QuerySet, search_term):
        if request.get_full_path().startswith('/admin/api/data/?q='):
            token = "ab17900dad15e70b5340449bb528835b05b011da"
            secret = "3df71589945f847ca7de68c087b81391bd4d4663"
            dadata = Dadata(token, secret)
            response = dadata.clean("address", search_term)
            Data.objects.get_or_create(result=response)
        return queryset, True
