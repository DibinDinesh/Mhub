from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()#=object creation

router.register("actors",views.ActorViewSet,basename="actors")
#router_object.urls
router.register("filims",views.MovieViewSet,basename="filims")

router.register("albums",views.AlbumViewSet,basename="albums")

router.register("tracks",views.TrackViewSetView,basename="tracks")

urlpatterns = [


    path("movies/",views.MovieListCreateView.as_view()),

    path("movies/<int:pk>/",views.MovieRetriveUpdateDestroyView.as_view()),

    path("movies/languages/",views.LanguagesView.as_view()),

    path("movies/genres/",views.GenreListView.as_view()),


]+router.urls