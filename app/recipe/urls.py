from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'ingredients', views.IngredientViewSet)
router.register(r'recipes', views.RecipeViewSet)

app_name = 'recipe'
urlpatterns = [
    path('', include(router.urls))
]
