from wpilib.command import CommandGroup, WaitCommand

from commands.move import Move


class DriveToBaseLine(CommandGroup):

    def __init__(self):
        super().__init__()
        self.addSequential(Move(0.5), 2.0)


class DelayedDriveToBaseLine(CommandGroup):

    def __init__(self):
        super().__init__()
        self.addSequential(WaitCommand(3.0))
        self.addSequential(DriveToBaseLine())
