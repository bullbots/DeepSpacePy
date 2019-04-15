import logging

from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command

from subsystems.intake_output import IntakeOutput

from commands.command_logging_decorator import logging_command


@logging_command
class SetIntakeMode(InstantCommand):

    def __init__(self, mode):
        super().__init__(subsystem=Command.getRobot().intakeOutput)
        self.mode = mode
        self.logger = logging.getLogger(self.getName())

    def initialize(self):
        if self.mode == IntakeOutput.IntakeInOutNeutral.NEUTRAL:
            self.logger.info("NEUTRAL")
            Command.getRobot().intakeOutput.setArmPower(0.0)
            Command.getRobot().intakeOutput.setPosition(IntakeOutput.Position.UP)
        elif self.mode == IntakeOutput.IntakeInOutNeutral.IN:
            self.logger.info("IN")
            Command.getRobot().intakeOutput.setArmPower(0.5)
            Command.getRobot().intakeOutput.setPosition(IntakeOutput.Position.DOWN)
        elif self.mode == IntakeOutput.IntakeInOutNeutral.OUT:
            self.logger.info("OUT")
            Command.getRobot().intakeOutput.setArmPower(-1.0)
            Command.getRobot().intakeOutput.setPosition(IntakeOutput.Position.DOWN)
