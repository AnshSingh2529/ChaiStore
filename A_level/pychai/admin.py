from .models import ChaiVariety, PyChaiReview, PyChaiLike, Store
from django.contrib import admin
# Register your models here.

class ChaiReviewInline(admin.TabularInline):
   model = PyChaiReview
   extra = 1
   
class ChaiLikeInline(admin.TabularInline):
   model = PyChaiLike
   extra = 1
   
class ChaiVarietyAdmin(admin.ModelAdmin):
   list_display = ('name', 'type', 'price', 'date_added')
   inlines = [ChaiReviewInline, ChaiLikeInline]
   
class StoreAdmin(admin.ModelAdmin):
   list_display = ('name', 'location')
   filter_horizontal = ('chai_varieties',)
   
admin.site.register(ChaiVariety,ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)

