from django.shortcuts import render
from django.views import View


class SystemMaintainBaseView(View):
    data = dict()
    data['system_maintain_title'] = 'active'


class ShowSystemMaintainIndex(SystemMaintainBaseView):
    def get(self, request):
        self.data['title'] = '系统维护'
        return render(request, 'system_maintain_index.html', self.data)
