from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command

from commands.command_logging_decorator import logging_command


@logging_command
class MoveHatchHeight(InstantCommand):

    def __init__(self):
        super().__init__(subsystem=Command.getRobot().liftElevator)

    def initialize(self):
        Command.getRobot().liftElevator.setElevatorReference(6.5)
