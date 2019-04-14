from wpilib.command import Command
import logging


class JoystickDrive(Command):

    def __init__(self):
        super().__init__(subsystem=Command.getRobot().drivetrain)
        self.logger = logging.getLogger(self.getName())

    def initialize(self):
        self.logger.info("initialize")
        Command.getRobot().drivetrain.setPIDSlot(1)

    def execute(self):
        joyX = Command.getRobot().oi.driveStick.getX()
        joyY = Command.getRobot().oi.driveStick.getY()
        Command.getRobot().drivetrain.customArcadeDrive(joyX, -joyY, squareInputs=True)

    def isFinished(self):
        return False
