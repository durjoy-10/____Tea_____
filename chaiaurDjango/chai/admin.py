from django.contrib import admin
from .models import ChaiVaraity,ChaiRiview,Store,ChaiCertificate

# Register your models here.
class ChaiReviewInLine(admin.TabularInline):
    model = ChaiRiview
    extra = 2

class ChaiVaraityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInLine]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number')

admin.site.register(ChaiVaraity,ChaiVaraityAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
