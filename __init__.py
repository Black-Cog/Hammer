

###############
# import master modules
###############

import ui
import core


###############
# Binding at root level of Hammer
###############

from core.HammerActions import getActions
from core.HammerActions import Database

getEntity = Database().getEntity
