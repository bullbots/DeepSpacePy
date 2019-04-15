import logging

from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command

from subsystems.intake_output import IntakeOutput


class SetObjectMode(InstantCommand):

    def __init__(self, mode):
        super().__init__(name="SetObjectMode", subsystem=Command.getRobot().intakeOutput)
        self.mode = mode
        self.logger = logging.getLogger(self.getName())

    def initialize(self):
        Command.getRobot().intakeOutput.panelPlace(IntakeOutput.PanelPutOrTake.TAKE)
        Command.getRobot().intakeOutput.mode = self.mode
