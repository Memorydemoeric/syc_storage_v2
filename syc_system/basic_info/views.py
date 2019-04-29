from django.shortcuts import render
from django.views import View


class ReportBaseView(View):
    data = dict()
    data['basic_info_title'] = 'active'


class ShowBasicInfoIndex(ReportBaseView):
    def get(self, request):
        self.data['title'] = '基本资料'
        return render(request, 'basic_info_index.html', self.data)
