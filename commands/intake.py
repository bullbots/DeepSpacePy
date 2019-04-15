from wpilib.command.conditionalcommand import ConditionalCommand
from wpilib.command.command import Command

from commands.ball_intake_group import BallIntakeG
from commands.move_hatch_height import MoveHatchHeight
from subsystems.intake_output import IntakeOutput

from commands.command_logging_decorator import logging_command


@logging_command
class Intake(ConditionalCommand):

    def __init__(self):
        super().__init__(self.__class__.__name__, BallIntakeG(), MoveHatchHeight())

    def condition(self):
        return Command.getRobot().intakeOutput.mode == IntakeOutput.BallOrHatchMode.BALL
