from django.shortcuts import render
from taggit.models import Tag
from .models import Post
from django.views.generic import ListView


class TagMixin(object):
    """ To handle all the tags that you have included in your posts """
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class TagIndexView(TagMixin, ListView):
    """ Tags Indexing """
    model = Post
    template_name = "blog.html"
    context_object_name = "Q"
    ordering = ['-date_posted']

    # Tags Handling
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


class Blog(TagMixin, ListView):
    template_name = "blog.html"
    model = Post
    paginate_by = 5
    queryset = Post.objects.all().order_by('-date_posted')
    context_object_name = "Q"
