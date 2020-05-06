from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Wine, GrapeSort, Rating
from .forms import ReviewForm, RatingForm


class CountyYear:

    def get_sorts(self):
        return GrapeSort.objects.all()

    def get_countries(self):
        return Wine.objects.filter().distinct().values("country")


class WinesView(CountyYear, ListView):
    model = Wine
    queryset = Wine.objects.all()
    paginate_by = 2


class WineDetailView(CountyYear, DetailView):
    # Опиисание фильма
    model = Wine
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        wine = Wine.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.wine = wine
            form.save()
        return redirect(wine.get_absolute_url())


class GrapeView(CountyYear, DetailView):
    model = GrapeSort
    template_name = 'wines/grape_sort.html'
    slug_field = 'name'


class FilterWinesView(ListView):
    def get_queryset(self):
        queryset = Wine.objects.filter(
            Q(country__in=self.request.GET.getlist("country")) |
            Q(grape_sort__in=self.request.GET.getlist("sort"))
        )
        return queryset


class AddStarRating(View):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                wine_id=int(request.POST.get("wine")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Wine.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context