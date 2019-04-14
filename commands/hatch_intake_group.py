from wpilib.command.commandgroup import CommandGroup

from commands.put_panel import PutPanel
from commands.move_elevator import MoveElevator
from commands.take_panel import TakePanel

from constants import Constants


class HatchIntakeG(CommandGroup):

    def __init__(self):
        super().__init__()
        self.addSequential(PutPanel(), 0.5)
        self.addSequential(MoveElevator(18))
        self.addSequential(TakePanel(), 0.5)
        self.addSequential(MoveElevator(Constants.LOWEST_ENABLED_ELEVATOR_POS))
