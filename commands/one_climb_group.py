from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from commands.raise_lift_elevator import RaiseLiftElevator
from commands.lift_drive import LiftDrive
from commands.move_elevator import MoveElevator
from commands.activate_arms import ActivateArms
from commands.move_lift import MoveLift
from commands.move import Move

from subsystems.intake_output import IntakeOutput


class OneClimbG(CommandGroup):

    def __init__(self, liftPos=-27, elevatorPos=-19.5):
        super().__init__(name="OneClimbG {}: {}".format(liftPos, elevatorPos))
        self.addSequential(RaiseLiftElevator(liftPos, elevatorPos), 3)
        self.addSequential(LiftDrive(-1), 4)
        self.addSequential(MoveElevator(7))
        self.addSequential(ActivateArms(IntakeOutput.Position.DOWN))
        self.addParallel(LiftDrive(-1), 3.5)
        self.addSequential(Move(3.5), 0.3)
        self.addSequential(WaitCommand(1.0))
        self.addParallel(Move(1), 0.1)
        self.addParallel(MoveLift(2.5))
        self.addSequential(LiftDrive(-1), 1)
