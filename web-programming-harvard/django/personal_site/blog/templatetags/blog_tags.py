from django import template
from ..models import Post
from django.db.models import Count

# Create simple tag
# Each template tags module need to contain variable called `register` to be valid tag library.
# It is used to register our own template tags and filters.
register = template.Library()

# define a tag called `total_posts`
# Django uses function name as tag name. To define specific name, provide `name` argument.
@register.simple_tag
def total_posts():
    return Post.published.count()

# To use them make them available in template using {% load %} tag. See base.html

# Create inclusion tag
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
# Thiscan be used as {% show_latest_posts 3 %}

# Create simple tag that stores result in a variable to directly output its value.
@register.simple_tag
def get_most_commented_posts(count=5):
    # return first 5 posts with most comments
    return Post.published.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments')[:count]