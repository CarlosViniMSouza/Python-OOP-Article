### Instanciar um objeto em Python

Abra a janela interativa do IDLE e digite o seguinte:

```python
>>> class Dog:
...     pass
```

Isso cria uma nova classe `Dog` sem atributos ou métodos.

Criar um novo objeto a partir de uma classe é chamado de `instanciar` um objeto. Você pode instanciar um novo objeto `Dog` digitando o nome da classe, seguido de abertura e fechamento de parênteses:

```python
>>> Dog()
# output: <__main__.Dog object at 0x106702d30>
```

Agora você tem um novo objeto `Dog` em `0x106702d30`. Essa sequência de letras e números de aparência engraçada é um `endereço de memória` que indica onde o objeto `Dog` está armazenado na memória do seu computador. Observe que o endereço que você vê na tela será diferente.

Agora instancie um segundo objeto `Dog`:

```python
>>> Dog()
# output: <__main__.Dog object at 0x0004ccc90>
```

A nova instância `Dog` está localizada em um endereço de memória diferente. Isso porque é uma instância totalmente nova e é completamente exclusiva do primeiro objeto `Dog` que você instancia.

Para ver isso de outra maneira, digite o seguinte:

```python
>>> a = Dog()
>>> b = Dog()
>>> a == b
# output: False
```

Nesse código, você cria dois novos objetos Dog e os atribui às variáveis ​​`a` e `b`. Quando você compara a e b usando o operador `==`, o resultado é `False`. Embora `a` e `b` sejam instâncias da classe `Dog`, eles representam dois objetos distintos na memória.

### Métodos de instância

**Métodos de instância** são funções que são definidas dentro de uma classe e só podem ser chamadas de uma instância dessa classe. Assim como `.__init__()`, o primeiro parâmetro de um método de instância é sempre `self`.

Abra uma nova janela do editor no IDLE e digite a seguinte classe `Dog`:

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
```

Esta classe Dog tem dois métodos de instância:

1. `.description()` retorna uma string exibindo o nome e a idade do cachorro.

2. `.speak()` tem um parâmetro chamado som e retorna uma string contendo o nome do cachorro e o som que o cachorro faz.

Salve a classe Dog modificada em um arquivo chamado `dog.py` e pressione `F5` para executar o programa.
Em seguida, abra a janela interativa e digite o seguinte para ver seus métodos de instância em ação:

```python shell
>>> miles = Dog("Miles", 4)

>>> miles.description()
'Miles is 4 years old'

>>> miles.speak("Woof Woof")
'Miles says Woof Woof'

>>> miles.speak("Bow Wow")
'Miles says Bow Wow'
```

Na classe Dog acima, `.description()` retorna uma string contendo informações sobre as `milhas` da instância `Dog`. Ao escrever suas próprias classes, é uma boa ideia ter um método que retorne uma string contendo informações úteis sobre uma instância da classe. No entanto, `.description()` não é a maneira mais [Pythonic](https://realpython.com/learning-paths/writing-pythonic-code/) de fazer isso.

Ao criar um objeto de `lista`, você pode usar `print()` para exibir uma string parecida com a lista:

```python shell
>>> names = ["Fletcher", "David", "Dan"]

>>> print(names)
['Fletcher', 'David', 'Dan']
```

Vamos ver o que acontece quando você `print()` o objeto miles:

```python shell
>>> print(miles)
# output: <__main__.Dog object at 0x00aeff70>
```

Quando você emite o `print(miles)`, você recebe uma mensagem enigmática informando que miles é um objeto `Dog` no endereço de memória `0x00aeff70`. Esta mensagem não é muito útil. Você pode alterar o que é impresso definindo um método de instância especial chamado `.__str__()`.

Na janela do editor, altere o nome do método `.description()` da classe `Dog` para `.__str__()`:

```python
class Dog:
    # Leave other parts of Dog class as-is

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"
```

Salve o arquivo e pressione `F5`. Agora, quando você `print(miles)`, obtém uma saída muito mais amigável:

```python shell
>>> miles = Dog("Miles", 4)

>>> print(miles)
'Miles is 4 years old'
```

Métodos como `.__init__()` e `.__str__()` são chamados de **métodos dunder** porque começam e terminam com sublinhados duplos. Existem muitos métodos dunder que você pode usar para personalizar classes em Python. Embora seja um tópico muito avançado para um livro iniciante em Python, entender os métodos dunder é uma parte importante do domínio de programação orientada a objetos em Python.

Na próxima seção, você verá como levar seu conhecimento um passo adiante e criar aulas a partir de outras aulas.
