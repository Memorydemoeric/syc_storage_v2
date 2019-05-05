"""syc_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from purchase import views as purchase_views
from storage import views as storage_views
from report import views as report_views
from basic_info import views as basic_info_views
from system_maintain import views as system_maintain_views

urlpatterns = [
    path(r'admin/', admin.site.urls),


    path(r'', purchase_views.show_purchase_index),
    path(r'purchase_index/', purchase_views.ShowPurchaseIndex.as_view(), name='purchase_index'),
    # path(r'create_purchase_order/', purchase_views.CreatePurchaseOrder.as_view(), name='create_purchase_order'),


    path(r'storage_index/', storage_views.ShowStorageIndex.as_view(), name='storage_index'),


    path(r'report_index/', report_views.ShowReportIndex.as_view(), name='report_index'),


    path(r'basic_info_index/', basic_info_views.ShowBasicInfoIndex.as_view(), name='basic_info_index'),
    path(r'basic_info/customer_info/', basic_info_views.ShowCustomerInfo.as_view(), name='customer_info'),
    path(r'basic_info/upload_customer_info/', basic_info_views.UploadCustomerInfo.as_view(), name='upload_customer_info'),
    path(r'basic_info/add_customer_info/', basic_info_views.AddCustomerInfo.as_view(), name='add_customer_info'),
    path(r'basic_info/modify_customer_info/', basic_info_views.ModifyCustomerInfo.as_view(), name='modify_customer_info'),
    path(r'basic_info/delete_customer_info/', basic_info_views.DeleteCustomerInfo.as_view(), name='delete_customer_info'),


    path(r'system_maintain_index/', system_maintain_views.ShowSystemMaintainIndex.as_view(),
         name='system_maintain_index'),


]
