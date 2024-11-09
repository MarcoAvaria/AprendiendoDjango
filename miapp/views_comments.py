# def articulos(request):
    
    # articulos = Article.objects.order_by('title')
    # articulos = Article.objects.order_by('-title')
    # articulos = Article.objects.order_by('id')[:3]
    # articulos = Article.objects.order_by('id')[2:5]
    
    # articulos = Article.objects.filter(title="Batman")
    
    # articulos = Article.objects.filter(title_contains="articulo")
    
    # articulos = Article.objects.filter(title__exact="articulo")
    
    # articulos = Article.objects.filter(title__iexact="articulo")
    
    # Mayores que 12
    # articulos = Article.objects.filter(id__gt=12)
    
    # Mayores o iguales a 12
    # articulos = Article.objects.filter(id__gte=12)
    
    # Menores que 12
    # articulos = Article.objects.filter(id__lt=12)
    
    # Menores o iguales a 12
    # articulos = Article.objects.filter(id__lte=12)
    
    # Se pueden combinar condicionales/filtros
    # articulos = Article.objects.filter(id__gt=12, title_contains="articulo")
    
    # exclude quita de la lista los que cumplan con el argumento como condición
    # articulos = Article.objects.filter(
    #     title="Articulo",
    # ).exclude(
    #     public=True,
    # )
    
    
    # Con raw se pueden hacer consultas SQL directas
    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo 2' AND public=0")
    
    # Con "Q" se puede hacer filtros con lo que "|" puede hacer de "OR"
    # articulos = Article.objects.filter(
    #     Q(title__contains="2") | Q(title__contains="3")
    # )
    
    # articulos = Article.objects.all()
    
    # return HttpResponse(articulos)
    # return render(request, 'articulos.html',{
    #     'articulos':articulos
    # })