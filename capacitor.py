from ex0 import CreatureFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from typing import cast
from ex1.capability import HealCapability, TransformCapability


def testing_healing_factory(healing_factory: CreatureFactory) -> None:
    basic = healing_factory.create_base()
    evolved = healing_factory.create_evolved()
    print("Testing Creature with healing capability")
    print("base:")
    print(basic.describe())
    print(basic.attack())
    print(cast(HealCapability, basic).heal())
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(cast(HealCapability, evolved).heal())


def testing_transformed_factory(transform_factory: CreatureFactory) -> None:
    basic = transform_factory.create_base()
    evolved = transform_factory.create_evolved()
    print("Testing Creature with transform capability")
    print("base:")
    print(basic.describe())
    print(basic.attack())
    print(cast(TransformCapability, basic).transform())
    print(basic.attack())
    print(cast(TransformCapability, basic).revert())
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(cast(TransformCapability, evolved).transform())
    print(evolved.attack())
    print(cast(TransformCapability, evolved).revert())


def main() -> None:
    testing_healing_factory(HealingCreatureFactory())
    print()
    testing_transformed_factory(TransformCreatureFactory())


if __name__ == "__main__":
    main()
