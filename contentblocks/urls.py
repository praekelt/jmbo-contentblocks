from django.conf.urls import include, url

from jmbo.views import ObjectDetail


urlpatterns = [
    url(
        r"^(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="contentblock-detail"
    ),
]
