# Class Based View

# https://docs.djangoproject.com/en/4.2/ref/class-based-views/

# TemplateView https://docs.djangoproject.com/en/4.2/ref/class-based-views/base/#templateview

# View https://docs.djangoproject.com/en/4.2/ref/class-based-views/base/#view

# ListView https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#listview
# (Lista os elementos do DB)

# DetailView https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#detailview
# (Através de um id ou pk (ou outro slug) injetado na url, retorna os itens de um elemnto específico)
# exemplo: na urls.py => person_detail/<int:pk>/ , e na url do navegador =>  /person_list/1

# CreateView https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#createview
# ATENCÃO com  enctype="multipart/form-data"  no template class_form.html

# UpdateView https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#updateview
# ATENCAO usar o reverse_lazy() para indicar o link interno

#DeleteView https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#deleteview
