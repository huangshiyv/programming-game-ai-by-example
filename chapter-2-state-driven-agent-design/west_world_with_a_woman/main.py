from locations import Locations
from miner import Miner
from state import EnterMineAndDigForNugget, DoHouseWork
from wife import Wife


def main():
    miner = Miner(current_state=EnterMineAndDigForNugget(), location=Locations.SHACK)
    wife = Wife(current_state=DoHouseWork(), location=Locations.SHACK)
    for i in range(0, 20):
        miner.update()
        wife.update()


if __name__ == '__main__':
    main()
