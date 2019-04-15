from wpilib.command import Command

from commands.command_logging_decorator import logging_command


@logging_command
class MoveLift(Command):

    def __init__(self, targetPos):
        super().__init__("MoveLift {}".format(targetPos))
        self.targetPos = 150 if targetPos > 150 else targetPos

    def initialize(self):
        Command.getRobot().lift.setLiftReference(self.targetPos)

    def isFinished(self):
        return abs(Command.getRobot().liftElevator.getLiftPos() - self.targetPos) < 1
