from code04_inherit_classes import Dog


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass
