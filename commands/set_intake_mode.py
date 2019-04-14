from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command

from subsystems.intake_output import IntakeOutput


class SetIntakeMode(InstantCommand):

    def __init__(self, mode):
        super().__init__(subsystem=Command.getRobot().intakeOutput)
        self.mode = mode

    def initialize(self):
        if self.mode == IntakeOutput.IntakeInOutNeutral.NEUTRAL:
            Command.getRobot().intakeOutput.setPower(0.0)
            Command.getRobot().intakeOutput.setPosition(IntakeOutput.Position.UP)
        elif self.mode == IntakeOutput.IntakeInOutNeutral.IN:
            Command.getRobot().intakeOutput.setPower(0.5)
            Command.getRobot().intakeOutput.setPosition(IntakeOutput.Position.DOWN)
        elif self.mode == IntakeOutput.IntakeInOutNeutral.OUT:
            Command.getRobot().intakeOutput.setPower(-1.0)
            Command.getRobot().intakeOutput.setPosition(IntakeOutput.Position.DOWN)
