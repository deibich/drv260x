import drv260x_constants.library as Library
import drv260x_constants.mode as Mode
import drv260x_constants.register as Register
import drv260x_constants.bitmasks as Mask
import drv260x_constants.misc as Misc

from smbus2 import SMBus
import math

class DRV260X:
    def __init__(self, i2c_bus_num = 1):
        self.__i2c_bus_num = i2c_bus_num
        self.__i2c_bus = SMBus(self.__i2c_bus_num)
        self._mode = -1
        self.__library = -1
        self.__standby = -1
        self.__actuator = -1
        self.__device_id = -1
        self.__rtp_format = -1
        if not self.is_present():
            raise ConnectionError("Not present")
    
    @property
    def device_id(self):
        if self.__device_id < 0:
            self.__device_id = self.read_register_value(Register._DRV260X_REG_STATUS, Mask._DEVICE_ID_READ, 7)
        return self.__device_id

    @property
    def diag_result(self):
        return self.read_register_value(Register._DRV260X_REG_STATUS, Mask._DIAG_RESULT_READ, 3)

    @property
    def fb_sts(self):
        return self.read_register_value(Register._DRV260X_REG_STATUS, Mask._FB_STS_READ, 2)
    
    @property
    def over_temp(self):
        return self.read_register_value(Register._DRV260X_REG_STATUS, Mask._OVER_TEMP_READ, 1)
    
    @property
    def oc_detect(self):
        return self.read_register_value(Register._DRV260X_REG_STATUS, Mask._OC_DETECT_READ, 0)
    
    @property
    def dev_reset(self):
        return self.read_register_value(Register._DRV260X_REG_MODE, Mask._DEV_RESET_READ, 7)

    @dev_reset.setter
    def dev_reset(self, value):
        self.set_register_value(Register._DRV260X_REG_MODE, value, Mask._DEV_RESET_WRITE, 7)

    @property
    def standby(self):
        if self.__standby < 0:
            self.__standby = self.read_register_value(Register._DRV260X_REG_MODE, Mask._MODE_READ, 6)
        if self.__standby == 0:
            return False
        else:
            return True
    
    @standby.setter
    def standby(self, value):
        if value:
            self.set_register_value(Register._DRV260X_REG_MODE, 1, Mask._STANDBY_WRITE, 6)
            self.__standby = 1
        else:
            self.set_register_value(Register._DRV260X_REG_MODE, 0, Mask._STANDBY_WRITE, 6)
            self.__standby = 0

    @property
    def mode(self):
        if self._mode < 0:
            self._mode = self.read_register_value(Register._DRV260X_REG_MODE, Mask._MODE_READ)
        return self._mode

    @mode.setter
    def mode(self, value):
        if not Mode.INT_TRIG <= value <= Mode.AUTOCAL:
            raise ValueError("Mode value must be between 0 and 6")
        self.set_register_value(Register._DRV260X_REG_MODE, value, Mask._MODE_WRITE)
        self._mode = value

    @property
    def rtp_input(self):
        return self.read_register_value(Register._DRV260X_REG_RTP_IN, Mask._RTP_INPUT_READ)

    @rtp_input.setter
    def rtp_input(self, value):
        self.set_register_value(Register._DRV260X_REG_RTP_IN, value, Mask._RTP_INPUT_WRITE)

    @property
    def hi_z(self):
        self.read_register_value(Register._DRV260X_REG_LIBRARY, Mask._HI_Z_READ, 4)

    @hi_z.setter
    def hi_z(self, value):
        self.set_register_value(Register._DRV260X_REG_LIBRARY, value, Mask._HI_Z_WRITE, 4)

    @property
    def library(self):
        if self.__library < 0:
            self.__library = self.read_register_value(Register._DRV260X_REG_LIBRARY, Mask._LIBRARY_SEL_READ)
        return self.__library

    @library.setter
    def library(self, value):
        if not Library.EMPTY <= value <= Library.LRA:
            raise ValueError("Library value must be between 0 and 6")
        self.set_register_value(Register._DRV260X_REG_LIBRARY, value, Mask._LIBRARY_SEL_READ)
        self.__library = value

    @property
    def wait0(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ0, Mask._WAIT_READ, 7)

    @wait0.setter
    def wait0(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ0, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq0(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ0, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq0.setter
    def wav_frm_seq0(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ0, value, Mask._WAV_FRM_SEQ_WRITE)

    @property
    def wait1(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ1, Mask._WAIT_READ, 7)

    @wait1.setter
    def wait1(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ1, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq1(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ1, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq1.setter
    def wav_frm_seq1(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ1, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait2(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ2, Mask._WAIT_READ, 7)

    @wait2.setter
    def wait2(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ2, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq2(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ2, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq2.setter
    def wav_frm_seq2(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ2, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait3(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ3, Mask._WAIT_READ, 7)

    @wait3.setter
    def wait3(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ3, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq3(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ3, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq3.setter
    def wav_frm_seq3(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ3, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait4(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ4, Mask._WAIT_READ, 7)

    @wait4.setter
    def wait4(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ4, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq4(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ4, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq4.setter
    def wav_frm_seq4(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ4, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait5(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ5, Mask._WAIT_READ, 7)

    @wait5.setter
    def wait5(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ5, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq5(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ5, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq5.setter
    def wav_frm_seq5(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ5, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait6(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ6, Mask._WAIT_READ, 7)

    @wait6.setter
    def wait6(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ6, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq6(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ6, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq6.setter
    def wav_frm_seq6(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ6, value, Mask._WAV_FRM_SEQ_WRITE)

    @property
    def wait7(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ7, Mask._WAIT_READ, 7)

    @wait7.setter
    def wait7(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ7, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq7(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ7, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq7.setter
    def wav_frm_seq7(self, value):
        self.set_register_value(Register._DRV260X_REG_WAVESEQ7, value, Mask._WAV_FRM_SEQ_WRITE)

    @property
    def go(self):
        return self.read_register_value(Register._DRV260X_REG_GO, Mask._GO_READ)

    @go.setter
    def go(self, value):
        self.set_register_value(Register._DRV260X_REG_GO, value, Mask._GO_WRITE)

    @property
    def odt(self):
        self.read_register_value(Register._DRV260X_REG_OVERDRIVE, Mask._ODT_READ)

    @odt.setter
    def odt(self, value):
        self.set_register_value(Register._DRV260X_REG_OVERDRIVE, value, Mask._OD_CLAMP_WRITE)

    @property
    def spt(self):
        self.read_register_value(Register._DRV260X_REG_SUSTAINPOS, Mask._SPT_READ)

    @spt.setter
    def spt(self, value):
        self.set_register_value(Register._DRV260X_REG_SUSTAINPOS, value, Mask._SPT_WRITE)

    @property
    def snt(self):
        self.read_register_value(Register._DRV260X_REG_SUSTAINNEG, Mask._SNT_READ)

    @snt.setter
    def snt(self, value):
        self.set_register_value(Register._DRV260X_REG_SUSTAINNEG, value, Mask._SNT_WRITE)

    @property
    def brt(self):
        self.read_register_value(Register._DRV260X_REG_BREAK_TIME_OFFSET, Mask._BRT_READ)

    @brt.setter
    def brt(self, value):
        self.set_register_value(Register._DRV260X_REG_BREAK_TIME_OFFSET, value, Mask._BRT_WRITE)

    @property
    def ath_peak_time(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB, Mask._ATH_PEAK_TIME_READ)

    @ath_peak_time.setter
    def ath_peak_time(self, value):
        self.set_register_value(Register._DRV260X_REG_AUDIO2VIB, value, Mask._ATH_PEAK_TIME_WRITE)

    @property
    def ath_filter(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB, Mask._ATH_FILTER_READ)

    @ath_filter.setter
    def ath_filter(self, value):
        self.set_register_value(Register._DRV260X_REG_AUDIO2VIB, value, Mask._ATH_FILTER_WRITE)

    @property
    def ath_min_input(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB_MIN_IN, Mask._ATH_MIN_INPUT_READ)

    @ath_min_input.setter
    def ath_min_input(self, value):
        self.set_register_value(Register._DRV260X_REG_AUDIO2VIB_MIN_IN, value, Mask._ATH_MIN_INPUT_WRITE)

    @property
    def ath_max_input(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB_MAX_IN, Mask._ATH_MAX_INPUT_READ)

    @ath_max_input.setter
    def ath_max_input(self, value):
        self.set_register_value(Register._DRV260X_REG_AUDIO2VIB_MAX_IN, value, Mask._ATH_MAX_INPUT_WRITE)

    @property
    def ath_min_drive(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB_MIN_OUT, Mask._ATH_MIN_DRIVE_READ)

    @ath_min_drive.setter
    def ath_min_drive(self, value):
        self.set_register_value(Register._DRV260X_REG_AUDIO2VIB_MIN_OUT, value, Mask._ATH_MIN_DRIVE_WRITE)

    @property
    def ath_max_drive(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB_MAX_OUT, Mask._ATH_MAX_DRIVE_READ)

    @ath_max_drive.setter
    def ath_max_drive(self, value):
        self.set_register_value(Register._DRV260X_REG_AUDIO2VIB_MAX_OUT, value, Mask._ATH_MAX_DRIVE_WRITE)

    @property
    def rated_voltage(self):
        return self.read_register_value(Register._DRV260X_REG_RATED_VOLTAGE, Mask._RATED_VOLTAGE_READ)

    @rated_voltage.setter
    def rated_voltage(self, value):
        self.set_register_value(Register._DRV260X_REG_RATED_VOLTAGE, value, Mask._RATED_VOLTAGE_WRITE)

    @property
    def od_clamp(self):
        return self.read_register_value(Register._DRV260X_REG_CLAMP_VOLTAGE, Mask._OD_CLAMP_READ)

    @od_clamp.setter
    def od_clamp(self, value):
        self.set_register_value(Register._DRV260X_REG_CLAMP_VOLTAGE, value, Mask._OD_CLAMP_WRITE)
      
    @property
    def a_cal_comp(self):
        self.read_register_value(Register._DRV260X_REG_AUTOCAL_COMP_RESULT, Mask._A_CAL_COMP_READ)

    @a_cal_comp.setter
    def a_cal_comp(self, value):
        self.set_register_value(Register._DRV260X_REG_AUTOCAL_COMP_RESULT, value, Mask._A_CAL_COMP_WRITE)

    @property
    def a_cal_bemf(self):
        self.read_register_value(Register._DRV260X_REG_AUTOCAL_BACK_EMF_RESULT, Mask._A_CAL_BEMF_READ)

    @a_cal_bemf.setter
    def a_cal_bemf(self, value):
        self.set_register_value(Register._DRV260X_REG_AUTOCAL_BACK_EMF_RESULT, value, Mask._A_CAL_BEMF_WRITE)
        
    @property
    def n_erm_lra(self, value):
        if self.actuator < 0:
            self.__actuator = self.read_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, Mask._N_ERM_LRA_READ, 7)
        return self.__actuator
        
    @n_erm_lra.setter
    def n_erm_lra(self, value):
        if not Misc.ACTUATOR_ERM <= value <= Misc.ACTUATOR_LRA:
            raise ValueError("Actuator value must be " + str(Misc.ACTUATOR_ERM) + " or " + str(Misc.ACTUATOR_LRA))
        self.set_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, value, Mask._N_ERM_LRA_WRITE, 7)
        self.__actuator = value

    @property
    def fb_brake_factor(self):
        return self.read_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, Mask._FB_BRAKE_FACTOR_READ, 4)

    @fb_brake_factor.setter
    def fb_brake_factor(self, value):
        self.set_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, value, Mask._FB_BRAKE_FACTOR_WRITE, 4)

    @property
    def loop_gain(self):
        return self.read_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, Mask._LOOP_GAIN_READ, 2)
        
    @loop_gain.setter
    def loop_gain(self, value):
        self.set_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, value, Mask._LOOP_GAIN_WRITE, 2)

    @property
    def bemf_gain(self):
        return self.read_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, Mask._BEMF_GAIN_READ)
        
    @bemf_gain.setter
    def bemf_gain(self, value):
        self.set_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, value, Mask._BEMF_GAIN_WRITE)

    @property
    def startup_boost(self):
        self.read_register_value(Register._DRV260X_REG_CONTROL1, Mask._STARTUP_BOOST_READ, 7)
    
    @startup_boost.setter
    def startup_boost(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL1, value, Mask._STARTUP_BOOST_WRITE, 7)

    @property
    def ac_couple(self):
        self.read_register_value(Register._DRV260X_REG_CONTROL1, Mask._AC_COUPLE_READ, 5)
    
    @ac_couple.setter
    def ac_couple(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL1, value, Mask._AC_COUPLE_WRITE, 5)
    
    @property
    def drive_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL1, Mask._DRIVE_TIME_READ)
    
    @drive_time.setter
    def drive_time(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL1, value, Mask._DRIVE_TIME_WRITE)
    
    @property
    def bidir_input(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._BIDIR_INPUT_READ, 7)
    
    @bidir_input.setter
    def bidir_input(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._BIDIR_INPUT_WRITE, 7)
    
    @property
    def brake_stabilizer(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._BRAKE_STABILIZER_READ, 6)
    
    @brake_stabilizer.setter
    def brake_stabilizer(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._BRAKE_STABILIZER_WRITE, 6)
    
    @property
    def sample_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._SAMPLE_TIME_READ, 4)
    
    @sample_time.setter
    def sample_time(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._SAMPLE_TIME_WRITE, 4)
    
    @property
    def blanking_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._BLANKING_TIME_READ, 2)
    
    @blanking_time.setter
    def blanking_time(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._BLANKING_TIME_WRITE, 2)
    
    @property
    def idiss_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._IDISS_TIME_READ)
    
    @idiss_time.setter
    def idiss_time(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._IDISS_TIME_READ)
    
    @property
    def ng_tresh(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._NG_TRESH_READ, 6)
    
    @ng_tresh.setter
    def ng_tresh(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._NG_TRESH_WRITE, 6)
    
    @property
    def erm_open_loop(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._ERM_OPEN_LOOP_READ, 5)
    
    @erm_open_loop.setter
    def erm_open_loop(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._ERM_OPEN_LOOP_WRITE, 5)
    
    @property
    def supply_comp_dis(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._SUPPLY_COMP_DIS_READ, 4)
    
    @supply_comp_dis.setter
    def supply_comp_dis(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._SUPPLY_COMP_DIS_WRITE, 4)
    
    @property
    def data_format_rtp(self):
        if self.__rtp_format < 0:
            self.__rtp_format = self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._DATA_FORMAT_RTP_READ, 3)
        return self.__rtp_format

    @data_format_rtp.setter
    def data_format_rtp(self, value):
        if not Misc.RTP_SIGNED <= value <= Misc.RTP_UNSIGNED:
            raise ValueError("RTP format vale must be " + str(Misc.RTP_SIGNED) + " or " + str(Misc.RTP_UNSIGNED))
        self.set_register_value(Register._DRV260X_REG_CONTROL3, Mask._DATA_FORMAT_RTP_WRITE, 3)
    
    @property
    def lra_drive_mode(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._LRA_DRIVE_MODE_READ, 2)
    
    @lra_drive_mode.setter
    def lra_drive_mode(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._LRA_DRIVE_MODE_WRITE, 2)
    
    @property
    def n_pwm_analog(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._N_PWM_ANALOG_READ, 1)
    
    @n_pwm_analog.setter
    def n_pwm_analog(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._N_PWM_ANALOG_WRITE, 1)
    
    @property
    def lra_open_loop(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._LRA_OPEN_LOOP_READ)
    
    @lra_open_loop.setter
    def lra_open_loop(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._LRA_OPEN_LOOP_WRITE)
    
    @property
    def auto_cal_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL4, Mask._AUTO_CAL_TIME_READ, 4)
    
    @auto_cal_time.setter
    def auto_cal_time(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL4, value, Mask._AUTO_CAL_TIME_WRITE, 4)

    @property
    def otp_status(self):
        self.read_register_value(Register._DRV260X_REG_CONTROL4, Mask._OTP_STATUS_READ, 2)
    
    @property
    def otp_program(self):
        self.read_register_value(Register._DRV260X_REG_CONTROL4, Mask._OTP_PROGRAM_READ)

    @otp_program.setter
    def otp_program(self, value):
        self.set_register_value(Register._DRV260X_REG_CONTROL4, value, Mask._OTP_PROGRAM_WRITE)

    @property
    def vbat(self):
        return self.read_register_value(Register._DRV260X_REG_VOLTAGE_MONITOR, Mask._RATED_VOLTAGE_READ)
    
    @vbat.setter
    def vbat(self, value):
        self.set_register_value(Register._DRV260X_REG_VOLTAGE_MONITOR, value, Mask._RATED_VOLTAGE_WRITE)

    @property
    def lra_period(self):
        return self.read_register_value(Register._DRV260X_REG_LRA_RESONANCE_PERIOD, Mask._LRA_PERIOD_READ)
    
    @lra_period.setter
    def lra_period(self, value):
        self.set_register_value(Register._DRV260X_REG_LRA_RESONANCE_PERIOD, value, Mask._LRA_PERIOD_WRITE)  
    
    def set_register_value(self, register, value, write_mask, shift = 0):
        reg_val = self.read_byte(register)
        self.write_byte(register, (reg_val & write_mask) | (value << shift))    

    def read_register_value(self, register, read_mask, shift = 0):
        return (self.read_byte(register) & read_mask) >> shift
    
    def write_byte(self, register, value):
        if not Register._DRV260X_REG_STATUS <= register <= Register._DRV260X_REG_LRA_RESONANCE_PERIOD or register is Register._DRV260X_REG_INVALID_1 or register is Register._DRV260X_REG_INVALID_2:
            raise ValueError("Register " + str(register) + " not valid!")
        return self.__i2c_bus.write_byte_data(Misc._DRV_ADDR, register, value)

    def read_byte(self, register):
        if not Register._DRV260X_REG_STATUS <= register <= Register._DRV260X_REG_LRA_RESONANCE_PERIOD or register is Register._DRV260X_REG_INVALID_1 or register is Register._DRV260X_REG_INVALID_2:
            raise ValueError("Register " + str(register) + " not valid!")
        return self.__i2c_bus.read_byte_data(Misc._DRV_ADDR, register)

    def is_present(self):
        try:
            self.read_byte(Register._DRV260X_REG_STATUS)
            return True
        except Exception:
            return False

    def setup_rtp(self):
        self.standby = False
        # TODO: Calibration procedure
        self.mode = Mode.RTP
    
    def calc_rated_voltage(self, voltage, erm_lra, resonant_frequency = 0, sample_time = 0.0002):
        if erm_lra == Misc.ACTUATOR_ERM:
                return voltage / 0.02133
        elif erm_lra == Misc.ACTUATOR_LRA:
                return voltage / (0.02071 * math.sqrt(1 - (4 * sample_time + 0.0003) * resonant_frequency))
        return 0
    
    def calc_od_clamp(self, voltage, erm_lra, closed_open_loop, resonant_frequency = 0):
        if erm_lra == Misc.ACTUATOR_ERM:
            if closed_open_loop == 0:
                return 0
            elif closed_open_loop == 1:
                return voltage / 0.02196
        elif erm_lra == Misc.ACTUATOR_LRA:
            if closed_open_loop == 0:
                return 0
            elif closed_open_loop == 1:
                return voltage / (0.02133 * math.sqrt(1 - resonant_frequency * 0.0008))
        return 0

    def calibrate(self, erm_lra, fb_brake_factor, loop_gain, voltage, od_clamp, auto_cal_time, drive_time, blanking_time, idiss_time, resonant_frequency, sample_time):
        self.standby = False
        self.mode = Mode.AUTOCAL
        self.actuator = erm_lra
        self.rated_voltage = self.calc_rated_voltage(voltage, erm_lra, resonant_frequency, sample_time)
        self.od_clamp = self.calc_od_clamp
        self.auto_cal_time = auto_cal_time
        self.drive_time = drive_time
