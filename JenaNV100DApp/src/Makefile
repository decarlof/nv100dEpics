TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = JenaNV100DApp

# JenaNV100DApp.dbd will be created and installed
DBD += JenaNV100DApp.dbd

# test.dbd will include these files:
JenaNV100DApp_DBD += base.dbd
JenaNV100DApp_DBD += busySupport.dbd
JenaNV100DApp_DBD += asSupport.dbd

# JenaNV100DApp_registerRecordDeviceDriver.cpp derives from test.dbd
JenaNV100DApp_SRCS += JenaNV100DApp_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
JenaNV100DApp_SRCS_DEFAULT += JenaNV100DMain.cpp
JenaNV100DApp_SRCS_vxWorks += -nil-

JenaNV100DApp_LIBS += autosave
JenaNV100DApp_LIBS += busy
#JenaNV100DApp_LIBS += asyn

# Finally link IOC to the EPICS Base libraries
JenaNV100DApp_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE
