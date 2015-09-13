from django.shortcuts import render
from forms import PeriodForm
from models import Order

# Create your views here.
def index_view(request):
    if request.method == 'GET':
        form=PeriodForm(request.GET)
        start_date_year=request.GET.get('start_date_year','2010')
        end_date_year=request.GET.get('start_date_year','2010')

        order_info=Order.objects.filter(sale_date__year=start_date_year)
        order_data= {
            "order_detail":order_info,
            "form":form
        }
        return render(request,'base.html',order_data)
    else:
        form=PeriodForm()
        return render(request,'base.html',{'form':form})
