from django.urls import path
from .views import HomeView
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name="index")

]
    # path('', views.index, name="index"),
    # path('list/', views.viewlist, name="views_list"),
    # path('details/<int:question_id>', views.detailView, name="detail"),
    # path('<int:question_id>', views.vote, name="vote"),
    # path('product/',views.product_view, name="product"),