from django.shortcuts import render, redirect
from django.views import View


class PurchaseBaseView(View):
    data = dict()
    data['purchase_title'] = 'active'


def show_purchase_index(request):
    return redirect('purchase_index/')


class ShowPurchaseIndex(PurchaseBaseView):
    def get(self, request):
        self.data['title'] = '销售管理'
        return render(request, 'purchase_index.html', self.data)


class CreatePurchaseOrder(object):
    pass