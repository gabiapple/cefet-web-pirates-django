from django.shortcuts import render
from django.views import View
from django.db.models import F, ExpressionWrapper, DecimalField, Sum
from pirates.models import Tesouro


class ListaTesourosView(View):
	def get(self, request):
		queryset = Tesouro.objects.annotate(valor_total=ExpressionWrapper(F('preco')*F('quantidade'), \
				output_field=DecimalField(
				decimal_places=2,
				blank=True)
				)\
		)
		lista_tesouros = list(queryset)
		total = queryset.aggregate(total=Sum('valor_total'))['total']
		data = {
			'lista_tesouros': lista_tesouros,
			'total': total
		}

		return render(request, 'lista_tesouros.html', data)