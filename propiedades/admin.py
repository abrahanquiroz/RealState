from django.contrib import admin


class RealStateAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "country", "city", "postal_code", "type", "area")

    search_fields = (
        "name",
        "city",
        "address",
        "country",
    )
