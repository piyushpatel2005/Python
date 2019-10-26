from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


# Check feed at http://localhost:8000/blog/feed/
class LatestPostsFeed(Feed):
    title = 'My blog'  # provides title to RSS elements
    link = '/blog/'  # provides link tag to RSS elements
    description = 'New posts of Piyush\'s blog.'  # provides description

    # retrieves the objects to be included in the feed
    def items(self):
        return Post.published.all()[:5]  # retrieve last 5 published posts

    # this method returns item title
    def item_title(self, item):
        return item.title

    # This returns item description
    def item_description(self, item):
        return truncatewords(item.body, 30)  # return 30 words only
