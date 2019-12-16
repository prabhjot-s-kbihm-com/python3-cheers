# from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
# from cheers.apps.bar.forms.bar import FormBar
# from cheers.apps.bar.forms.bar_timing import BarTimingFormSet
#
#
# class ViewBarAdd(LoginRequiredMixin, CreateView):
#     """
#     This class handle the add bar.
#     """
#
#     form_class = FormBar
#     template_name = "bar/add-bar.html"
#     success_url = reverse_lazy("bar:add-bar")
#
#     def get_form_kwargs(self):
#
#         kwargs = super(ViewBarAdd, self).get_form_kwargs()
#         kwargs['request'] = self.request
#         return kwargs
#
#     def get(self, request, *args, **kwargs):
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         bartiming_form = BarTimingFormSet()
#
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   bartiming_form=bartiming_form))
#
#     def get_context_data(self, **kwargs):
#         context = super(ViewBarAdd, self).get_context_data(**kwargs)
#         return context
#
#     def post(self, request, *args, **kwargs):
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         bartiming_form = BarTimingFormSet(self.request.POST)
#         if (form.is_valid() and bartiming_form.is_valid()):
#             return self.form_valid(form, bartiming_form)
#         else:
#             return self.form_invalid(form, bartiming_form)
#
#     def form_valid(self, form, bartiming_form):
#         print(form.cleaned_data)
#
#         self.object = form.save()
#         # self.object.bar_category_set.add(form.cleaned_data.get('bar_category'))
#         bartiming_form.instance = self.object
#         bartiming_form.save()
#
#         for bar_timing_obj in bartiming_form:
#             bar_timing = bar_timing_obj.save(commit=False)
#             bar_timing.bar = self.object
#             bar_timing.save()
#         messages.info(self.request, "New Bar added successfully")
#         return HttpResponseRedirect(self.get_success_url())
#
#     def form_invalid(self, form, bartiming_form):
#         print(form.cleaned_data)
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   bartiming_form=bartiming_form))
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import  CreateView

from cheers.apps.bar.forms.bar import FormBar


class ViewBarAdd(LoginRequiredMixin, CreateView):
    """
    This class handle the add bar.
    """

    form_class = FormBar
    template_name = "bar/add-bar.html"

    def get_form_kwargs(self):
        kwargs = super(ViewBarAdd, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        obj = form.save()
        messages.info(self.request, "Please added drinks for your new bar.")
        return HttpResponseRedirect(reverse_lazy("bar:drinks", kwargs={'pk':obj.id}))


