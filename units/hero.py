import base_unit
import sys
class Hero(base_unit.BaseUnit):
    def __init__(self, lvl):
        self.lvl = lvl
        self.max_health = 100
        self.attack_power = 25
        self.health = 100

    def rest():
        if health < max_health and health + max_health/10 < max_health:
            health += max_health/10

    def heroPosition(self):
        x=0
        y=0
        for i in self.lvl.map:
            if 'H' in i:
                y=i.index('H')
                break
            else:
                x+=1
        return [x,y]

    def feel(self,dir):
            position=self.heroPosition()
            try:
                if(dir=='left'):
                    return self.lvl.map[position[0]][position[1]-1]
                elif dir=='right':
                    return self.lvl.map[position[0]][position[1]+1]
                elif dir=='up':
                    return self.lvl.map[position[0]-1][position[1]]
                elif dir=='down':
                    return self.lvl.map[position[0]+1][position[1]]
            except IndexError:
                print "There is no escape!"
                sys.exit()

    def move(self,dir):
            position=self.heroPosition()
            try:
                if self.feel(dir) ==' ':
                    self.lvl.map[position[0]][position[1]]=' '
                    if(dir=='left'):
                        self.lvl.map[position[0]][position[1]-1]='H'
                    elif dir=='right':
                        self.lvl.map[position[0]][position[1]+1]='H'
                    elif dir=='up':
                        self.lvl.map[position[0]][1,position[1]]='H'
                    elif dir=='down':
                        self.lvl.map[position[0]][1,position[1]]='H'
            except IndexError:
                print "There is no escape!"
                sys.exit()
    def rope(self):
        position=self.heroPosition()
            if position[0]<(len(self.lvl.map[0]-1) and position[1]<len(self.lvl.map[1]-1):
                    self.lvl.map[position[0]][position[1]+1] or 
            print "LEVEL COMPLETE!"
            sys.exit()
