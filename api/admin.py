from django.contrib import admin
from .models import Quote, Role, Show, Ticket

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    # 'id' رو آوردم اول تا لینک ورود به ویرایش باشه و بتونی 'quote' رو تو لیست ادیت کنی
    list_display = ("id", "quote", "role", "show", "key")
    list_display_links = ("id",)  # کلیک روی ID وارد صفحه ویرایش میشه
    list_editable = ("quote",)    # حالا می‌تونی متن دیالوگ رو مستقیم تو لیست تغییر بدی
    search_fields = ("quote", "role__name", "show__name")
    list_filter = ("show",)
    ordering = ("id",)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # برای Ticket هم همین منطق رو رعایت کردم
    list_display = ("id", "quote", "role", "show", "key", "contain_adult_lang")
    list_display_links = ("id",)
    list_editable = ("contain_adult_lang", "quote")

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "id")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "id")
    prepopulated_fields = {"slug": ("name",)}
