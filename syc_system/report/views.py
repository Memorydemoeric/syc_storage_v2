from django.shortcuts import render
from django.views import View


class ReportBaseView(View):
    data = dict()
    data['report_title'] = 'active'


class ShowReportIndex(ReportBaseView):
    def get(self, request):
        self.data['title'] = '报表管理'
        return render(request, 'report_index.html', self.data)
