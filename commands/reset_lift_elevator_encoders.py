from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command

from commands.command_logging_decorator import logging_command


@logging_command
class ResetLiftElevatorEncoder(InstantCommand):

    def __init__(self):
        super().__init__(name=self.__class__, subsystem=Command.getRobot().liftElevator)

    def initialize(self):
        Command.getRobot().liftElevator.resetEncoders()
