"""
our heuristic value is calculated based on the AC type
e.g if the home is aleady using the heat pump we will give them higher heuristic value
if we do not know what type of heating a certain household is using we will look at the
year was built and assign heuristic value based on that. e.g. older home will have lower
heuristc value because it's more likely that the older built home still uses boiler system

OF HOME HAS HITPUMP = 100
IF BOILER = 10
IF IT'S BUILT BEFORE 2000 = 30
"""


def heuristic(node):
    node.getData