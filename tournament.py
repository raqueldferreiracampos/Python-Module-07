from ex2.strategy import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy, InvalidStrategyError
from ex0.factory import AquaFactory, CreatureFactory, FlameFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


opponents = [(FlameFactory(), NormalStrategy()),
             (HealingCreatureFactory(), DefensiveStrategy())]


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_1, strategy_1 = opponents[i]
                factory_2, strategy_2 = opponents[j]
                creature_1 = factory_1.create_base()
                creature_2 = factory_2.create_base()
                print()
                print("* Battle *")
                print(creature_1.describe())
                print("vs")
                print(creature_2.describe())
                print("now fight!")
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)

    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    normal = NormalStrategy()
    agressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(FlameFactory(), normal),
            (HealingCreatureFactory(), defensive)])
    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(FlameFactory(), agressive),
            (HealingCreatureFactory(), defensive)])
    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(AquaFactory(), normal),
            (HealingCreatureFactory(), defensive),
            (TransformCreatureFactory(), agressive)])


if __name__ == "__main__":
    main()
