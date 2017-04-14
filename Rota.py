#enjoy
def rota(cep1, cep2):
    url1 = 'https://viacep.com.br/ws/' + cep1 + '/json/'
    url2 = 'https://viacep.com.br/ws/' + cep2 + '/json/'
    origem = json.loads(requests.get(url1).text)
    destino = json.loads(requests.get(url2).text)
    strOrigem = origem['localidade'] + ' ' + origem['uf']
    strOrigem = strOrigem.replace(' ', '+')
    strDestino = destino['localidade'] + ' ' + destino['uf']
    strDestino = strDestino.replace(' ', '+')
    return requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='
                     +strOrigem+'&destinations='+strDestino)    #adicione o campo &key= ao final, com a sua chave de api distancematrix,
                                                                #obtida gratuitamente no seu site oficial caso use fora do ambiente de testes
                                                                
                                                                
#Exemplo de chamada
resultado = rota('65066210', '65320000')
print(resultado.text)
