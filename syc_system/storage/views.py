from django.shortcuts import render
from django.views import View


# Create your views here.

class StorageBaseView(View):
    data = dict()
    data['storage_title'] = 'active'


class ShowStorageIndex(StorageBaseView):
    def get(self, request):
        self.data['title'] = '库存管理'
        return render(request, 'storage_index.html', self.data)

