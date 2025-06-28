tf_prompt = """
Você é uma LLM com o propósito de gerar uma questão baseado no conteúdo abaixo para estudantes universitários, essa questão é uma questão de verdadeiro ou falso onde há uma afirmação e ela ou possui alguma irregularidade a fazendo falsa ou ela é correta lhe fazendo verdadeira. Essa afirmação não pode ser ambígua ou opinativa ela deve poder ser afirmada ou negada com certeza por alguém com conhecimento o suficente, Sua resposta deve seguir estritamente a formatação solicitada e deve ser em língua portuguesa. Na resposta não pode haver nada além do conteúdo formatado e a formatação deve seguir o exemplo de formatação sem desvios. Conteúdo não faz parte da formatação sendo apenas uma informação do que a questão será sobre partindo das informações da descrição dos assuntos de uma aula.

Pergunta: <pergunta>
Resposta correta: verdadeiro/falso


Conteúdo:
{{$content}}
"""

mcq_prompt = """
Você é uma LLM com o propósito de gerar uma questão baseado no conteúdo abaixo para estudantes universitários, essa questão é uma questão de múltipla escolha com 4 alternativas (A, B, C, D). Apenas uma deve ser correta. Sua resposta deve seguir estritamente a formatação solicitada e deve ser em língua portuguesa. Na resposta não pode haver nada além do conteúdo formatado e a formatação deve seguir o exemplo de formatação sem desvios. Conteúdo não faz parte da formatação sendo apenas uma informação do que a questão será sobre partindo das informações da descrição dos assuntos de uma aula.

Formato:
Pergunta: <pergunta>
A) <opção A>
B) <opção B>
C) <opção C>
D) <opção D>
Resposta correta: A/B/C/D

Conteúdo:
{{$content}}
"""
matching_prompt = """
Você é uma LLM com o propósito de gerar uma questão baseado no conteúdo abaixo para estudantes universitários, essa questão é uma questão de associação de 3 pares correspondente logicamente em um determinado contexto, como por exemplo Java e JDK em um contexto de linguagens e seus compiladores. todos os elementos devem ter um e apenas um elemento complementar e um elemento não pode ser complementar a mais de um elemento, Sua resposta deve seguir estritamente a formatação solicitada e deve ser em língua portuguesa. Na resposta não pode haver nada além do conteúdo formatado e a formatação deve seguir o exemplo de formatação sem desvios. Conteúdo não faz parte da formatação sendo apenas uma informação do que a questão será sobre partindo das informações da descrição dos assuntos de uma aula.

Pergunta: <pergunta>
1. <item esquerda> - <item direita>
2. <item esquerda> - <item direita>
3. <item esquerda> - <item direita>

Conteúdo:
{{$content}}
"""