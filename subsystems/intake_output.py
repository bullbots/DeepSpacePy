import enum

from wpilib.command.subsystem import Subsystem
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib.command.command import Command

from ctre.wpi_talonsrx import WPI_TalonSRX
from ctre.wpi_victorspx import WPI_VictorSPX
from ctre._impl import ControlMode

from robotmap import RobotMap
from constants import Constants


class IntakeOutput(Subsystem):
    """
    This subsystem controls the Intake or Output of the Panels or Cargo.
    """
    def __init__(self):
        super().__init__()
        self.leftIntakeTalon = WPI_TalonSRX(RobotMap.LEFT_INTAKE_TALON)
        self.rightIntakeTalon = WPI_TalonSRX(RobotMap.RIGHT_INTAKE_TALON)
        self.intakeVictor = WPI_VictorSPX(RobotMap.END_EFFECTOR_VICTOR)

        self.intakeSolenoid = DoubleSolenoid(RobotMap.INTAKE_IN_SOLENOID, RobotMap.INTAKE_OUT_SOLENOID)
        self.placingSolenoid = DoubleSolenoid(RobotMap.PLACE_IN_SOLENOID, RobotMap.PLACE_OUT_SOLENOID)

        self.leftIntakeTalon.configContinuousCurrentLimit(6, Constants.TIMEOUT_MS)
        self.rightIntakeTalon.configContinuousCurrentLimit(6, Constants.TIMEOUT_MS)

        self.setPosition(IntakeOutput.Position.UP)
        self.setPower(0)

        self.mode = None  # This cannot be set here because the buttons do not yet exist.

    def initDefaultCommand(self):
        pass

    def setPosition(self, pos):
        if pos == IntakeOutput.Position.DOWN:
            self.intakeSolenoid.set(DoubleSolenoid.Value.kReverse)
        elif pos == IntakeOutput.Position.UP:
            self.intakeSolenoid.set(DoubleSolenoid.Value.kForward)

    def setArmPower(self, power):
        self.leftIntakeTalon.set(-power)
        self.rightIntakeTalon.set(power)

    def panelPlace(self, putortake):
        if putortake == IntakeOutput.PanelPutOrTake.PUT:
            self.placingSolenoid.set(DoubleSolenoid.Value.kForward)
        elif putortake == IntakeOutput.PanelPutOrTake.TAKE:
            self.placingSolenoid.set(DoubleSolenoid.Value.kReverse)

    def giveOrTakeCargo(self, giveortake):
        if giveortake == IntakeOutput.CargeGiveOrTake.GIVE:
            self.intakeVictor.set(ControlMode.PercentOutput, 1)
        elif giveortake == IntakeOutput.CargeGiveOrTake.TAKE:
            self.intakeVictor.set(ControlMode.PercentOutput, -0.5)
        elif giveortake == IntakeOutput.CargeGiveOrTake.NADA:
            self.intakeVictor.set(ControlMode.PercentOutput, 0)

    def getPistonPos(self):
        return self.placingSolenoid.get() == DoubleSolenoid.Value.kForward

    def setMode(self, mode):
        assert (isinstance(mode, IntakeOutput.BallOrHatchMode))
        self.mode = mode

    class Position(enum.IntEnum):
        DOWN = 0
        UP = 1

    class PanelPutOrTake(enum.IntEnum):
        PUT = 0
        TAKE = 1

    class CargeGiveOrTake(enum.IntEnum):
        NADA = 0
        GIVE = 1
        TAKE = 2

    class BallOrHatchMode(enum.IntEnum):
        BALL = 0
        HATCH = 1

    class IntakeInOutNeutral(enum.IntEnum):
        NEUTRAL = 0
        IN = 1
        OUT = 2
