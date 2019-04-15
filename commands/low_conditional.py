from wpilib.command.conditionalcommand import ConditionalCommand
from wpilib.command.command import Command

from commands.place_ball_group import PlaceBallG
from commands.place_hatch_group import PlaceHatchG
from subsystems.intake_output import IntakeOutput


from commands.command_logging_decorator import logging_command


@logging_command
class LowConditional(ConditionalCommand):

    def __init__(self):
        super().__init__(self.__class__.__name__, PlaceBallG(43.2), PlaceHatchG(16))

    def condition(self):
        return Command.getRobot().intakeOutput.mode == IntakeOutput.BallOrHatchMode.BALL
