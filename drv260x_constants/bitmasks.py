# Status Register
_DEVICE_ID_READ =            0b11100000
_DIAG_RESULT_READ =          0b00001000
_FB_STS_READ =               0b00000100
_OVER_TEMP_READ =            0b00000010
_OC_DETECT_READ =            0b00000001
# Mode Register
_DEV_RESET_READ =            0b10000000
_DEV_RESET_WRITE =           0b01111111
_STANDBY_READ =              0b01000000
_STANDBY_WRITE =             0b10111111
_MODE_READ =                 0b00000111
_MODE_WRITE =                0b11111000
# Real-Time Playback Input Register
_RTP_INPUT_READ =            0b11111111
_RTP_INPUT_WRITE =           0b00000000
# Register 0x03
_HI_Z_READ =                 0b00010000
_HI_Z_WRITE =                0b11101111
_LIBRARY_SEL_READ =          0b00000111
_LIBRARY_SEL_WRITE =         0b11111000
# Waveform Sequencer Registers
_WAIT_READ =                 0b10000000
_WAIT_WRITE =                0b01111111
_WAV_FRM_SEQ_READ =          0b01111111
_WAV_FRM_SEQ_WRITE =         0b10000000
# GO Register
_GO_READ =                   0b00000001
_GO_WRITE =                  0b11111110
# Overdrive Time Offset Register
_ODT_READ =                  0b11111111
_ODT_WRITE =                 0b00000000
# Sustain Time Offset, Positive Register
_SPT_READ =                  0b11111111
_SPT_WRITE =                 0b00000000
# Sustain Time Offset, Negative Register
_SNT_READ =                  0b111111111
_SNT_WRITE =                 0b000000000
# Break Time Offset Register
_BRT_READ =                  0b11111111
_BRT_WRITE =                 0b00000000
# Audio-to-Vibe Control Register
_ATH_PEAK_TIME_READ =        0b00001100
_ATH_PEAK_TIME_WRITE =       0b11110011
_ATH_FILTER_READ =           0b00000011
_ATH_FILTER_WRITE =          0b11111100
# Audio-to-Vibe Minimum Input Level Register
_ATH_MIN_INPUT_READ =        0b11111111
_ATH_MIN_INPUT_WRITE =       0b00000000
# Audio-to-Vibe Maximum Input Level Register
_ATH_MAX_INPUT_READ =        0b11111111
_ATH_MAX_INPUT_WRITE =       0b00000000
# Audio-to-Vibe Minimum Output Drive Register
_ATH_MIN_DRIVE_READ =        0b11111111
_ATH_MIN_DRIVE_WRITE =       0b00000000
# Audio-to-Vibe Maximum Output Drive Register
_ATH_MAX_DRIVE_READ =        0b11111111
_ATH_MAX_DRIVE_WRITE =       0b00000000
# Rated Voltage Register
_RATED_VOLTAGE_READ =        0b11111111
_RATED_VOLTAGE_WRITE =       0b00000000
# Overdrive Clamp Voltage Register
_OD_CLAMP_READ =             0b11111111
_OD_CLAMP_WRITE =            0b00000000
# Auto-CalibrationCompensation-Result Register
_A_CAL_COMP_READ =           0b11111111
_A_CAL_COMP_WRITE =          0b00000000
# Auto-CalibrationBack-EMF Result Register
_A_CAL_BEMF_READ =           0b11111111
_A_CAL_BEMF_WRITE =          0b00000000
# Feedback Control Register
_N_ERM_LRA_READ =            0b10000000
_N_ERM_LRA_WRITE =           0b01111111
_FB_BRAKE_FACTOR_READ =      0b01110000
_FB_BRAKE_FACTOR_WRITE =     0b10001111
_LOOP_GAIN_READ =            0b00001100
_LOOP_GAIN_WRITE =           0b11110011
_BEMF_GAIN_READ =            0b00000011
_BEMF_GAIN_WRITE =           0b11111100
# Control Register 1
_STARTUP_BOOST_READ =        0b10000000
_STARTUP_BOOST_WRITE =       0b01111111
_AC_COUPLE_READ =            0b00100000
_AC_COUPLE_WRITE =           0b11011111
_DRIVE_TIME_READ =           0b00011111
_DRIVE_TIME_WRITE =          0b11000000
# Control Register 2
_BIDIR_INPUT_READ =          0b10000000
_BIDIR_INPUT_WRITE =         0b01111111
_BRAKE_STABILIZER_READ =     0b01000000
_BRAKE_STABILIZER_WRITE =    0b10111111
_SAMPLE_TIME_READ =          0b00110000
_SAMPLE_TIME_WRITE =         0b11001111
_BLANKING_TIME_READ =        0b00001100
_BLANKING_TIME_WRITE =       0b11110011
_IDISS_TIME_READ =           0b00000011
_IDIS_TIME_WRITE =           0b11111100
# Control Register 3
_NG_TRESH_READ =             0b11000000
_NG_TRESH_WRITE =            0b00111111
_ERM_OPEN_LOOP_READ =        0b00100000
_ERM_OPEN_LOOP_WRITE =       0b11011111
_SUPPLY_COMP_DIS_READ =      0b00010000
_SUPPLY_COMP_DIS_WRITE =     0b11101111
_DATA_FORMAT_RTP_READ =      0b00001000
_DATA_FORMAT_RTP_WRITE =     0b11110111
_LRA_DRIVE_MODE_READ =       0b00000100
_LRA_DRIVE_MODE_WRITE =      0b11111011
_N_PWM_ANALOG_READ =         0b00000010
_N_PWM_ANALOG_WRITE =        0b11111101
_LRA_OPEN_LOOP_READ =        0b00000001
_LRA_OPEN_LOOP_WRITE =       0b11111110
# Control Register 4
_AUTO_CAL_TIME_READ =        0b00110000
_AUTO_CAL_TIME_WRITE =       0b11001111
_OTP_STATUS_READ =           0b00000100
_OTP_PROGRAM_READ =          0b00000001
_OTP_PROGRAM_WRITE =         0b11111110
# Voltage Monitor
_VBAT_READ =                 0b11111111
_VBAT_WRITE =                0b00000000
# LRA Resonance Period
_LRA_PERIOD_READ =           0b11111111
_LRA_PERIOD_WRITE =          0b00000000