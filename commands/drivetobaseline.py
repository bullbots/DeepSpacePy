from wpilib.command import CommandGroup, WaitCommand

from commands.command_logging_decorator import logging_command


from commands.move import Move


@logging_command
class DriveToBaseLine(CommandGroup):

    def __init__(self):
        super().__init__()
        self.addSequential(Move(0.5), 2.0)


@logging_command
class DelayedDriveToBaseLine(CommandGroup):

    def __init__(self):
        super().__init__()
        self.addSequential(WaitCommand(3.0))
        self.addSequential(DriveToBaseLine())
