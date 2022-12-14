from django.urls import path

from . import views

app_name="auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:product_id>", views.information, name="information"),
    path("create", views.create, name="create"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("listing", views.listing.as_view(), name="listing")
    # path("nmayesh", views.nmayesh,name="nmayesh")
]
