from django.core.management.base import BaseCommand
from demo.models import Funds
from dateutil import parser
import requests
class Command(BaseCommand):

    def create_data(self):
        data = requests.get("http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf=53&tp=1&frmdt=01-Apr-2015&todt=21-Apr-2020")
        temp = data.text
        li = temp.split('Axis Mutual Fund')
        re = []
        ind = []
        for item in li:
            item = item.replace('\n','')
            ind.append(item.split('\r'))
            re.append(item.rstrip())
        
        for item in ind:
            while '' in item:
                item.remove('')
        del ind[0]
        for item in ind:
            item.pop()

        final_data = []
        for item in ind:
            for ele in item:
                final_data.append(ele.split(';'))
        
        funds_obj = [Funds(scheme_code=item[0],scheme_name=item[1],\
            isin_div_pay_growth=item[2],isin_div_reinvest=item[3],\
                net_asset_value=item[4],repurchase_price=item[5] if item[5] else 0.0,\
                    sale_price=item[6] if item[6] else 0.0,\
                        date=parser.parse(item[7]).date()) for item in final_data ]
        Funds.objects.bulk_create(funds_obj)
            
        print("Data inserted Successfully!!")

    def handle(self, *args, **options):
        self.create_data()