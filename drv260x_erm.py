from drv260x import DRV260X
import drv260x_constants.values as Values

class DRV260X_ERM(DRV260X):
    def __init__(self, i2c):
        super().__init__(i2c)
        self.standby = 0
        self.n_erm_lra = Values.N_ERM_LRA_ERM

    def calc_rated_voltage(self, voltage_volt):
        return voltage_volt / 0.02133

    def calc_od_clamp(self, voltage_volt, closed_open_loop, drive_time, idiss_time, blanking_time):
        if closed_open_loop == Values.LOOP_MODE_CLOSED:
            return (voltage_volt * (drive_time + idiss_time + blanking_time)) / (0.02133 * (drive_time - 0.000300))
        elif closed_open_loop == Values.LOOP_MODE_OPEN:
            return voltage_volt / 0.02196
        else:
            raise ValueError("closed_open_loop must be LOOP_MODE_CLOSED or LOOP_MODE_OPEN")
    
    def calibrate(self, voltage_volt, closed_open_loop, fb_brake_factor, loop_gain, auto_cal_time, drive_time, idiss_time, blanking_time, sample_time):
        self.set_base_calibration_values(Values.N_ERM_LRA_ERM, closed_open_loop, fb_brake_factor, loop_gain, auto_cal_time, drive_time, sample_time, blanking_time, idiss_time)
        self.rated_voltage = self.calc_rated_voltage(voltage_volt)
        self.od_clamp = self.calc_od_clamp(voltage_volt, closed_open_loop, drive_time, idiss_time, blanking_time)

    def calibrate_default():
        pass