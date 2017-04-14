# Buscando-distancia-por-cep-em-Python
consumindo APIs e trabalhando com tratamento dos retornos em json
Consulta a API de correios http://viacep.com.br/
E a api distance matrix https://developers.google.com/maps/documentation/distance-matrix/start?hl=pt-br
Recebe os dados da viacep destes locais e concatena os campos relevantes em duas strings origem e destino, usando-as por fim como segmentos do recurso da api distance matrix para retorno das milhas, distancia em km e tempo médio de viagem de um local ao outro.
