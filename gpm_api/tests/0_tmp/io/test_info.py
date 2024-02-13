#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:14:46 2022

@author: ghiggi
"""
### NASA pattern
# product level:
# - 1A, 2A, 2B,
# - 3A-MO, 3B-DAY, 3A-DAY-ASC, 3A-DAY-DESC, 3B-ORBIT, 3B-MO. 3B-HHR-{E/L}
# - 2A-CS-<SITE> (CS=COINCIDENCE)

# satellite:
# - TRMM, GPM, SSMIS, ..
# - MS (multi-sensor) --> IMERG

### JAXA pattern
# mission_id (mission + satellite_id)
# sensor: KUR, KAR, CMB
# product_type: R(NRT) or S (RS)

### Example file names
# # IMERG
# filename = "3B-HHR.MS.MRG.3IMERG.20140422-S043000-E045959.0270.V06B.HDF5"

# IMERG-EARLY
# 3B-HHR-E.MS.MRG.3IMERG.20221201-S020000-E022959.0120.V06C.RT-H5
# # IMERG-LATE
# 3B-HHR-L.MS.MRG.3IMERG.20221201-S023000-E025959.0150.V06C.RT-H5
# # IMERG FINAL
# 3B-HHR.MS.MRG.3IMERG.20190713-S123000-E125959.0750.V06B.HDF5

# # 2B
# filename = "2B.GPM.DPRGMI.2HCSHv7-0.20140422-S013047-E030320.000831.V07A.HDF5"
# filename = "2B.GPM.DPRGMI.CORRA2022.20140422-S230649-E003923.000845.V07A.HDF5"
# filename = "2B.TRMM.PRTMI.2HCSHv7-0.20140422-S110725-E123947.093603.V07A.HDF5"

# # 2A
# filename = "2A.MT1.SAPHIR.PRPS2019v2-02.20140422-S000858-E015053.013038.V06A.HDF5"
# filename = "2A.GPM.DPR.V9-20211125.20201028-S075448-E092720.037875.V07A.HDF5"
# # 1C
# filename = "1C.GPM.GMI.XCAL2016-C.20140422-S013047-E030320.000831.V07A.HDF5"

# # 1B
# filename = "GPMCOR_KUR_2010280754_0927_037875_1BS_DAB_07A.h5"
# filename = "GPMCOR_KAR_2010280754_0927_037875_1BS_DAB_07A.h5"
# filename = "1B.TRMM.PR.V9-20210630.20140422-S002044-E015306.093596.V07A.HDF5"
# # 1A
# filename = "1A.GPM.GMI.COUNT2021.20140422-S230649-E003923.000845.V07A.HDF5"
# filename = "1A.TRMM.TMI.COUNT2021.20140422-S002044-E015306.093596.V07A.HDF5"
