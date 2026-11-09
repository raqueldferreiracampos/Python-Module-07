from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import TransformCapability, HealCapability
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class InvalidStrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature) is False:
            raise InvalidStrategyError("Invalid Creature "
                                       f"'{creature._c_name}'"
                                       " for this aggressive strategy"
                                       )
        else:
            print(cast(TransformCapability, creature).transform())
            print(creature.attack())
            print(cast(TransformCapability, creature).revert())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid is False:
            raise InvalidStrategyError("Invalid Creature "
                                       f"'{creature._c_name}'"
                                       " for this defensive strategy"
                                       )
        else:
            print(creature.attack())
            print(cast(HealCapability, creature).heal())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
