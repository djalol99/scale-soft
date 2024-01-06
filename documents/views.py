from django_filters.views import FilterView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.db.models.deletion import ProtectedError
from django.contrib import messages
from rest_framework.generics import RetrieveAPIView

from . import models, forms, filtersets
from .serializers import VehicleTareSerializer

class MyCustomDeleteView(DeleteView):
    template_name = 'documents/confirm_delete.html'
    error_url = None
    success_message = "Muvaffaqiyatli o'chirildi."
    error_message = "O'chirishni amalga oshirib bo'lmadi, chunki katalogdan foydalanilgan"

    def delete(self, request, *args, **kwargs):
        response = None
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, self.success_message)
        except ProtectedError:
            error_message = self.error_message
        except Exception:
            error_message = "O'chirishni amalga oshirib bo'lmadi."

        if response is None:
            messages.error(request, error_message, 'danger')
            if self.error_url is None:
                self.error_url = self.success_url
            response = HttpResponseRedirect(self.error_url)
        return response
    

class MyCustomCreateView(CreateView):
    success_message = "Muvaffaqiyatli yaratildi"
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form) 


class MyCustomUpdateView(UpdateView):
    success_message = "Muvaffaqiyatli yangilandi"
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
# Vehicle Tare
class VehicleTareListView(FilterView):
    template_name = 'documents/vehicle_tare_list.html'
    model = models.VehicleTare
    filterset_class = filtersets.VehicleTareFilterSet


class VehicleTareCreateView(MyCustomCreateView):
    template_name = 'documents/vehicle_tare_form.html'
    model = models.VehicleTare
    form_class = forms.VehicleTareForm
    success_url = reverse_lazy('documents:vehicle-tares')


class VehicleTareUpdateView(MyCustomUpdateView):
    template_name = 'documents/vehicle_tare_form.html'
    model = models.VehicleTare
    form_class = forms.VehicleTareForm
    success_url = reverse_lazy('documents:vehicle-tares')
    

class VehicleTareDeleteView(MyCustomDeleteView):
    model = models.VehicleTare
    success_url = reverse_lazy('documents:vehicle-tares')


class LastVehicleTareView(RetrieveAPIView):
    serializer_class = VehicleTareSerializer
    lookup_field = 'vehicle'

    def get_object(self):
        vehicle = self.kwargs['vehicle']
        last_obj =  models.VehicleTare.objects.filter(vehicle=vehicle).last()
        if last_obj is None:
            raise Http404
        return last_obj


# Weighing [gross-tare=netto]
class WeighingListView(FilterView):
    template_name = 'documents/weighing_list.html'
    model = models.Weighing
    filterset_class = filtersets.WeighingFilterSet
    

class WeighingCreateView(MyCustomCreateView):
    template_name = 'documents/weighing_form.html'
    model = models.Weighing
    form_class = forms.WeighingForm
    success_url = reverse_lazy('documents:weighing')


class WeighingUpdateView(MyCustomUpdateView):
    template_name = 'documents/weighing_form.html'
    model = models.Weighing
    form_class = forms.WeighingForm
    success_url = reverse_lazy('documents:weighing')
    

class WeighingDeleteView(MyCustomDeleteView):
    model = models.Weighing
    success_url = reverse_lazy('documents:weighing')