from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def myview(request: HttpRequest) -> HttpResponse:
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits
    if num_visits > 4:
        del request.session["num_visits"]
    resp = HttpResponse(f"View count: {num_visits}")
    resp.set_cookie("dj4e_cookie", "eea1c0b5", max_age=1000)
    return resp
