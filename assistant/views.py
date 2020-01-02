## ...略...
## 新增下面這行
from .forms import DiaryForm, MoneyForm
## ...略...

class DiaryCreate(LoginRequiredMixin, CreateView):
    # 刪除 model = Diary 以及 fields = ['memo']
    # 新增指定 form_class = DiaryForm
    form_class = DiaryForm
    success_url = "/"
    template_name = 'form.html'

class DiaryUpdate(LoginRequiredMixin, UpdateView):
    model = Diary
    # 刪除 fields = '__all__'
    # 新增指定 form_class = DiaryForm
    form_class = DiaryForm
    success_url = "/"
    template_name = 'form.html'

## ...略...
class MoneyCreate(LoginRequiredMixin, CreateView):
    # 刪除 model = Money 以及 fields = __all__
    # 新增指定 form_class = MoneyForm
    form_class = MoneyForm
    success_url = "/web/money"
    template_name = 'form.html'

class MoneyUpdate(LoginRequiredMixin, UpdateView):
    model = Money
    # 刪除 fields = __all__
    # 新增指定 form_class = MoneyForm
    form_class = MoneyForm
    success_url = "/web/money"
    template_name = 'form.html'

## ...略...