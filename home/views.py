from django.shortcuts import render, get_object_or_404, redirect, reverse


def index(request, *args, **kwargs):
    """A view that displays the index page"""
    return render(request, "index.html", {"home": "index"})


def about(request, *args, **kwargs):
    """A view that displays the about page"""
    return render(request, "about.html", {"home": "about"})
