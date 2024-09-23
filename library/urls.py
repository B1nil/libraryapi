
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from book import views
from rest_framework.authtoken import views as view1  # module aliasing



router = SimpleRouter()
router.register('books',views.BookView)
router.register('user',views.Register)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.book_List,name="books"),
    # path('',views.BookListView.as_view(),name="books"),
    # path('book_details/<int:pk>',views.book_details,name="details"),
    # path('book_details/<int:pk>',views.BookDetailView.as_view(),name="details"),
    path('', include(router.urls)),
    path('search',views.SearchView.as_view()),
    path('login/',view1.obtain_auth_token), # login view from chrome authentication in rest - token authentication
    path('logout/',views.LogoutApiView.as_view()) # logout-view
]
