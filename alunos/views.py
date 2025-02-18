from rest_framework.viewsets import ModelViewSet
from .models import Estado, Aluno, Cidade
from .serializers import EstadoSerializer, AlunoSerializer, CidadeSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    
class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class =  CidadeSerializer