from django.contrib import admin
from .models import ChaiVaraity,ChaiRiview,Store,ChaiCertificate,Review,Video,CustomerOrder

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

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'review','created_at')
    
class VideoAdmin(admin.ModelAdmin):
    list_display= ('title','description','video_file','uploaded_at')
    
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display=('name','number','tea_name','tea_price','quantity','price','additional_tea','created_at','total_price')
    

admin.site.register(CustomerOrder,CustomerOrderAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(ChaiVaraity,ChaiVaraityAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
