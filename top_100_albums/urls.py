# API_TITLE = 'Pastebin API'
# API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
# schema_view = get_schema_view(title=API_TITLE)

# urlpatterns = [
#     url(r'^schema/$', schema_view),
#     url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
# ]

from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('top_albums.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
