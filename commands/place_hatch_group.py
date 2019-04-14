from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from commands.move_elevator import MoveElevator
from commands.put_panel import PutPanel
from commands.take_panel import TakePanel
from constants import Constants


class PlaceHatchG(CommandGroup):

    def __init__(self, desiredPos):
        super().__init__()
        self.addSequential(MoveElevator(desiredPos))
        self.addSequential(PutPanel(), 0.4)
        self.addSequential(MoveElevator(desiredPos))
        self.addSequential(WaitCommand(0.35))
        self.addSequential(TakePanel(), 0)
        self.addSequential(MoveElevator(Constants.LOWEST_ENABLED_ELEVATOR_POS))
