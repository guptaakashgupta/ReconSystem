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
        condition='good'

        cursor.execute('SELECT c.return_date,c.condition,c.return_amount,'
                       'd.channel,d.order_number,d.net_amount, '
                       'd.sale_date,d.invoice_number,d.item,d.quantity '
                       'FROM recon_return c RIGHT OUTER JOIN '
                       '(SELECT a.channel,a.order_number,a.sale_date,a.net_amount,a.invoice_number,a.item,a.quantity '
                       'FROM recon_order as a LEFT OUTER JOIN recon_payment as b  '
                       'ON a.order_number=b.order_number  '
                       'WHERE b.order_number is null )  d '
                       ' ON c.order_number=d.order_number '
                       'WHERE c.condition<>%s OR c.condition is null AND '
                        'd.sale_date BETWEEN %s AND %s ',[condition,start_date,end_date])


        order_payment_pending=dictfetchall(cursor)

        cursor.execute('SELECT a.channel,a.order_number,a.sale_date,a.net_amount,a.invoice_number,'
                       'a.item,a.quantity,b.pay_date,b.payment_amount '
                       'FROM recon_order a,recon_payment b '
                       'WHERE a.order_number=b.order_number AND '
                       'a.net_amount<>b.payment_amount AND '
                       'a.sale_date BETWEEN %s AND %s ',[start_date,end_date])

        order_payment_mismatch=dictfetchall(cursor)
        order_data= {
            "order_detail":order_payment_pending,
            "order_mismatch":order_payment_mismatch,
            "form":form
        }
        return render(request,'base.html',order_data)
    else:
        form=PeriodForm()
        return render(request,'base.html',{'form':form})


def home_view(request):
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
        condition='good'

        cursor.execute('SELECT c.return_date,c.condition,c.return_amount,'
                       'd.channel,d.order_number,d.net_amount, '
                       'd.sale_date,d.invoice_number,d.item,d.quantity '
                       'FROM recon_return c RIGHT OUTER JOIN '
                       '(SELECT a.channel,a.order_number,a.sale_date,a.net_amount,a.invoice_number,a.item,a.quantity '
                       'FROM recon_order as a LEFT OUTER JOIN recon_payment as b  '
                       'ON a.order_number=b.order_number  '
                       'WHERE b.order_number is null )  d '
                       ' ON c.order_number=d.order_number '
                       'WHERE c.condition<>%s OR c.condition is null AND '
                        'd.sale_date BETWEEN %s AND %s ',[condition,start_date,end_date])


        order_payment_pending=dictfetchall(cursor)

        cursor.execute('SELECT a.channel,a.order_number,a.sale_date,a.net_amount,a.invoice_number,'
                       'a.item,a.quantity,b.pay_date,b.payment_amount '
                       'FROM recon_order a,recon_payment b '
                       'WHERE a.order_number=b.order_number AND '
                       'a.net_amount<>b.payment_amount AND '
                       'a.sale_date BETWEEN %s AND %s ',[start_date,end_date])

        order_payment_mismatch=dictfetchall(cursor)
        order_data= {
            "order_detail":order_payment_pending,
            "order_mismatch":order_payment_mismatch,
            "form":form
        }
        return render(request,'index.html',order_data)
    else:
        form=PeriodForm()
        return render(request,'index.html',{'form':form})


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]
