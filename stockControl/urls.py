from django.contrib import admin
from django.urls import path
from stockControl.views import login
from stockControl.views import signup
from stockControl.views import password_recovery
from stockControl.views import dashboard
from stockControl.views import ConsumableGoodListView
from stockControl.views import SupplierListView
from stockControl.views import new_consumable_good
from stockControl.views import new_supplier

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login, name="login"),
    path("signup", signup, name="signup"),
    path("password-recovery", password_recovery, name="password_recovery"),
    path("dashboard", dashboard, name="dashboard"),
    path("dashboard/new_consumable_good", new_consumable_good, name="new_consumable_good"),
    path("dashboard/consumables", ConsumableGoodListView.as_view(), name="consumables"),
    path("dashboard/new_supplier", new_supplier, name="new_supplier"),
    path("dashboard/suppliers", SupplierListView.as_view(), name="suppliers"),
]
