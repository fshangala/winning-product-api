from rest_framework.routers import DefaultRouter
from sales_tracker import views

salesTrackerRouter=DefaultRouter()
salesTrackerRouter.register(r"sales-tracker",viewset=views.StoreViewSet,basename="sales-tracker")
salesTrackerRouter.register(r"sales-tracker/track-data",viewset=views.TrackDataViewSet,basename="sales-tracker-data")