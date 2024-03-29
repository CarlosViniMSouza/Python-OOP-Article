## Definir uma classe em Python

[Estruturas de dados](https://realpython.com/courses/python-data-types/) primitivas – como números, [strings](https://realpython.com/python-strings/) e listas – são projetadas para representar informações simples, como o custo de uma maçã, o nome de um poema ou suas cores favoritas, respectivamente. E se você quiser representar algo mais complexo?

Por exemplo, digamos que você queira acompanhar os funcionários de uma organização. Você precisa armazenar algumas informações básicas sobre cada funcionário, como nome, idade, cargo e ano em que começou a trabalhar.

Uma maneira de fazer isso é representar cada funcionário como uma [lista](https://realpython.com/python-lists-tuples/):

```python
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]
```

Há uma série de problemas com essa abordagem.

Primeiro, ele pode dificultar o gerenciamento de arquivos de código maiores. Se você fizer referência a `kirk[0]` várias linhas de distância de onde a lista kirk é declarada, você se lembrará de que o elemento com índice 0 é o nome do funcionário?

Em segundo lugar, pode introduzir erros se nem todos os funcionários tiverem o mesmo número de elementos na lista. Na lista `mccoy` acima, a idade está faltando, então `mccoy[1]` retornará `"Chief Medical Officer"` em vez da idade do Dr. McCoy.

Uma ótima maneira de tornar esse tipo de código mais gerenciável e mais fácil de manter é usar **classes**.

### Classes x instâncias

As classes são usadas para criar estruturas de dados definidas pelo usuário. As classes definem funções chamadas **métodos**, que identificam os comportamentos e ações que um objeto criado a partir da classe pode realizar com seus dados.

Neste tutorial, você criará uma classe Dog que armazena algumas informações sobre as características e comportamentos que um cão individual pode ter.

Uma classe é um modelo de como algo deve ser definido. Na verdade, não contém nenhum dado. A classe Dog especifica que um nome e uma idade são necessários para definir um cachorro, mas não contém o nome ou a idade de nenhum cachorro específico.

Enquanto a classe é o blueprint, uma **instância** é um objeto que é construído a partir de uma classe e contém dados reais. Uma instância da classe Dog não é mais um blueprint. É um cachorro de verdade com um nome, como Miles, que tem quatro anos.

Dito de outra forma, uma aula é como um formulário ou questionário. Uma instância é como um formulário que foi preenchido com informações. Assim como muitas pessoas podem preencher o mesmo formulário com suas próprias informações exclusivas, muitas instâncias podem ser criadas a partir de uma única classe.

### Como definir uma classe

Todas as definições de classe começam com a palavra-chave `class`, que é seguida pelo nome da classe e dois pontos. Qualquer código recuado abaixo da definição da classe é considerado parte do corpo da classe.

Aqui está um exemplo de uma classe `Dog`:

```python
class Dog:
    pass
```

O corpo da classe `Dog` consiste em uma única instrução: a palavra-chave `pass`. `pass` é frequentemente usado como um espaço reservado indicando para onde o código irá eventualmente. Ele permite que você execute esse código sem que o Python gere um erro.

A classe `Dog` não é muito interessante agora, então vamos aprimorá-la um pouco definindo algumas propriedades que todos os objetos `Dog` devem ter. Há uma série de propriedades que podemos escolher, incluindo nome, idade, cor da pelagem e raça. Para simplificar, usaremos apenas nome e idade.

As propriedades que todos os objetos `Dog` devem ter são definidas em um método chamado `.__init__()`. Toda vez que um novo objeto `Dog` é criado, `.__init__()` define o estado inicial do objeto atribuindo os valores das propriedades do objeto. Ou seja, `.__init__()` inicializa cada nova instância da classe.

Você pode dar `.__init__()` a qualquer número de parâmetros, mas o primeiro parâmetro sempre será uma [variável](https://realpython.com/python-variables/) chamada `self`. Quando uma nova instância de classe é criada, a instância é automaticamente passada para o parâmetro `sel`f em `.__init__()` para que novos atributos possam ser definidos no objeto.

Vamos atualizar a classe Dog com um método `.__init__()` que cria atributos `.name` e `.age`:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Observe que a assinatura do método `.__init__()` é recuada quatro espaços. O corpo do método é recuado por oito espaços. Este recuo é de vital importância. Ele diz ao Python que o método `.__init__()` pertence à classe Dog.

No corpo de `.__init__()`, existem duas instruções usando a variável self:

1. **`self.name`** = **`name`** cria um atributo chamado `name` e atribui a ele o valor do parâmetro `name`.

2. **`self.age`** = **`age`** cria um atributo chamado `age` e atribui a ele o valor do parâmetro `age`.

Os atributos criados em `.__init__()` são chamados de **atributos de instância**. O valor de um atributo de instância é específico para uma instância específica da classe. Todos os objetos `Dog` têm um nome e uma idade, mas os valores dos atributos `name` e `age` variam dependendo da instância `Dog`.

Por outro lado, **atributos de classe** são atributos que possuem o mesmo valor para todas as instâncias de classe. Você pode definir um atributo de classe atribuindo um valor a um nome de [variável](https://realpython.com/python-variables/) fora de `.__init__()`.

Por exemplo, a seguinte classe `Dog` tem um atributo de classe chamado `species` com o valor `"Canis familiaris"`:

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Os atributos de classe são definidos diretamente abaixo da primeira linha do nome da classe e são recuados por quatro espaços. Devem sempre ser atribuídos um valor inicial. Quando uma instância da classe é criada, os atributos de classe são criados automaticamente e atribuídos aos seus valores iniciais.

Use atributos de classe para definir propriedades que devem ter o mesmo valor para cada instância de classe. Use atributos de instância para propriedades que variam de uma instância para outra.

Agora que temos uma classe `Dog`, vamos criar alguns cachorros!