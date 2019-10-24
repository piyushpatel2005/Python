from django import template
from ..models import Post

# Each template tags module need to contain variable called `register` to be valid tag library.
# It is used to register our own template tags and filters.
register = template.Library()

# define a tag called `total_posts`
# Django uses function name as tag name. To define specific name, provide `name` argument.
@register.simple_tag
def total_posts():
    return Post.published.count()

# To use them make them available in template using {% load %} tag. See base.html