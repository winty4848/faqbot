from django.conf.urls import url, include

## 언제 include() 를 사용해야 하나요?
## admin.site.urls 를 제외한, 다른 URL 패턴을 include 할 때마다 항상 include() 를 사용해야 합니다.
urlpatterns = [
    url(r'', include('selffaq.urls')),
]
