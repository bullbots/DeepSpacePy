import wpilib

from wpilib.command import Command
from commandbased import CommandBasedRobot

from wpilib.compressor import Compressor

from commands.drivetobaseline import DelayedDriveToBaseLine
from subsystems.lift_elevator import LiftElevator
from subsystems.drivetrain import DriveTrain
from subsystems.intake_output import IntakeOutput
from oi import OI


class DeepSpaceRobot(CommandBasedRobot):
    """
    The CommandBasedRobot base class implements almost everything you need for
    a working robot program. All you need to do is set up the subsystems and
    commands. You do not need to override the "periodic" functions, as they
    will automatically call the scheduler. You may override the "init" functions
    if you want to do anything special when the mode changes.
    """
    def robotInit(self):
        """
        This is a good place to set up your subsystems and anything else that
        you will need to access later.
        """
        # Define Robot getter
        Command.getRobot = lambda: self

        # Create subsystems
        self.liftElevator = LiftElevator()
        self.drivetrain = DriveTrain()
        self.intakeOutput = IntakeOutput()

        self.compressor = Compressor()
        self.compressor.start()

        # Shuffleboard options

        # Autonomous commands
        self.autonomousCommand = DelayedDriveToBaseLine()

        """
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        """
        self.oi = OI()

    def autonomousInit(self):
        """
        You should call start on your autonomous program here. You can
        instantiate the program here if you like, or in robotInit as in this
        example. You can also use a SendableChooser to have the autonomous
        program chosen from the SmartDashboard.
        """
        self.autonomousCommand.start()


if __name__ == "__main__":
    wpilib.run(DeepSpaceRobot)
