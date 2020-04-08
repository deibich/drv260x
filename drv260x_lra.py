from drv260x import DRV260X
import drv260x_constants.values as Values
import math

class DRV260X_LRA(DRV260X):
    def __init__(self, i2c):
        super().__init__(i2c)
        self.standby = Values.STANDBY_READY
        self.n_erm_lra = Values.N_ERM_LRA_LRA
    
    def calc_rated_voltage(self, voltage_volt, sample_time, resonant_frequency):
        return voltage_volt / (0.02071 * math.sqrt(1 - (4 * sample_time + 0.0003) * resonant_frequency))
    
    def calc_od_clamp(self, voltage_volt, closed_open_loop, resonant_frequency = 200):
        if closed_open_loop == Values.LOOP_MODE_CLOSED:
            return voltage_volt / 0.02196
        elif closed_open_loop == Values.LOOP_MODE_OPEN:
            return voltage_volt / (0.02133 * math.sqrt(1 - resonant_frequency * 0.0008))
        else:
            raise ValueError("closed_open_loop must be LOOP_MODE_CLOSED or LOOP_MODE_OPEN")
    
    def calibrate(self, voltage_volt, closed_open_loop, resonant_frequency, fb_brake_factor, loop_gain, auto_cal_time, drive_time, idiss_time, blanking_time, sample_time):
        self.set_base_calibration_values(Values.N_ERM_LRA_LRA, closed_open_loop, fb_brake_factor, loop_gain, auto_cal_time, drive_time, sample_time, blanking_time, idiss_time)
        self.rated_voltage = self.calc_rated_voltage(voltage_volt, sample_time, resonant_frequency)
        self.od_clamp = self.calc_od_clamp(voltage_volt, closed_open_loop, drive_time, idiss_time, blanking_time)
