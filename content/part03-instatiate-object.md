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
