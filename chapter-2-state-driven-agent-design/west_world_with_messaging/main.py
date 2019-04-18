from locations import Locations
from miner import Miner
from state import EnterMineAndDigForNugget, DoHouseWork
from wife import Wife


def main():
    miner = Miner(current_state=EnterMineAndDigForNugget(), location=Locations.SHACK)
    wife = Wife(current_state=DoHouseWork(), location=Locations.SHACK)

    miner.other_entity = wife
    wife.other_entity = miner

    for i in range(0, 30):
        miner.update()
        wife.update()


if __name__ == '__main__':
    main()
