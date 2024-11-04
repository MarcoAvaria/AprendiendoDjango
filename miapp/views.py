from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article

# Create your views here.

# Opción 1:
# def index(request):
#     return HttpResponse("""
#         <h1>Inicio</h1>                    
#     """)

layout = """
<h1>Sitio web con Django | Marco Avaria</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
"""

def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul> 
    "" 
    year = 2024
    while year <= 2050: 
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year +=1
        
    html += "</ul"
    """
    
    year = 2024
    hasta = range(year, 2051)
    
    nombre = 'Marco Avaria'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']
    
    # return HttpResponse(layout + html)
    # return render(request, 'index.html')
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable':'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'year': hasta
    })
    

def hola_mundo(request):
    # return HttpResponse(layout + "")
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):
    
    if redirigir == 1:
        return redirect('contacto', nombre="MArco", apellidos="AvaRia")
        
    # return HttpResponse(layout + """
    #     <h1>Página de mi web</h1>
    #     <p>Creado por Marco Avaria</p>
    # """)
    
    return render(request, 'pagina.html', {
        'texto': 'Texto de Marco Avaria',
        'lista': ['uno', 'dos', 'tres']
    })
    
def contacto(request, nombre = "", apellidos = ""):
    html = ""
    nombre = nombre.capitalize()
    apellidos = apellidos.capitalize()
    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}<h3>"
    
    return HttpResponse(layout + f"<h2>Contacto</h2>"+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public,
    )
    articulo.save()
    
    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulo(request):
    try:
        articulo = Article.objects.get(title="Superman", public=False)
        response = f"Artículo: <br/> {articulo.id} {articulo.title}"
    except:
        response = "<h1>Artículo no encontrado</h1>"
        
    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "Batman"
    articulo.content = "Película del 2017"
    articulo.public = True
    articulo.save()
    
    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):
    articulos = Article.objects.all()
    return render(request, 'articulos.html',{
        'articulos':articulos
    })