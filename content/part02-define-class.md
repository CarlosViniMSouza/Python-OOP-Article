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
