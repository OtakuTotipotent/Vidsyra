from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Article


def blogs(request):
    articles = Article.objects.filter(status=Article.Status.PUBLISHED)
    query = request.GET.get("q", "").strip()
    if query:
        articles = articles.filter(
            Q(title__icontains=query)
            | Q(summary__icontains=query)
            | Q(category__icontains=query)
        )

    featured_article = articles.filter(is_featured=True).first()
    if featured_article:
        articles = articles.exclude(pk=featured_article.pk)

    return render(
        request,
        "pages/blogs.html",
        {
            "pageTitle": "Blogs Written Out of Pure Curiosity",
            "featured_article": featured_article,
            "articles": articles,
            "search_query": query,
        },
    )


def blog_details(request, slug):
    article = get_object_or_404(
        Article.objects.select_related("author", "source_video"),
        slug=slug,
        status=Article.Status.PUBLISHED,
    )
    return render(
        request,
        "pages/blog-details.html",
        {"pageTitle": article.title, "article": article},
    )
