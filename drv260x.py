from drv260x_base import DRV260X_Base
import drv260x_constants.values as Values

class DRV260X(DRV260X_Base):
    
    _bemf_gain_values = {
        Values.N_ERM_LRA_ERM: [0.33, 1.0, 1.8, 4.0],
        Values.N_ERM_LRA_LRA: [5.0, 10.0, 20.0, 30.0]
    }

    _sample_time_values = [
        150, 200, 250, 300
    ]

    _fb_brake_factor_values = [1, 2, 3, 4, 6, 8, 16, 0]

    def __init__(self, i2c):
        super().__init__(i2c)

    def set_base_calibration_values(self, erm_lra, closed_open_loop, fb_brake_factor, loop_gain, auto_cal_time, drive_time, sample_time = Values.SAMPLE_TIME_300, blanking_time = 2, idiss_time = 1):
        self.standby = Values.STANDBY_READY
        self.mode = Values.MODE_AUTOCAL
        self.n_erm_lra = erm_lra
         # Set Loop Mode
        self.erm_open_loop = closed_open_loop
        self.lra_open_loop = closed_open_loop
        # Set required values for calibration
        self.fb_brake_factor = fb_brake_factor
        self.loop_gain = loop_gain
        self.auto_cal_time = auto_cal_time
        self.drive_time = drive_time
        # LRA only. Advances use
        self.sample_time = sample_time
        self.blanking_time = blanking_time
        self.idiss_time = idiss_time

    @property
    def lra_period_us(self):
        return self.lra_period * 98.46
    
    @lra_period_us.setter
    def lra_period_us(self, value):
        self.lra_period = value / 98.46

    @property
    def vbat_volt(self, value):
        return self.vbat * 5.6 / 255.0
    
    @property
    def bemf_gain_value(self):
        return self._bemf_gain_values[self.n_erm_lra][self.bemf_gain]

    @property
    def fb_brake_factor_value(self):
        return self._fb_brake_factor_values[self.fb_brake_factor]

    @property
    def a_cal_bemf_volt(self):
        return ((self.a_cal_bemf / 255.0) * 1.22) / self.bemf_gain_value
    
    @property
    def a_cal_comp_coeff(self):
        return 1.0 + self.a_cal_comp / 255.0

    @property
    def ath_max_drive_percent(self):
        return (self.ath_max_drive / 255.0) * 100.0
    
    @ath_max_drive_percent.setter
    def ath_max_drive_percent(self, value):
        if not 0 <= value <= 100:
            raise ValueError("value must be between 0 and 100")
        self.ath_max_drive = (value / 100.0) * 255.0
    
    @property
    def ath_min_drive_percent(self):
        return (self.ath_min_drive / 255.0) * 100.0
    
    @ath_min_drive_percent.setter
    def ath_min_drive_percent(self, value):
        if not 0 <= value <= 100:
            raise ValueError("value must be between 0 and 100")
        self.ath_min_drive = (value / 100.0) * 255.0
    
    @property
    def ath_max_input_voltage(self):
        return (self.ath_max_input * 1.8) / 255.0
    
    @ath_max_input_voltage.setter
    def ath_max_input_voltage(self, value):
        if not 0 <= value <= 100:
            raise ValueError("value must be between 0 and 100")
        self.ath_max_input = (value / 1.8) * 255.0

    @property
    def ath_min_input_voltage(self):
        return (self.ath_max_input * 1.8) / 255.0
    
    @ath_min_input_voltage.setter
    def ath_min_input_voltage(self, value):
        if not 0 <= value <= 100:
            raise ValueError("value must be between 0 and 100")
        self.ath_max_input = (value / 1.8) * 255.0
    
    @property
    def ath_peak_time_ms(self):
        return self.ath_peak_time * 10 + 10

    @ath_peak_time_ms.setter
    def ath_peak_time_ms(self, value):
        if value < 10 or value > 40 or value % 10 != 0:
            raise ValueError("ath_peak_time_ms must be 10, 20, 30, or 40")
        self.ath_peak_time = (value - 10) / 10.0

    @property
    def drive_time_ms(self):
        if self.n_erm_lra == Values.N_ERM_LRA_LRA:
            return self.drive_time * 0.1 + 0.5
        else:
            return self.drive_time * 0.2 + 1.0
    
    @drive_time_ms.setter
    def drive_time_ms(self, value):
        if self.n_erm_lra == Values.N_ERM_LRA_LRA:
            self.drive_time = (value - 0.5) / 0.1
        else:
            self.drive_time = (value - 1.0) / 0.2
