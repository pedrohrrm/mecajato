from django.shortcuts import render, get_object_or_404
from .forms import FormServico
from django.http import HttpResponse, FileResponse
from .models import Servico
# ServicoAdicional
from fpdf import FPDF
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

@login_required
def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Salvo com sucesso')
        else:
            return render(request, 'novo_servico.html', {'form': form})

@login_required
def listar_servico(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        return render(request, 'listar_servico.html', {'servicos': servicos})
    
@login_required
def servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    return render(request, 'servico.html', {'servico': servico})

@login_required
def gerar_os(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)

    pdf.set_fill_color(240,240,240)
    pdf.cell(35, 10, 'Cliente:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.cliente.nome}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Serviço:', 1, 0, 'L', 1)

    categorias_manutencao = servico.categoria_manutencao.all()
    for i, manutencao in enumerate(categorias_manutencao):
        pdf.cell(0, 10, f'- {manutencao.get_titulo_display()}', 1, 1, 'L', 1)
        if not i == len(categorias_manutencao) -1:
            pdf.cell(35, 10, '', 0, 0)

    pdf.cell(35, 10, 'Data de início:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_inicio}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Data de entrega:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_entrega}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Protocolo:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.protocole}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Total:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.preco_total()}', 1, 1, 'L', 1)
    
    pdf_content = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_content)
   
    return FileResponse(pdf_bytes, as_attachment=True, filename=f"os-{servico.protocole}.pdf")


def calendario(request):
    return render(request, 'calendar.html')

def servicos_json(request):
    servicos = Servico.objects.all()
    eventos = []
    for servico in servicos:
        eventos.append({
            'title': servico.titulo,
            'start': f"{servico.data_inicio}T{servico.horario}",  # Formato ISO 8601
            'end': f"{servico.data_entrega}T{servico.horario}" if servico.data_entrega else None,
        })
    return JsonResponse(eventos, safe=False)
# def servico_adicional(request):
#     identificador_servico = request.POST.get('identificador_servico')
#     titulo = request.POST.get('titulo')
#     descricao = request.POST.get('descricao')
#     preco = request.POST.get('preco')

#     servico_adicional = ServicoAdicional(titulo=titulo,
#                                         descricao=descricao,
#                                         preco=preco)
    
#     servico_adicional.save()

#     servico = Servico.objects.get(identificador=identificador_servico)
#     servico.servicos_adicionais.add(servico_adicional)
#     servico.save()

#     return HttpResponse("Salvo")