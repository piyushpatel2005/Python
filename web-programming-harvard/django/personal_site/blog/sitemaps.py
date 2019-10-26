from django.contrib.sitemaps import Sitemap
from .models import Post


# Check sitemap at http://localhost:8000/sitemap.xml
class PostSitemap(Sitemap):
    changefreq = 'weekly'  # change frequency of your post pages
    priority = 0.9  # change relevance in website, maximum 1

    # returns the QuerySet of objects to include in this sitemap
    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
