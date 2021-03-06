import random

from west_world.locations import Locations


class State(object):

    def enter(self, entity):
        raise NotImplementedError

    def execute(self, entity):
        raise NotImplementedError

    def exit(self, entity):
        raise NotImplementedError


# Miner states
class EnterMineAndDigForNugget(State):
    def enter(self, entity):
        if entity.location is not Locations.GOLDMINE:
            print("Walking to the goldmine")
            entity.location = Locations.GOLDMINE

    def execute(self, entity):
        # Increase the gold
        entity.increase_gold_carried(1)

        # Digging is hard work
        entity.increase_fatigue()

        print('Picking up  a nugget')

        if entity.pockets_full():
            entity.change_state(VisitBankAndDepositGold())

        if entity.is_thirsty():
            entity.change_state(QuenchThirst())

    def exit(self, entity):
        print('I am leaving the gold mine with mah pockets full o sweet gold')


class GoHomeAndSleepTilRested(State):
    def enter(self, entity):
        if entity.location is not Locations.SHACK:
            print('Walking home')
            entity.change_location(Locations.SHACK)

    def execute(self, entity):
        if entity is not entity.is_fatigue():
            print('What a darn fantastic nap! Time to find more gold')
            entity.change_state(EnterMineAndDigForNugget())
        else:
            entity.descrease_fatigue()
            print('ZZZZ....')

    def exit(self, entity):
        print('Leaving the house')


class QuenchThirst(State):
    def enter(self, entity):
        if entity.location is not Locations.SALOON:
            print('Boy, ah sure is thirsty! Walking to the saloon')
            entity.change_location(Locations.SALOON)

    def execute(self, entity):
        if entity.is_thirsty():
            entity.buy_and_drink_whiskey()
            print("That's mighty fine sipping liqueur")
            entity.change_state(EnterMineAndDigForNugget())

    def exit(self, entity):
        print('Leaving the saloon, feeling good')


class VisitBankAndDepositGold(State):
    def enter(self, entity):
        if entity.location is not Locations.BANK:
            print('Going to the bank. Yes siree')
            entity.change_location(Locations.BANK)

    def execute(self, entity):
        entity.add_to_wealth(entity.gold_carried)

        entity.set_gold_carried(0)

        print('Depositing gold. Total savings now: {}'.format(entity.wealth))

        if entity.wealth >= entity.COMFORT_LEVEL:
            print('WooHoo! Rich enough for now. Back home to mah lille lady')
            entity.change_state(GoHomeAndSleepTilRested())
        else:
            entity.change_state(EnterMineAndDigForNugget())

    def exit(self, entity):
        print('Leaving the bank')


# Wife states
class WifeGlobalState(State):
    def enter(self, entity):
        return

    def execute(self, entity):
        if random.randint(0, 10) == 3 and entity.current_state is not VisitTheBathroom():
            entity.change_state(VisitTheBathroom())

    def exit(self, entity):
        return


class DoHouseWork(State):
    def enter(self, entity):
        print('Time to do some housework')

    def execute(self, entity):

        if not entity.is_stressed():
            case = random.randint(0, 2)
            if case == 0:
                print('Mopping the flor')
                return

            if case == 1:
                print('Washing the dishes')
                return

            if case == 2:
                print('Making the bed')
                return
        else:
            entity.change_state(VisitTheBathroom())

    def exit(self, entity):
        return


class VisitTheBathroom(State):
    def enter(self, entity):
        print('Walking to the can. Need to powda my pretty little nose')

    def execute(self, entity):
        print('Ahhhhhh! sweet relief')
        entity.change_state(DoHouseWork())

    def exit(self, entity):
        print('Leaving the Jon')


class CookStew(State):
    def enter(self, entity):
        if not entity.is_cooking:
            print('Putting the stew in the oven')
            entity.set_is_cooking(True)

    def execute(self, entity):
        print('Fussing over the food')

    def exit(self, entity):
        print('Putting the stew on the table')
