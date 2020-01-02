from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Expense



class ExpenseList(LoginRequiredMixin, ListView):
    model = Expense
    ordering = ['-id']  
    paginate_by = 10    

## 新增支出紀錄
class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expense
    fields = '__all__'                  
    template_name = 'form.html'         

    def get_success_url(self):
        return reverse('expense_list')  

## 修改支出紀錄
class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = '__all__'
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('expense_list')  

## 刪除支出紀錄
class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('expense_list')  


