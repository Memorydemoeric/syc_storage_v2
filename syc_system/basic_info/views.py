from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from basic_info.helper import OperateCustomerInfo
from basic_info.models import CustomerInfo
from common.base_forms import SearchLocationOrNameForm, UploadFileForm
from common.excel_operate import translate_excel_data
from common.file_operate import create_customer_info_file


class ReportBaseView(View):
    data = dict()
    json_data = dict()
    data['basic_info_title'] = 'active'


class ShowBasicInfoIndex(ReportBaseView):
    def get(self, request):
        self.data['title'] = '基本资料'
        return render(request, 'basic_info_index.html', self.data)


class ShowCustomerInfo(ReportBaseView):
    def get(self, request):
        form_search = SearchLocationOrNameForm(request.GET)
        form_file = UploadFileForm()
        if form_search.is_valid():
            self.data['title'] = '客户资料'
            self.data['search_condition'] = form_search
            self.data['upload_file'] = form_file
            self.data['customer_infos'] = CustomerInfo.get_all_customer_info()
            return render(request, 'customer_info.html', self.data)
        else:
            return HttpResponse('请正确访问...')


class UploadCustomerInfo(ReportBaseView):
    def post(self, request):
        form_file = UploadFileForm(request.POST, request.FILES)
        if form_file.is_valid():
            fr = form_file.files.get('upload_file')
            file_path = create_customer_info_file(fr)
            data_lt, check_word = translate_excel_data(file_path)
            if check_word == '客户资料':
                try:
                    OperateCustomerInfo.bulk_create_customer_info(data_lt)
                except Exception as e:
                    print('error', e)
                    self.json_data['code'] = 'error'
                else:
                    self.json_data['code'] = 'ok'
            else:
                self.json_data['code'] = 'error'
            return JsonResponse(self.json_data)
