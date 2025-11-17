# This script creates an object of type JenaNV100D for supporting JenaNV100DApp
# To run this script type the following:
#     python -i start_JenaNV100D.py
# The -i is needed to keep Python running, otherwise it will create the object and exit
from JenaNV100D.JenaNV100D import JenaNV100D
ts = JenaNV100D(["../../db/JenaNV100D_settings.req","../../db/JenaNV100D_settings.req"], {"$(P)":"32id:", "$(R)":"JenaNV100D:"})
