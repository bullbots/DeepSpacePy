from wpilib.command import Command

from commands.command_logging_decorator import logging_command


@logging_command
class MoveElevator(Command):

    def __init__(self, targetPos):
        super().__init__("MoveElevator {}".format(targetPos))
        self.targetPos = 150 if targetPos > 150 else targetPos

    def initialize(self):
        Command.getRobot().liftElevator.setElevatorReference(self.targetPos)

    def isFinished(self):
        return abs(Command.getRobot().liftElevator.getElevatorPos() - self.targetPos) < 1
