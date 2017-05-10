# Buscando-distancia-por-cep-em-Python
consumindo APIs e trabalhando com tratamento dos retornos em json.

Consulta as APIs gratuitas:
* Correios http://viacep.com.br/

* Distance Matrix https://developers.google.com/maps/documentation/distance-matrix/start?hl=pt-br

Recebe os dados da viacep destes locais e concatena os campos relevantes em duas strings ***origem*** e ***destino***, usando-as por fim como segmentos do recurso da api distance matrix para retorno das milhas, distancia em km e tempo médio de viagem de um local ao outro.

#### exemplo de chamada:

minhaRota = rota(cep1, cep2)

print(minhaRota.text) **JSON, padrão de retorno de APIs RESTful**.


