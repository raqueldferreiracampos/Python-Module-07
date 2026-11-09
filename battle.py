from ex0 import FlameFactory, AquaFactory, CreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    basic = factory.create_base()
    print(basic.describe())
    print(basic.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def testing_battle(factory_1: CreatureFactory,
                   factory_2: CreatureFactory) -> None:
    creature_1 = factory_1.create_base()
    creature_2 = factory_2.create_base()
    print(creature_1.describe())
    print("vs")
    print(creature_2.describe())
    print("fight!")
    print(creature_1.attack())
    print(creature_2.attack())


def main() -> None:
    print("Testing factory")
    testing_factory(FlameFactory())
    print()
    print("Testing factory")
    testing_factory(AquaFactory())
    print()
    print("Testing battle")
    testing_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
