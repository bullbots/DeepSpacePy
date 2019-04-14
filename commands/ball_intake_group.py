from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from commands.take_panel import TakePanel
from commands.set_intake_mode import SetIntakeMode
from commands.inhale_exhale import InhaleExhale
from commands.put_panel import PutPanel

from subsystems.intake_output import IntakeOutput


class BallIntakeG(CommandGroup):

    def __init__(self):
        super().__init__(name=self.__class__.__name__)
        self.addSequential(TakePanel(), 0.25)
        self.addSequential(SetIntakeMode(IntakeOutput.IntakeInOutNeutral.IN))
        self.addSequential(InhaleExhale(IntakeOutput.CargeGiveOrTake.TAKE))
        self.addSequential(WaitCommand(0.25))
        self.addSequential(PutPanel(), 0.25)
