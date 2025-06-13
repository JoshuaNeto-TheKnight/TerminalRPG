import disfunction
import random
TheDream = disfunction.light()
MAXHP, INIPWR, INIDEF = disfunction.powerdice()
name = disfunction.welcome()
MAXHP = disfunction.pathchoices(disfunction.thugencounter(MAXHP, INIPWR, INIDEF), disfunction.nestencounter())