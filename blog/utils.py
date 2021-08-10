from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Entry


def paginateblog(request, blog, results):
    blog = Entry.objects.order_by('-pub_date')
    result = results
    page = request.GET.get('page')
    paginator = Paginator(blog, result)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blog = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        blog = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, blog, paginator

