from wpilib.command.commandgroup import CommandGroup

from commands.raise_lift_elevator import RaiseLiftElevator
from commands.one_climb_group import OneClimbG


class TwoClimbG(CommandGroup):

    def __init__(self):
        super().__init__()
        self.addSequential(RaiseLiftElevator(-27, -19.5), 3)
        self.addSequential(OneClimbG(2 * -27, 2 * -19.5))
