from django.shortcuts import render


def home(request):
    suggested_videos = [
        {
            "link": "https://www.youtube.com/",
            "thumbnail": "https://unsplash.com/photos/red-play-button-icon-niUkImZcSP8",
            "alt": "Youtube Video Thumbnail",
            "title": "Suggested Video's Title Is Shown Here",
        },
        {
            "link": "https://www.youtube.com/",
            "thumbnail": "https://unsplash.com/photos/red-play-button-icon-niUkImZcSP8",
            "alt": "Youtube Video Thumbnail",
            "title": "Suggested Video's Title Is Shown Here",
        },
        {
            "link": "https://www.youtube.com/",
            "thumbnail": "https://unsplash.com/photos/red-play-button-icon-niUkImZcSP8",
            "alt": "Youtube Video Thumbnail",
            "title": "Suggested Video's Title Is Shown Here",
        },
        {
            "link": "https://www.youtube.com/",
            "thumbnail": "https://unsplash.com/photos/red-play-button-icon-niUkImZcSP8",
            "alt": "Youtube Video Thumbnail",
            "title": "Suggested Video's Title Is Shown Here",
        },
    ]

    return render(
        request,
        "home.html",
        {
            "pageTitle": "Home of Intelligence Behind Videos",
            "suggested_videos": suggested_videos,
        },
    )
