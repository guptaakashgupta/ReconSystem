from django.contrib import admin
from models import Order
from models import Payment
from models import Return
from django.http import HttpResponse

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

class OrderResource(resources.ModelResource):
    class Meta:
        model=Order
        import_id_fields = ('order_number',)
        exclude=('id','net_amount')

    def after_save_instance(self,instance,dry_run):
        if not dry_run:
            obj=Order.objects.get(order_number=instance.order_number)
            obj.net_amount=float(instance.sale_price)-(float((float(instance.sale_price)*
                                                ((float(instance.market_fee)+float(instance.payment_collection_fee))
                                                 /100))) +
                                                float(instance.logistic_fee))
            obj.save()


class PaymentResource(resources.ModelResource):
    class Meta:
        model=Payment
        import_id_fields = ('order_number',)
        exclude=('id',)

class ReturnResource(resources.ModelResource):
    class Meta:
        model=Return
        import_id_fields = ('order_number',)
        exclude=('id',)


# Register your models here.
class OrderAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    model=Order
    date_hierarchy = 'sale_date'
    list_display = ('channel','sale_date','order_number','item','quantity','sale_price',
                    'market_fee','logistic_fee','payment_collection_fee','net_amount')
    list_display_links = ('order_number',)
    list_filter = ('channel',)
    ordering = ('sale_date',)
    search_fields = ('channel','sale_date','order_number','item','customer_city')
    actions = ['export_csv']

    resource_class = OrderResource

    def export_csv(self, request, queryset):
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=order.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
            smart_str(u"ID"),
            smart_str(u"channel"),
            smart_str(u"sale_date"),
            smart_str(u"order_number"),
            smart_str(u"invoice_number"),
            smart_str(u"item"),
            smart_str(u"quantity"),
            smart_str(u"customer_name"),
            smart_str(u"customer_city"),
            smart_str(u"base_price"),
            smart_str(u"sale_tax_rate"),
            smart_str(u"sale_price"),
            smart_str(u"market_fee"),
            smart_str(u"logistic_fee"),
            smart_str(u"payment_collection_fee"),
            smart_str(u"net_amount"),
        ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.pk),
                smart_str(obj.channel),
                smart_str(obj.sale_date),
                smart_str(obj.order_number),
                smart_str(obj.invoice_number),
                smart_str(obj.item),
                smart_str(obj.quantity),
                smart_str(obj.customer_name),
                smart_str(obj.customer_city),
                smart_str(obj.base_price),
                smart_str(obj.sale_tax_rate),
                smart_str(obj.sale_price),
                smart_str(obj.market_fee),
                smart_str(obj.logistic_fee),
                smart_str(obj.payment_collection_fee),
                smart_str(obj.net_amount)
            ])
        return response
    export_csv.short_description = u"Export as CSV including Net Amount"


class PaymentAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    model=Payment
    date_hierarchy = 'pay_date'
    list_display = ('channel','pay_date','order_number','item','quantity','payment_amount')
    list_display_links = ('order_number',)
    list_filter = ('channel',)
    ordering = ('pay_date',)
    search_fields = ('channel','pay_date','order_number','item','payment_amount')
    actions = ['export_csv']

    resource_class = PaymentResource

    def export_csv(self, request, queryset):
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=payment.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
            smart_str(u"ID"),
            smart_str(u"channel"),
            smart_str(u"pay_date"),
            smart_str(u"order_number"),
            smart_str(u"item"),
            smart_str(u"quantity"),
            smart_str(u"payment_amount"),
        ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.pk),
                smart_str(obj.channel),
                smart_str(obj.pay_date),
                smart_str(obj.order_number),
                smart_str(obj.item),
                smart_str(obj.quantity),
                smart_str(obj.payment_amount)
            ])
        return response
    export_csv.short_description = u"Export as CSV"

class ReturnAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    model=Order
    date_hierarchy = 'return_date'
    list_display = ('channel','return_date','order_number','item','quantity','condition','return_amount')
    list_display_links = ('order_number',)
    list_filter = ('channel',)
    ordering = ('return_date',)
    search_fields = ('channel','return_date','order_number','item','condition','return_amount')
    actions = ['export_csv']

    resource_class = ReturnResource

    def export_csv(self, request, queryset):
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=return.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
            smart_str(u"ID"),
            smart_str(u"channel"),
            smart_str(u"return_date"),
            smart_str(u"order_number"),
            smart_str(u"item"),
            smart_str(u"quantity"),
            smart_str(u"condition"),
            smart_str(u"return_amount"),
        ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.pk),
                smart_str(obj.channel),
                smart_str(obj.return_date),
                smart_str(obj.order_number),
                smart_str(obj.item),
                smart_str(obj.quantity),
                smart_str(obj.condition),
                smart_str(obj.return_amount)
            ])
        return response
    export_csv.short_description = u"Export as CSV"




admin.site.register(Order,OrderAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Return,ReturnAdmin)
