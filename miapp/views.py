from django.shortcuts import render, HttpResponse, redirect

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
    
    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul> 
    """
    year = 2024
    while year <= 2050: 
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year +=1
        
    html += "</ul"
    
    # return HttpResponse(layout + html)
    return render(request, 'index.html')

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
    return render(request, 'pagina.html')
    
def contacto(request, nombre = "", apellidos = ""):
    html = ""
    nombre = nombre.capitalize()
    apellidos = apellidos.capitalize()
    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}<h3>"
    
    return HttpResponse(layout + f"<h2>Contacto</h2>"+html)