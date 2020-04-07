import drv260x_constants.library as Library
import drv260x_constants.mode as Mode
import drv260x_constants.register as Register
import drv260x_constants.bitmasks as Mask
import drv260x_constants.misc as Misc

import math

class DRV260X_Base:

    def __init__(self, i2c):
        self.__i2c_bus = i2c
        if not self.is_present():
            raise ConnectionError("Not present")
    
    @property
    def device_id(self):
        return self.read_register_value(Register._DRV260X_REG_STATUS, Mask._DEVICE_ID_READ, 7)

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
        self.write_register_value(Register._DRV260X_REG_MODE, value, Mask._DEV_RESET_WRITE, 7)

    @property
    def standby(self):
        return self.read_register_value(Register._DRV260X_REG_MODE, Mask._MODE_READ, 6)
    
    @standby.setter
    def standby(self, value):
        self.write_register_value(Register._DRV260X_REG_MODE, 1, Mask._STANDBY_WRITE, 6)

    @property
    def mode(self):
        return self.read_register_value(Register._DRV260X_REG_MODE, Mask._MODE_READ)

    @mode.setter
    def mode(self, value):
        if not Mode.INT_TRIG <= value <= Mode.AUTOCAL:
            raise ValueError("Mode value must be between 0 and 6")
        self.write_register_value(Register._DRV260X_REG_MODE, value, Mask._MODE_WRITE)

    @property
    def rtp_input(self):
        return self.read_register_value(Register._DRV260X_REG_RTP_IN, Mask._RTP_INPUT_READ)

    @rtp_input.setter
    def rtp_input(self, value):
        self.write_register_value(Register._DRV260X_REG_RTP_IN, value, Mask._RTP_INPUT_WRITE)

    @property
    def hi_z(self):
        self.read_register_value(Register._DRV260X_REG_LIBRARY, Mask._HI_Z_READ, 4)

    @hi_z.setter
    def hi_z(self, value):
        self.write_register_value(Register._DRV260X_REG_LIBRARY, value, Mask._HI_Z_WRITE, 4)

    @property
    def library(self):
        return self.read_register_value(Register._DRV260X_REG_LIBRARY, Mask._LIBRARY_SEL_READ)

    @library.setter
    def library(self, value):
        if not Library.EMPTY <= value <= Library.LRA:
            raise ValueError("Library value must be between 0 and 6")
        self.write_register_value(Register._DRV260X_REG_LIBRARY, value, Mask._LIBRARY_SEL_READ)

    @property
    def wait0(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ0, Mask._WAIT_READ, 7)

    @wait0.setter
    def wait0(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ0, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq0(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ0, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq0.setter
    def wav_frm_seq0(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ0, value, Mask._WAV_FRM_SEQ_WRITE)

    @property
    def wait1(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ1, Mask._WAIT_READ, 7)

    @wait1.setter
    def wait1(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ1, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq1(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ1, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq1.setter
    def wav_frm_seq1(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ1, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait2(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ2, Mask._WAIT_READ, 7)

    @wait2.setter
    def wait2(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ2, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq2(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ2, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq2.setter
    def wav_frm_seq2(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ2, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait3(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ3, Mask._WAIT_READ, 7)

    @wait3.setter
    def wait3(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ3, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq3(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ3, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq3.setter
    def wav_frm_seq3(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ3, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait4(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ4, Mask._WAIT_READ, 7)

    @wait4.setter
    def wait4(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ4, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq4(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ4, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq4.setter
    def wav_frm_seq4(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ4, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait5(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ5, Mask._WAIT_READ, 7)

    @wait5.setter
    def wait5(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ5, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq5(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ5, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq5.setter
    def wav_frm_seq5(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ5, value, Mask._WAV_FRM_SEQ_WRITE)
    
    @property
    def wait6(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ6, Mask._WAIT_READ, 7)

    @wait6.setter
    def wait6(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ6, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq6(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ6, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq6.setter
    def wav_frm_seq6(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ6, value, Mask._WAV_FRM_SEQ_WRITE)

    @property
    def wait7(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ7, Mask._WAIT_READ, 7)

    @wait7.setter
    def wait7(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ7, Mask._WAIT_WRITE, 7)

    @property
    def wav_frm_seq7(self):
        self.read_register_value(Register._DRV260X_REG_WAVESEQ7, Mask._WAV_FRM_SEQ_READ)

    @wav_frm_seq7.setter
    def wav_frm_seq7(self, value):
        self.write_register_value(Register._DRV260X_REG_WAVESEQ7, value, Mask._WAV_FRM_SEQ_WRITE)

    @property
    def go(self):
        return self.read_register_value(Register._DRV260X_REG_GO, Mask._GO_READ)

    @go.setter
    def go(self, value):
        self.write_register_value(Register._DRV260X_REG_GO, value, Mask._GO_WRITE)

    @property
    def odt(self):
        self.read_register_value(Register._DRV260X_REG_OVERDRIVE, Mask._ODT_READ)

    @odt.setter
    def odt(self, value):
        self.write_register_value(Register._DRV260X_REG_OVERDRIVE, value, Mask._OD_CLAMP_WRITE)

    @property
    def spt(self):
        self.read_register_value(Register._DRV260X_REG_SUSTAINPOS, Mask._SPT_READ)

    @spt.setter
    def spt(self, value):
        self.write_register_value(Register._DRV260X_REG_SUSTAINPOS, value, Mask._SPT_WRITE)

    @property
    def snt(self):
        self.read_register_value(Register._DRV260X_REG_SUSTAINNEG, Mask._SNT_READ)

    @snt.setter
    def snt(self, value):
        self.write_register_value(Register._DRV260X_REG_SUSTAINNEG, value, Mask._SNT_WRITE)

    @property
    def brt(self):
        self.read_register_value(Register._DRV260X_REG_BREAK_TIME_OFFSET, Mask._BRT_READ)

    @brt.setter
    def brt(self, value):
        self.write_register_value(Register._DRV260X_REG_BREAK_TIME_OFFSET, value, Mask._BRT_WRITE)

    @property
    def ath_peak_time(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB, Mask._ATH_PEAK_TIME_READ)

    @ath_peak_time.setter
    def ath_peak_time(self, value):
        self.write_register_value(Register._DRV260X_REG_AUDIO2VIB, value, Mask._ATH_PEAK_TIME_WRITE)

    @property
    def ath_filter(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB, Mask._ATH_FILTER_READ)

    @ath_filter.setter
    def ath_filter(self, value):
        self.write_register_value(Register._DRV260X_REG_AUDIO2VIB, value, Mask._ATH_FILTER_WRITE)

    @property
    def ath_min_input(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB_MIN_IN, Mask._ATH_MIN_INPUT_READ)

    @ath_min_input.setter
    def ath_min_input(self, value):
        self.write_register_value(Register._DRV260X_REG_AUDIO2VIB_MIN_IN, value, Mask._ATH_MIN_INPUT_WRITE)

    @property
    def ath_max_input(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB_MAX_IN, Mask._ATH_MAX_INPUT_READ)

    @ath_max_input.setter
    def ath_max_input(self, value):
        self.write_register_value(Register._DRV260X_REG_AUDIO2VIB_MAX_IN, value, Mask._ATH_MAX_INPUT_WRITE)

    @property
    def ath_min_drive(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB_MIN_OUT, Mask._ATH_MIN_DRIVE_READ)

    @ath_min_drive.setter
    def ath_min_drive(self, value):
        self.write_register_value(Register._DRV260X_REG_AUDIO2VIB_MIN_OUT, value, Mask._ATH_MIN_DRIVE_WRITE)

    @property
    def ath_max_drive(self):
        self.read_register_value(Register._DRV260X_REG_AUDIO2VIB_MAX_OUT, Mask._ATH_MAX_DRIVE_READ)

    @ath_max_drive.setter
    def ath_max_drive(self, value):
        self.write_register_value(Register._DRV260X_REG_AUDIO2VIB_MAX_OUT, value, Mask._ATH_MAX_DRIVE_WRITE)

    @property
    def rated_voltage(self):
        return self.read_register_value(Register._DRV260X_REG_RATED_VOLTAGE, Mask._RATED_VOLTAGE_READ)

    @rated_voltage.setter
    def rated_voltage(self, value):
        self.write_register_value(Register._DRV260X_REG_RATED_VOLTAGE, value, Mask._RATED_VOLTAGE_WRITE)

    @property
    def od_clamp(self):
        return self.read_register_value(Register._DRV260X_REG_CLAMP_VOLTAGE, Mask._OD_CLAMP_READ)

    @od_clamp.setter
    def od_clamp(self, value):
        self.write_register_value(Register._DRV260X_REG_CLAMP_VOLTAGE, value, Mask._OD_CLAMP_WRITE)
      
    @property
    def a_cal_comp(self):
        self.read_register_value(Register._DRV260X_REG_AUTOCAL_COMP_RESULT, Mask._A_CAL_COMP_READ)

    @a_cal_comp.setter
    def a_cal_comp(self, value):
        self.write_register_value(Register._DRV260X_REG_AUTOCAL_COMP_RESULT, value, Mask._A_CAL_COMP_WRITE)

    @property
    def a_cal_bemf(self):
        self.read_register_value(Register._DRV260X_REG_AUTOCAL_BACK_EMF_RESULT, Mask._A_CAL_BEMF_READ)

    @a_cal_bemf.setter
    def a_cal_bemf(self, value):
        self.write_register_value(Register._DRV260X_REG_AUTOCAL_BACK_EMF_RESULT, value, Mask._A_CAL_BEMF_WRITE)
        
    @property
    def n_erm_lra(self, value):
        return self.read_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, Mask._N_ERM_LRA_READ, 7)
        
    @n_erm_lra.setter
    def n_erm_lra(self, value):
        if not Misc.ACTUATOR_ERM <= value <= Misc.ACTUATOR_LRA:
            raise ValueError("Actuator value must be " + str(Misc.ACTUATOR_ERM) + " or " + str(Misc.ACTUATOR_LRA))
        self.write_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, value, Mask._N_ERM_LRA_WRITE, 7)

    @property
    def fb_brake_factor(self):
        return self.read_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, Mask._FB_BRAKE_FACTOR_READ, 4)

    @fb_brake_factor.setter
    def fb_brake_factor(self, value):
        self.write_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, value, Mask._FB_BRAKE_FACTOR_WRITE, 4)

    @property
    def loop_gain(self):
        return self.read_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, Mask._LOOP_GAIN_READ, 2)
        
    @loop_gain.setter
    def loop_gain(self, value):
        self.write_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, value, Mask._LOOP_GAIN_WRITE, 2)

    @property
    def bemf_gain(self):
        return self.read_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, Mask._BEMF_GAIN_READ)
        
    @bemf_gain.setter
    def bemf_gain(self, value):
        self.write_register_value(Register._DRV260X_REG_FEEDBACK_CONTROL, value, Mask._BEMF_GAIN_WRITE)

    @property
    def startup_boost(self):
        self.read_register_value(Register._DRV260X_REG_CONTROL1, Mask._STARTUP_BOOST_READ, 7)
    
    @startup_boost.setter
    def startup_boost(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL1, value, Mask._STARTUP_BOOST_WRITE, 7)

    @property
    def ac_couple(self):
        self.read_register_value(Register._DRV260X_REG_CONTROL1, Mask._AC_COUPLE_READ, 5)
    
    @ac_couple.setter
    def ac_couple(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL1, value, Mask._AC_COUPLE_WRITE, 5)
    
    @property
    def drive_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL1, Mask._DRIVE_TIME_READ)
    
    @drive_time.setter
    def drive_time(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL1, value, Mask._DRIVE_TIME_WRITE)
    
    @property
    def bidir_input(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._BIDIR_INPUT_READ, 7)
    
    @bidir_input.setter
    def bidir_input(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._BIDIR_INPUT_WRITE, 7)
    
    @property
    def brake_stabilizer(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._BRAKE_STABILIZER_READ, 6)
    
    @brake_stabilizer.setter
    def brake_stabilizer(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._BRAKE_STABILIZER_WRITE, 6)
    
    @property
    def sample_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._SAMPLE_TIME_READ, 4)
    
    @sample_time.setter
    def sample_time(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._SAMPLE_TIME_WRITE, 4)
    
    @property
    def blanking_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._BLANKING_TIME_READ, 2)
    
    @blanking_time.setter
    def blanking_time(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._BLANKING_TIME_WRITE, 2)
    
    @property
    def idiss_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL2, Mask._IDISS_TIME_READ)
    
    @idiss_time.setter
    def idiss_time(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL2, value, Mask._IDISS_TIME_READ)
    
    @property
    def ng_tresh(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._NG_TRESH_READ, 6)
    
    @ng_tresh.setter
    def ng_tresh(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._NG_TRESH_WRITE, 6)
    
    @property
    def erm_open_loop(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._ERM_OPEN_LOOP_READ, 5)
    
    @erm_open_loop.setter
    def erm_open_loop(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._ERM_OPEN_LOOP_WRITE, 5)
    
    @property
    def supply_comp_dis(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._SUPPLY_COMP_DIS_READ, 4)
    
    @supply_comp_dis.setter
    def supply_comp_dis(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._SUPPLY_COMP_DIS_WRITE, 4)
    
    @property
    def data_format_rtp(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._DATA_FORMAT_RTP_READ, 3)

    @data_format_rtp.setter
    def data_format_rtp(self, value):
        if not Misc.RTP_SIGNED <= value <= Misc.RTP_UNSIGNED:
            raise ValueError("RTP format vale must be " + str(Misc.RTP_SIGNED) + " or " + str(Misc.RTP_UNSIGNED))
        self.write_register_value(Register._DRV260X_REG_CONTROL3, Mask._DATA_FORMAT_RTP_WRITE, 3)
    
    @property
    def lra_drive_mode(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._LRA_DRIVE_MODE_READ, 2)
    
    @lra_drive_mode.setter
    def lra_drive_mode(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._LRA_DRIVE_MODE_WRITE, 2)
    
    @property
    def n_pwm_analog(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._N_PWM_ANALOG_READ, 1)
    
    @n_pwm_analog.setter
    def n_pwm_analog(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._N_PWM_ANALOG_WRITE, 1)
    
    @property
    def lra_open_loop(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL3, Mask._LRA_OPEN_LOOP_READ)
    
    @lra_open_loop.setter
    def lra_open_loop(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL3, value, Mask._LRA_OPEN_LOOP_WRITE)
    
    @property
    def auto_cal_time(self):
        return self.read_register_value(Register._DRV260X_REG_CONTROL4, Mask._AUTO_CAL_TIME_READ, 4)
    
    @auto_cal_time.setter
    def auto_cal_time(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL4, value, Mask._AUTO_CAL_TIME_WRITE, 4)

    @property
    def otp_status(self):
        self.read_register_value(Register._DRV260X_REG_CONTROL4, Mask._OTP_STATUS_READ, 2)
    
    @property
    def otp_program(self):
        self.read_register_value(Register._DRV260X_REG_CONTROL4, Mask._OTP_PROGRAM_READ)

    @otp_program.setter
    def otp_program(self, value):
        self.write_register_value(Register._DRV260X_REG_CONTROL4, value, Mask._OTP_PROGRAM_WRITE)

    @property
    def vbat(self):
        return self.read_register_value(Register._DRV260X_REG_VOLTAGE_MONITOR, Mask._RATED_VOLTAGE_READ)
    
    @vbat.setter
    def vbat(self, value):
        self.write_register_value(Register._DRV260X_REG_VOLTAGE_MONITOR, value, Mask._RATED_VOLTAGE_WRITE)

    @property
    def lra_period(self):
        return self.read_register_value(Register._DRV260X_REG_LRA_RESONANCE_PERIOD, Mask._LRA_PERIOD_READ)
    
    @lra_period.setter
    def lra_period(self, value):
        self.write_register_value(Register._DRV260X_REG_LRA_RESONANCE_PERIOD, value, Mask._LRA_PERIOD_WRITE)  
    
    def get_waveform(self, sequencer):
        if not 0 <= sequencer <= 7:
            raise ValueError("Sequencer register must be between 0 and 7.")
        self.read_register_value(Register._DRV260X_REG_WAVESEQ0 + sequencer, Mask._WAV_FRM_SEQ_READ)

    def set_waveform(self, sequencer, value):
        if not 0 <= sequencer <= 7 or not 0 <= value <= 123:
            raise ValueError("Sequencer register must be between 0 and 7. Value must be between 0 and 123")
        self.write_register_value(Register._DRV260X_REG_WAVESEQ0 + sequencer, value, Mask._WAV_FRM_SEQ_WRITE)
    
    def write_register_value(self, register, value, write_mask, shift = 0):
        reg_val = self.read_byte(register)
        self.write_byte(register, (reg_val & write_mask) | (value << shift))    

    def read_register_value(self, register, read_mask, shift = 0):
        return (self.read_byte(register) & read_mask) >> shift
    
    def write_byte(self, register, value):
        if not Register._DRV260X_REG_STATUS <= register <= Register._DRV260X_REG_LRA_RESONANCE_PERIOD or register is Register._DRV260X_REG_INVALID_1 or register is Register._DRV260X_REG_INVALID_2:
            raise ValueError("Register " + str(register) + " not valid!")
        self.__i2c_bus.write_byte_data(Misc._DRV_ADDR, register, value)

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

    

class DRV260X(DRV260X_Base):
    
    _bemf_gain_values = {
        Misc.ACTUATOR_ERM: [0.33, 1.0, 1.8, 4.0],
        Misc.ACTUATOR_LRA: [5.0, 10.0, 20.0, 30.0]
    }

    _fb_brake_factor_values = [1, 2, 3, 4, 6, 8, 16, 0]

    def __init__(self, i2c):
        super().__init(i2c)

    def set_base_calibration_values(self, erm_lra, closed_open_loop, fb_brake_factor, loop_gain, auto_cal_time, drive_time, sample_time = 1, blanking_time = 2, idiss_time = 2):
        self.standby = 0
        self.mode = Mode.AUTOCAL
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
        if self.n_erm_lra == Misc.ACTUATOR_LRA:
            return self.drive_time * 0.1 + 0.5
        else:
            return self.drive_time * 0.2 + 1.0
    
    @drive_time_ms.setter
    def drive_time_ms(self, value):
        if self.n_erm_lra == Misc.ACTUATOR_LRA:
            self.drive_time = (value - 0.5) / 0.1
        else:
            self.drive_time = (value - 1.0) / 0.2

class DRV260X_ERM(DRV260X):
    def __init__(self, i2c):
        super().__init__(i2c)
        self.standby = 0
        self.n_erm_lra = Misc.ACTUATOR_ERM

    def calc_rated_voltage(self, voltage_volt):
        return voltage_volt / 0.02133

    def calc_od_clamp(self, voltage_volt, closed_open_loop, drive_time, idiss_time, blanking_time):
        if closed_open_loop == Misc.LOOP_MODE_CLOSED:
            return (voltage_volt * (drive_time + idiss_time + blanking_time)) / (0.02133 * (drive_time - 0.000300))
        elif closed_open_loop == Misc.LOOP_MODE_OPEN:
            return voltage_volt / 0.02196
        else:
            raise ValueError("closed_open_loop must be LOOP_MODE_CLOSED or LOOP_MODE_OPEN")
    
    def calibrate(self, voltage_volt, closed_open_loop, fb_brake_factor, loop_gain, auto_cal_time, drive_time, idiss_time, blanking_time, sample_time):
        self.set_base_calibration_values(Misc.ACTUATOR_ERM, closed_open_loop, fb_brake_factor, loop_gain, auto_cal_time, drive_time, sample_time, blanking_time, idiss_time)
        self.rated_voltage = self.calc_rated_voltage(voltage_volt)
        self.od_clamp = self.calc_od_clamp(voltage_volt, closed_open_loop, drive_time, idiss_time, blanking_time)

class DRV260X_LRA(DRV260X):
    def __init__(self, i2c):
        super().__init__(i2c)
        self.standby = 0
        self.n_erm_lra = Misc.ACTUATOR_LRA
    
    
    def calc_rated_voltage(self, voltage_volt, sample_time, resonant_frequency):
        return voltage_volt / (0.02071 * math.sqrt(1 - (4 * sample_time + 0.0003) * resonant_frequency))
    
    def calc_od_clamp(self, voltage_volt, closed_open_loop, resonant_frequency = 200):
        if closed_open_loop == Misc.LOOP_MODE_CLOSED:
            return voltage_volt / 0.02196
        elif closed_open_loop == Misc.LOOP_MODE_OPEN:
            return voltage_volt / (0.02133 * math.sqrt(1 - resonant_frequency * 0.0008))
        else:
            raise ValueError("closed_open_loop must be LOOP_MODE_CLOSED or LOOP_MODE_OPEN")
    
    def calibrate(self, voltage_volt, closed_open_loop, resonant_frequency, fb_brake_factor, loop_gain, auto_cal_time, drive_time, idiss_time, blanking_time, sample_time):
        self.set_base_calibration_values(Misc.ACTUATOR_LRA, closed_open_loop, fb_brake_factor, loop_gain, auto_cal_time, drive_time, sample_time, blanking_time, idiss_time)
        self.rated_voltage = self.calc_rated_voltage(voltage_volt, sample_time, resonant_frequency)
        self.od_clamp = self.calc_od_clamp(voltage_volt, closed_open_loop, drive_time, idiss_time, blanking_time)


