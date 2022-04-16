from django.contrib import admin
from tours.models import Tour, RegularTour, TourBooking


@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = ['regular_tour','place_count','mobile','status','is_paid','created','update']
    list_filter = ['status','created','is_paid']
    list_editable = ['status','is_paid']
    search_fields = ['mobile','notice','user__first_name','user__last_name']
    readonly_fields = ['mobile','notice','user']


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title','price','created', 'updated', 'is_active',]
    list_filter = ['created','price','is_active',]
    search_fields = ['title','created','description',]
    list_editable = ['is_active','price',]


@admin.register(RegularTour)
class RegularTourAdmin(admin.ModelAdmin):
    list_display = ['tour','start_datetime','end','places_count','status',]
    list_filter = ['start_datetime','end','status',]
    search_fields = ['tour__title','start','end',]
    list_editable = ["status", "start_datetime","end","places_count",]

