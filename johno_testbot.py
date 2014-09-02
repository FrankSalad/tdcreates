import rg

class Robot:
    def act(self, game):
        available = rg.locs_around(self.location, filter_out = ('invalid', 'obstacle'))
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player:
                if rg.dist(loc, self.location) == 1:
                    return ['attack', loc]
                elif rg.dist(loc, self.location) <= 3:
                    return ['move', rg.toward(self.location, loc)]
                else:
                    return ['move', rg.toward(self.location, rg.CENTER_POINT)]
