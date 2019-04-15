from wpilib.command import Command
import logging
from commands.command_logging_decorator import logging_command


@logging_command
class JoystickDrive(Command):

    def __init__(self):
        super().__init__(subsystem=Command.getRobot().drivetrain)

    def initialize(self):
        Command.getRobot().drivetrain.setPIDSlot(1)

    def execute(self):
        joyX = Command.getRobot().oi.driveStick.getX()
        joyY = Command.getRobot().oi.driveStick.getY()
        Command.getRobot().drivetrain.customArcadeDrive(joyX, -joyY, squareInputs=True)

    def isFinished(self):
        return False
