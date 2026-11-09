from .capability import HealCapability, TransformCapability
from ex0 import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if self._transform is True:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self) -> str:
        self._transform = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self._transform is True:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self) -> str:
        self._transform = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        return "Morphagon stabilizes its form."
