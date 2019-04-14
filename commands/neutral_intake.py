from wpilib.command.conditionalcommand import ConditionalCommand
from wpilib.command.command import Command

from commands.neutral_arm import NeutralArm
from commands.hatch_intake_group import HatchIntakeG

from subsystems.intake_output import IntakeOutput


class NeutralIntake(ConditionalCommand):

    def __init__(self):
        super().__init__(self.__class__.__name__, NeutralArm(), HatchIntakeG())

    def condition(self):
        return Command.getRobot().intakeOutput.mode == IntakeOutput.BallOrHatchMode.BALL
