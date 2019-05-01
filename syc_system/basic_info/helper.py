from basic_info.models import CustomerInfo, CustomerRank


class OperateCustomerInfo(object):
    @staticmethod
    def bulk_create_customer_info(data_lt):
        create_lt = [CustomerInfo(location=line[0], name=line[1], mobilephones=str(line[2]).split('.')[0],
                                  address=line[4], phone=str(line[3]).split('.')[0],
                                  default_rebate=line[5]) for line in data_lt[2:]]
        CustomerInfo.objects.bulk_create(create_lt)
        for cust_info in CustomerInfo.get_all_customer_info():
            CustomerRank.objects.create(customer_info=cust_info)
