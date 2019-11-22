# from django.core.files.base import ContentFile
# from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import action
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
#
#
# @action(methods=['POST'], detail=False)
#     def criar_pesquisa(self, request):
#         global status
#         data = request.data
#         fk_user = request.user.id
#
#         # if data['pesquisas']['situacao_ob'] == "Publicar":
#         #     status = True
#         # else:
#         #     status = False
#
#         try:
#             query_pesquisa = Pesquisa.objects.create(titulo=data['pesquisas']['titulo'],
#                                                      validade=data['pesquisas']['validade'][0:10],
#                                                      descricao=data['pesquisas']['descricao'], criador_id=fk_user,
#                                                      data_criacao=now,
#                                                      status_publi=status, tipo_pont=data['pesquisas']['pontuacao'])
#
#             if len(data['permissoes']) > 0:
#                 for regional in data['permissoes']:
#                     if regional['status']:
#                         ct = Regional.objects.get(nome=regional['nome'])
#                         query_pesquisa.permissoes_regional.add(ct)
#             else:
#                 ct = Regional.objects.get(nome__in=['Nacional', 'nacional', 'NACIONAL'])
#                 query_pesquisa.permissoes_regional.add(ct)
#
#             for categoria in data['filtros']:
#                 for filtro in categoria['filtros']:
#                     if filtro['status']:
#                         ct = Filtros.objects.get(valor=filtro['valor'])
#                         query_pesquisa.filtros_pdvs.add(ct)
#
#             query_pesquisa.save()
#
#             if data['pesquisas']['pontuacao'] == 'respostas':
#                 trataDadosRespostas(data, fk_user, query_pesquisa)
#             else:
#                 trataDadosPerguntas(data, fk_user, query_pesquisa)
#
#             return Response(status=HTTP_200_OK)
#
#         except Exception as error:
#             return Response(error, status=HTTP_500_INTERNAL_SERVER_ERROR)
#
#     @action(methods=['GET'], detail=False)
#     def obter_pesquisas(self, request):
#         data = []
#         permissoes = getRegionaisUsuario(request.user.id)
#         queryset = Pesquisa.objects.filter(permissoes_regional__in=permissoes).order_by('-data_criacao').distinct()
#         serializer = PesquisaSerializer(queryset, many=True).data
#
#         for pesquisa in serializer:
#             filtros_pre_selecionados = []
#             regionais_pre_selecionados = []
#
#             for ps in pesquisa['filtros_pdvs']:
#                 filtros_pre_selecionados.append(ps['id'])
#
#             for regional in pesquisa['permissoes_regional']:
#                 regionais_pre_selecionados.append(regional['id'])
#
#             filtros = categoriaFiltro.objects.filter(is_active=True)
#             serializer2 = categoriaFiltro2Serializer(filtros, many=True).data
#
#             filters = retornaListaFiltros(filtros_pre_selecionados, serializer2)
#             lista_regionais = retornaListaRegionais(regionais_pre_selecionados)
#
#             response = {
#                 'id': pesquisa['id'],
#                 'titulo': pesquisa['titulo'],
#                 'descricao': pesquisa['descricao'],
#                 'data_criacao': pesquisa['data_criacao'],
#                 'data_expiracao': pesquisa['validade'],
#                 'publicado': pesquisa['status_publi'],
#                 'pontuacao': pesquisa['pontuacao'],
#                 'tipo_pontuacao': pesquisa['tipo_pont'],
#                 'filtros': filters,
#                 'regionais': lista_regionais
#             }
#
#             data.append(response)
#
#         return Response(data, status=HTTP_200_OK)