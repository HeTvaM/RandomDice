from Stuff.abstract import Entity

class Base(Entity):
    def __init__(
        self,
        hp, speed, armor
    ):
        super().__init__(
            hp, speed, armor
        )

    def do_ability(self): pass
