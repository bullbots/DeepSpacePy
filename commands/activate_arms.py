from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command

from commands.command_logging_decorator import logging_command


@logging_command
class ActivateArms(InstantCommand):

    def __init__(self, position):
        super().__init__(name="ActivateArms {}".format(position), subsystem=Command.getRobot().intakeOutput)
        self.position = position

    def initialize(self):
        Command.getRobot().intakeOutput.setPosition(self.position)
