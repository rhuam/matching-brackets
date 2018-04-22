# Matching Brackets
Problema de balanceamento de parêntese, chaves e colchetes

## O Problema
Um _Brackets_ pode ser qualquer um dos seguintes caracteres: (, ), [, ], {, }.
E um _Par de Brackets_, as seguintes combinações: (), [], {}.

Uma entrada qualquer estará balanceada se um _Par de Brackets_ externo conter apenas _Par de Brackets_ em seu interior ou estiver vazio.

Desta forma, são exemplo de _Par de Brackets_ balanceados:
- {\[()]}
- ()\[]{}
- ((){})\[]

E exemplos de pares não balanceados:
- {[(]}
- (][]{}
- )\[]{}

## Proposta de Solução
Existem diversas maneiras de resolver esse problema, seja de forma interativa ou recursiva.
Para esse experimento, utilizei duas formas. Uma teste inicial, que procura por erros, sem precisar verificar o balanceamento de _Brackets_, consequentemente, de menor custo e com a recuperação do ponto exato do erro.
E um segundo método, que verifica o balanceamento par a par, que possui um custo maior e não especifica a posição do erro.

### Materiais
Para desenvolver essa solução foi usado a linguagem de programação Python e o framework Django.
Os testes foram feitos em uma instância virtual do Cloud9: [Clonar](https://c9.io/rhuam/matching-brackets) | [Testar](https://django-rhuam.c9users.io)

# Histórico
## Solução do problema
Primeiramente foram desenvolvidos os método em python para solucionar o problema. Por se tratar de manipulação de Strings, foi necessário recorrer a [Documentação do Python](https://docs.python.org/3.5/library/stdtypes.html?highlight=find#str.find), principalmente a seção de substituição e busca de substrings.
Foram desenvolvidos três métodos na _Classe_ [Processor](matching_brackets/brackets/processor.py), descritas detalhadamente abaixo.

### String: findErro()
O método findErro, faz buscas por 3 tipos de erros:
- Entradas iniciadas com _Brackets_ de fechamento: ), ], }.
- Entradas finalizando com _Brackets_ de abertura: (, \[, {.
- _Par de Brackets_ inválidos: ( ], ( }, \[ ), \[ }, { ), { ].

Ao encontrar qualquer um desses erros, o método finaliza a busca enviando para o método viewText() o número do índice onde encontra-se o erro. Caso contrário, chama-se o método replaceAll() para fazer uma busca completa.

### String: replaceAll()
Este método interativo remove a cada interação todos _Par de Brackets_ mais internos, até o momento que a string estiver vazia, e nesse caso, a entrada é balanceada, ou o loop não efetuar mudança nenhuma na string, caracterizando uma entrada desbalanceada.
Em ambos os casos, os índices são enviados para o método viewText(), porém no caso de string balanceada o índice enviado é -1.

### String: viewText(int i)
Essa função recebe um índice o qual há um elementos que provoca o erro de balanceamento. Os valores de índice recebidos podem ser:
- _i_ = -1: Entrada balanceada, retorna um código HTML com a entrada na cor verde e mensagem.
- 0 <= _i_ < _tamanho da string_: É a posição da string que contém o erro, retorna um código HTML com o carácter errado em vermelho e uma mensagem de erro.
- _i_ = _tamanho da string_: Quando não é possível determinar o local do erro, retorna um código HTML com toda a entrada em vermelho.

## Uso do Django
Após a conclusão do problema, foi analisada a possibilidade de criação de uma interface web para realizar os testes e entregar o projeto com melhor qualidade. Para isso, optei pelo Django.
O primeiro contato com Django foi através do vídeo [Aprenda Djando em 30 min](https://www.youtube.com/watch?v=zvyxQ5COwDI), por possuir uma estrutura semelhante ao Laravel (Framework que já tenho certo conhecimento), o desenvolvimento se mostrou tranquilo, vez ou outra um busca na [Documentação do Django](https://docs.djangoproject.com/pt-br/2.0) sobre formulários e views.
No Django, foram criados 5 arquivos para realizar todas as tarefas e exibir o formulário de consulta.

- [urls.py](matching_brackets/brackets/urls.py): Esse arquivo foi incluído no arquivo principal de URL do Django _(matching_brackets/urls.py)_ para organizar os endereços da aplicação em um único arquivo.
- [model.py](matching_brackets/brackets/model.py): Aqui onde são descritos o modelos da aplicação, nesse caso, apenas um, o modelo Query, com um único atributo, uma string de até 1000 caracteres.
- [forms.py](matching_brackets/brackets/forms.py): Nesse arquivo é definido o formulário que será exibido para o usuário, seus campos e características, além disso, o método **is_valid()** resposável por verificar se a entrada não contém nenhum caracter inválido para a aplicação.
- [views.py](matching_brackets/brackets/views.py): Possui a lógica de exibição das view, onde verifica-se se a entrada foi solicitada via GET ou POST, envia a entrada para processamento, e retorna com o resultado para renderizar a página para o usuário.
- [index.html](matching_brackets/brackets/templates/index.html): Contém a estrutura HTML básica da página, as referências para o bootstrap, e alguns comandos de seleção, para exibir ou ocultar elementos dados os valores recebidos pela view.

# Conclusão
O problema de balanceamento do Brackets em si, é relativamente fácil, e se torna interessante a medida que tentamos diminuir sua complexidade, uso de estruturas de dados como vetores e listas ou até mesmo recursão, são possibilidades de soluções eficientes. O grande aprendizado nesse experimento foi o framwork Django, e a possibilidade de criar uma estrutura web toda em menos de 24 horas, mesmo sem nenhum conhecimento.
