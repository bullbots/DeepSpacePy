from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from commands.move_elevator import MoveElevator
from commands.inhale_exhale import InhaleExhale
from subsystems.intake_output import IntakeOutput
from constants import Constants

from commands.command_logging_decorator import logging_command


@logging_command
class PlaceBallG(CommandGroup):

    def __init__(self, desiredPos):
        super().__init__()
        self.addSequential(MoveElevator(desiredPos))
        self.addSequential(InhaleExhale(IntakeOutput.CargeGiveOrTake.GIVE))
        self.addSequential(WaitCommand(1))
        self.addSequential(InhaleExhale(IntakeOutput.CargeGiveOrTake.GIVE))
        self.addSequential(MoveElevator(Constants.LOWEST_ENABLED_ELEVATOR_POS))
