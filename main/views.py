from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, GalleryItem, Category
from .forms import OrderForm, ContactForm


def index(request):
    """Главная страница"""
    services = Service.objects.filter(is_active=True)[:3]
    return render(request, 'main/index.html', {
        'services': services,
    })


def about(request):
    """Страница 'О компании'"""
    return render(request, 'main/about.html')


def services(request):
    """Страница со всеми услугами"""
    all_services = Service.objects.filter(is_active=True)
    return render(request, 'main/services.html', {
        'services': all_services,
    })


def gallery(request):
    """Страница галереи работ"""
    categories = Category.objects.all()
    items = GalleryItem.objects.select_related('category').all()

    return render(request, 'main/gallery.html', {
        'categories': categories,
        'all_items': items,
    })


def contact(request):
    """Страница контактов с формой заявки"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо! Мы свяжемся с вами в ближайшее время.')
            return redirect('main:contact')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {
        'form': form,
    })


def order_service(request, service_id=None):
    """Страница оформления заказа"""
    service = None
    if service_id:
        service = get_object_or_404(Service, id=service_id, is_active=True)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(
                request,
                f'Заказ #{order.id} успешно оформлен! Мы свяжемся с вами по телефону {order.phone}'
            )
            return redirect('main:index')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        initial = {}
        if service:
            initial['service'] = service
        form = OrderForm(initial=initial)

    return render(request, 'main/order_form.html', {
        'form': form,
        'selected_service': service,
    })