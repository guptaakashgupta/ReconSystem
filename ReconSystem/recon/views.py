from django.shortcuts import render
from forms import PeriodForm
from models import Order
from datetime import date

from django.db import connection

# Create your views here.
def index_view(request):
    if request.method == 'GET':
        form=PeriodForm(request.GET)

        start_date_year=request.GET.get('start_date_year','2010')
        end_date_year=request.GET.get('end_date_year','2010')
        start_date_month=request.GET.get('start_date_month','1')
        end_date_month=request.GET.get('end_date_month','1')
        start_date_day=request.GET.get('start_date_day','1')
        end_date_day=request.GET.get('end_date_day','1')

        start_date=date(int(start_date_year),int(start_date_month),int(start_date_day))
        end_date= date(int(end_date_year),int(end_date_month),int(end_date_day))

        #order_info=Order.objects.filter(sale_date__year=start_date_year)
        cursor=connection.cursor()

        cursor.execute('SELECT a.channel,a.order_number,a.sale_date,a.net_amount,a.invoice_number,a.item,a.quantity,'
                       'b.pay_date,b.payment_amount '
                       'FROM recon_order as a LEFT OUTER JOIN recon_payment as b '
                       'ON a.order_number=b.order_number '
                       'WHERE b.order_number is null AND '
                       'a.sale_date BETWEEN %s AND %s ',[start_date,end_date])

        order_payment_pending=dictfetchall(cursor)
        order_data= {
            "order_detail":order_payment_pending,
            "form":form
        }
        return render(request,'base.html',order_data)
    else:
        form=PeriodForm()
        return render(request,'base.html',{'form':form})


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]
