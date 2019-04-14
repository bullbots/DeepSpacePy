from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command


class MoveHatchHeight(InstantCommand):

    def __init__(self):
        super().__init__(subsystem=Command.getRobot().liftElevator)

    def initialize(self):
        Command.getRobot().liftElevator.setElevatorReference(6.5)
