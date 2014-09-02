import rg
import random

class Robot:
    def act(self, game):
        available = rg.locs_around(self.location, filter_out = ('invalid','obstacle'))

        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    if self.hp <= 10:
                        if len(available) == 0
                            return ['suicide']
                        return ['move', random.choice(available)]
                    return ['attack', loc]

        # move toward the center
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]