import requests
import json

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

data = {
    "model": "llama3.1",
    "prompt": "Olá, será que me consegues ler o seguinte documento , analisá-lo e de certa forma resumir todo o contexto mais importante apenas por favor."
    "1. O Crime - 22 de Novembro de 1963 Chegada a Dallas Kennedy estava em campanha para sua reeleição e visitava o Texas para unir facções políticas do Partido Democrata. A carreata incluía um conversível Lincoln Continental SS-100-X, no qual estavam: Kennedy e sua esposa, Jacqueline Governador do Texas, John Connally, e sua esposa, Nellie Connally Motorista William Greer e agente do Serviço Secreto Roy Kellerman A Emboscada na Dealey Plaza O trajeto passava por ruas estreitas e curvas em baixíssima velocidade (cerca de 18 km/h). "
    "Às 12h30, tiros foram disparados quando o carro passou pelo Depósito de Livros Escolares do Texas. Os disparos (de acordo com a versão oficial): O primeiro tiro provavelmente errou ou atingiu um local não identificado. O segundo tiro acertou Kennedy no pescoço e Connally no peito, pulso e coxa (Teoria da Bala Mágica). O terceiro tiro atingiu a cabeça de Kennedy, causando ferimentos fatais. O carro acelerou imediatamente em direção ao Hospital Parkland, mas Kennedy foi declarado morto às 13h00. 2. A Captura e Assassinato de Oswald Fuga e "
    "Prisão Minutos após o crime, Lee Harvey Oswald, que trabalhava no prédio de onde partiram os disparos, deixou o local. Ele foi visto por um policial dentro do prédio cerca de 90 segundos após os tiros. Pegou um ônibus, depois um táxi e foi até sua pensão. Às 13h15, um policial chamado J.D. Tippit foi morto a tiros em Oak Cliff, bairro de Dallas. Pouco depois, Oswald foi encontrado escondido em um cinema e preso às 13h50. O Assassinato de Oswald No dia 24 de novembro, enquanto era transferido para a cadeia do condado, Jack Ruby, dono de uma "
    "boate em Dallas, atirou em Oswald ao vivo na TV. Ruby alegou que queria poupar Jackie Kennedy do trauma de um julgamento. Ele foi condenado à morte, mas morreu de câncer antes de um novo julgamento. 3. Investigação Oficial - Comissão Warren (1964) O presidente Lyndon B. Johnson nomeou a Comissão Warren, presidida pelo chefe da Suprema Corte, Earl Warren, para investigar o caso. Principais Conclusões Oswald agiu sozinho e disparou três tiros do sexto andar do Depósito de Livros. A Teoria da Bala Mágica explica os ferimentos de Kennedy e "
    "Connally com um único projétil. Jack Ruby também agiu sozinho ao matar Oswald. Críticas à Comissão Testemunhas não foram ouvidas de forma adequada. Erros na reconstituição dos disparos. O governo queria encerrar o caso rapidamente para evitar teorias conspiratórias. 4. Comitê da Câmara sobre Assassinatos (1976-1979) Novas análises acústicas indicaram um possível quarto tiro, sugerindo a presença de um segundo atirador. Conclusão: Alta probabilidade de conspiração, mas sem prova concreta de quem estaria envolvido.",
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))
    
data = json.loads(response.text)
resposta = data["response"]
print(resposta)