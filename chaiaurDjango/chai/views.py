from django.shortcuts import render, get_object_or_404 , redirect
from .models import ChaiVaraity, Store ,CustomerOrder,Review,Video
from .forms import ChaiVarityForm ,CustomerOrderForm,ReviewForm,VideoForm
from django.contrib import messages 
from django.db.models import Avg
from django.urls import reverse
import json 

# View to display all chai varieties
def all_chai(request):
    chais = ChaiVaraity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

# View for details of a specific chai variety
def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVaraity, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})



# View to handle the buying process
def buy_tea(request):
    tea_name = request.GET.get('tea_name', 'Unknown Tea')
    tea_price = request.GET.get('tea_price', 0)

    try:
        tea_price = float(tea_price)
    except ValueError:
        tea_price = 0.0

    if request.method == 'POST':
        form = CustomerOrderForm(request.POST)
        if form.is_valid():
            # Handle additional tea data
            additional_tea = []
            selected_teas = request.POST.getlist('additional_tea[]')
            quantities = request.POST.getlist('additional_quantity[]')

            for tea_id, quantity in zip(selected_teas, quantities):
                try:
                    chai = ChaiVaraity.objects.get(id=tea_id)
                    quantity = int(quantity)
                    additional_tea.append({
                        'tea_id': chai.id,
                        'name': chai.name,
                        'price': chai.price,
                        'quantity': quantity,
                        'total': chai.price * quantity
                    })
                except (ChaiVaraity.DoesNotExist, ValueError):
                    continue

            # Save the order
            order = form.save(commit=False)
            order.tea_name = tea_name
            order.tea_price = tea_price
            order.price = tea_price * order.quantity
            order.total_price = sum(item['total'] for item in additional_tea) + order.price
            order.additional_tea = additional_tea  # JSON serialization handled by Django's JSONField
            order.save()

            # Redirect to a thank-you page
            return render(request, 'chai/thank_you.html', {'order': order})
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = CustomerOrderForm()

    return render(request, 'chai/buy.html', {
        'tea_name': tea_name,
        'tea_price': tea_price,
        'form': form,
        'chais': ChaiVaraity.objects.all(),
    })

    
# View for displaying chai stores
def chai_store_view(request):
    stores = None  # Initialize stores as None for cases when there is no POST request
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            # Get the selected chai variety from the form
            chai_variety = form.cleaned_data['chai_varity']
            
            # Query the database for stores offering the selected chai variety
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        # Create an empty form for GET requests
        form = ChaiVarityForm()
    
    # Render the template with the form and stores queryset
    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})



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

    # Fetch all reviews and order by creation date (newest first)
    reviews = Review.objects.all().order_by('-created_at')  # Added ordering by created_at (desc)

    return render(request, 'chai/reviews_page.html', {
        'form': form,
        'message': message,
        'overall_rating': overall_rating,
        'reviews': reviews,
    })


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')  # Redirect to a video list view
    else:
        form = VideoForm()
    return render(request, 'chai/upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all().order_by('-uploaded_at') 
    return render(request, 'chai/video_list.html', {'videos': videos})




