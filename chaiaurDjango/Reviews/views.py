from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Review
from .forms import ReviewForm

def reviews_page(request):
    form = ReviewForm()
    message = ""
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Thank You Sir"
            form = ReviewForm()  # Reset the form after submission
    
    # Calculate the overall rating
    overall_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']
    overall_rating = round(overall_rating, 2) if overall_rating else 0

    # Fetch all reviews
    reviews = Review.objects.all()

    return render(request, 'reviews_page.html', {
        'form': form,
        'message': message,
        'overall_rating': overall_rating,
        'reviews': reviews,
    })
