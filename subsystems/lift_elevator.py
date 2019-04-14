from wpilib.command.subsystem import Subsystem

from ctre.wpi_talonsrx import WPI_TalonSRX

from rev import CANSparkMax
from rev._impl.autogen.sim_enums import MotorType, IdleMode, ControlType

from robotmap import RobotMap
from constants import Constants


class LiftElevator(Subsystem):

    def __init__(self):
        super().__init__()
        self.liftDrive = WPI_TalonSRX(RobotMap.BACK_DRIVE_TALON)

        self.liftSpark = CANSparkMax(RobotMap.LIFT_SPARK, MotorType.kBrushless)
        self.liftSpark.restoreFactoryDefaults()
        self.liftSpark.setIdleMode(IdleMode.kCoast)
        self.liftSpark.setSmartCurrentLimit(40)
        self.liftEncoder = self.liftSpark.getEncoder()
        self.liftPID = self.liftSpark.getPIDController()

        self.setLiftPIDConstants()

        self.elevatorSpark = CANSparkMax(RobotMap.ELEVATOR_SPARK, MotorType.kBrushless)
        self.elevatorSpark.restoreFactoryDefaults()
        self.elevatorSpark.setIdleMode(IdleMode.kCoast)
        self.elevatorSpark.setInverted(True)
        self.liftSpark.setSmartCurrentLimit(60)
        self.elevatorEncoder = self.elevatorSpark.getEncoder()
        self.elevatorPID = self.elevatorSpark.getPIDController()

        self.setElevatorPIDConstants()

        # self.liftEncoder.setPosition(0)

    def setLiftPIDConstants(self):
        self.liftPID.setFF(Constants.LIFT_ELEVATOR_FF)
        self.liftPID.setP(Constants.LIFT_ELEVATOR_P)
        self.liftPID.setI(Constants.LIFT_ELEVATOR_I)
        self.liftPID.setD(Constants.LIFT_ELEVATOR_D)

        self.liftPID.setSmartMotionAllowedClosedLoopError(0, 0)
        self.liftPID.setSmartMotionMaxVelocity(Constants.LIFT_MAX_VELOCITY, 0)
        self.liftPID.setSmartMotionMaxAccel(Constants.LIFT_MAX_ACCEL, 0)
        self.liftPID.setSmartMotionMinOutputVelocity(0, 0)

    def setElevatorPIDConstants(self):
        self.elevatorPID.setFF(Constants.LIFT_ELEVATOR_FF)
        self.elevatorPID.setP(Constants.LIFT_ELEVATOR_P)
        self.elevatorPID.setI(Constants.LIFT_ELEVATOR_I)
        self.elevatorPID.setD(Constants.LIFT_ELEVATOR_D)

        self.elevatorPID.setSmartMotionMaxVelocity(Constants.ELEVATOR_MAX_VELOCITY, 0)
        self.elevatorPID.setSmartMotionMaxAccel(Constants.ELEVATOR_MAX_ACCEL, 0)
        self.elevatorPID.setSmartMotionAllowedClosedLoopError(0, 0)
        self.elevatorPID.setSmartMotionMinOutputVelocity(0, 0)

    def initDefaultCommand(self):
        pass

    def setLiftReference(self, targetPos):
        self.liftPID.setReference(targetPos, ControlType.kSmartMotion)

    def setElevatorReference(self, targetPos):
        self.elevatorPID.setReference(targetPos, ControlType.kSmartMotion)

    def setDrive(self, magnitude):
        self.liftDrive.set(magnitude)

    def setLift(self, targetSpeed):
        self.liftDrive.set(targetSpeed)

    def setElevator(self, targetSpeed):
        self.elevatorSpark.set(targetSpeed)

    def setLiftElevator(self, targetLiftSpeed, targetElevatorSpeed):
        self.setLift(targetLiftSpeed)
        self.setElevator(targetElevatorSpeed)

    def stopLiftElevator(self):
        self.elevatorSpark.set(0)
        self.liftSpark.set(0)

    def resetEncoders(self):
        self.liftSpark.setEncPosition(0)
        self.elevatorSpark.setEncPosition(0)

    def getLiftElevatorAmps(self):
        return self.liftSpark.getOutputCurrent(), self.elevatorSpark.getOutputCurrent()

    def getLiftPos(self):
        self.liftEncoder.getPosition()

    def getElevatorPos(self):
        self.elevatorEncoder.getPosition()

    def getLiftElevatorPos(self):
        return self.getLiftPos(), self.getElevatorPos()

    def getLiftElevatorTemps(self):
        return self.liftSpark.getMotorTemperature(), self.elevatorSpark.getMotorTemperature()
