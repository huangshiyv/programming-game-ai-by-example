from west_world.miner import Miner
from west_world.locations import Locations
from west_world.state import EnterMineAndDigForNugget


def main():
    miner = Miner(current_state=EnterMineAndDigForNugget(), location=Locations.SHACK)
    for i in range(0, 20):
        miner.update()


if __name__ == '__main__':
    main()
