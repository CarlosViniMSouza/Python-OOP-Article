## Herdar de outras classes em Python

[Herança](https://realpython.com/inheritance-composition-python/) é o processo pelo qual uma classe assume os atributos e métodos de outra. As classes recém-formadas são chamadas de classes filhas e as classes das quais as classes filhas são derivadas são chamadas de classes pai.

As classes filhas podem substituir ou estender os atributos e métodos das classes pai. Em outras palavras, as classes filhas herdam todos os atributos e métodos do pai, mas também podem especificar atributos e métodos que são exclusivos para si.

Embora a analogia não seja perfeita, você pode pensar em herança de objetos como herança genética.

Você pode ter herdado a cor do cabelo de sua mãe. É um atributo com o qual você nasceu. Digamos que você decida pintar seu cabelo de roxo. Supondo que sua mãe não tenha cabelo roxo, você acabou de **substituir** o atributo de cor do cabelo que herdou de sua mãe.

Você também herda, em certo sentido, sua língua de seus pais. Se seus pais falam inglês, você também fala inglês. Agora imagine que você decida aprender uma segunda língua, como o alemão. Nesse caso, você **estendeu** seus atributos porque adicionou um atributo que seus pais não têm.


### Exemplo de parque para cães

Finja por um momento que você está em um parque para cães. Há muitos cães de diferentes raças no parque, todos engajados em vários comportamentos caninos.

Suponha agora que você queira modelar o parque de cães com classes Python. A classe `Dog` que você escreveu na seção anterior pode distinguir cães por nome e idade, mas não por raça.

Você pode modificar a classe Dog na janela do editor adicionando um atributo `.breed`:

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
```

Os métodos de instância definidos anteriormente são omitidos aqui porque não são importantes para esta discussão.

Pressione `F5` para salvar o arquivo. Agora você pode modelar o parque de cães instanciando vários cães diferentes na janela interativa:

```python
>>> miles = Dog("Miles", 4, "Jack Russell Terrier")

>>> buddy = Dog("Buddy", 9, "Dachshund")

>>> jack = Dog("Jack", 3, "Bulldog")

>>> jim = Dog("Jim", 5, "Bulldog")
```

Cada raça de cão tem comportamentos ligeiramente diferentes. Por exemplo, os buldogues têm um latido baixo que soa como `woof`, mas os dachshunds têm um latido mais agudo que soa mais como latido.

Usando apenas a classe `Dog`, você deve fornecer uma string para o argumento de som de `.speak()` toda vez que a chamar em uma instância de `Dog`:

```python shell
>>> buddy.speak("Yap")
'Buddy says Yap'

>>> jim.speak("Woof")
'Jim says Woof'

>>> jack.speak("Woof")
'Jack says Woof'
```

Passar uma string para cada chamada para `.speak()` é repetitivo e inconveniente. Além disso, a string que representa o som que cada instância de `Dog` faz deve ser determinada pelo seu atributo `.breed`, mas aqui você tem que passar manualmente a string correta para `.speak()` toda vez que ela for chamada.

Você pode simplificar a experiência de trabalhar com a classe `Dog` criando uma classe filha para cada raça de cachorro. Isso permite estender a funcionalidade que cada classe filha herda, incluindo a especificação de um argumento padrão para `.speak()`.
