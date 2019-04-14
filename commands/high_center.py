from wpilib.command.commandgroup import CommandGroup

from commands.move_lift import MoveLift
from commands.lift_drive import LiftDrive


class HighCenter(CommandGroup):

    def __init__(self):
        super().__init__()
        self.addSequential(MoveLift(-2))
        self.addSequential(LiftDrive(-1), 2.0)
        self.addSequential(MoveLift(1))
