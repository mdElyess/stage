from datetime import datetime
from urllib.request import urlopen
from datetime import timedelta
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import math
load_dotenv(find_dotenv())
# conection a la base de dennees mongodb
connection_string = "mongodb://127.0.0.1:27017/"
# create  database called smartGardenNew
client = MongoClient(connection_string)
smartGardenNew = client.smartGardenNew

# connection au lien des donnees
link = "https://naturetalkers.altervista.org/C0210045/ttcloud.txt"

url = urlopen(link)
# treeListIdTTPlus=['621B0408','621B0400','62190380']
# treeListIdTTWINE=['63210025','64210015','63210030']

# create  a new collection called cloud
cloud = smartGardenNew.cloud
# create  a new collection called generalData
generalData = smartGardenNew.generalData
# create a new collection called tree0TTPlus
tree0TTPlus55 = smartGardenNew.tree0TTPlus55
# create  a new collection called tree1TTPlus
tree1TTPlus55 = smartGardenNew.tree1TTPlus55
# create  a new collection called tree2TTPlus
tree2TTPlus55 = smartGardenNew.tree2TTPlus55
# create a new collection called tree0TTPlus
tree0TTPlus49 = smartGardenNew.tree0TTPlus49
# create  a new collection called tree1TTPlus
tree1TTPlus49 = smartGardenNew.tree1TTPlus49
# create  a new collection called tree2TTPlus
tree2TTPlus49 = smartGardenNew.tree2TTPlus49
# create  a new collection called tree0TTSoil55
tree0TTSoil55 = smartGardenNew.tree0TTSoil55
# create  a new collection called tree1TTSoil55
tree1TTSoil55 = smartGardenNew.tree1TTSoil55
# create  a new collection called tree2TTSoil55
tree2TTSoil55 = smartGardenNew.tree2TTSoil55

# create  a new collection called tree0TTSoil49
tree0TTSoil49 = smartGardenNew.tree0TTSoil49
# create  a new collection called tree1TTSoil49
tree1TTSoil49 = smartGardenNew.tree1TTSoil49
# create  a new collection called tree2TTSoil49
tree2TTSoil49 = smartGardenNew.tree2TTSoil49

treedicTTPlus = {'621B0408': [tree0TTPlus55, tree0TTPlus49],  # 621B048 id tree 0 of tt+
                 # 621B0400 id tree 1 of tt+
                 '621B0400': [tree1TTPlus55, tree1TTPlus49],
                 # 62190380 id tree 2 of tt+
                 '62190380': [tree2TTPlus55, tree2TTPlus49]

                 }

# create a dict called treedicTTPlus
treedicTTSoil = {'63210025': [tree0TTSoil55, tree0TTSoil49],
                 '64210015': [tree1TTSoil55, tree1TTSoil49],
                 '63210030': [tree2TTSoil55, tree2TTSoil49]
                 }

# thermal diffusivity of green wood
thd = {'64210015': 0.0358646371824824,
       '63210025': 0.063051907613087,
       '63210030': 0.13898268743410033,
       }

#lastLineNum = generalData.find_one()[ "last line number"]
lastLineNum = 0

file = url.readlines()[lastLineNum+1:]

for numLine, line in enumerate(file, lastLineNum+1):
    new_line = line.decode().strip()
    L1 = new_line.split()
    ch2 = L1[1]
    L2 = ch2.split(',')
    ch3 = L2[1]
    L3 = ch3.split(';')
    idTT = L3[0]
    sousidTT = L3[2]  # decouper la ligne
    # up_line=int(L3[1],16)
    d = dict()
    time_str = L1[0].replace('.', '/')+" "+L2[0]
    date_format_str = '%d/%m/%y %H:%M:%S'
    given_time = datetime.strptime(time_str, date_format_str)  # date of data
    d["_id"] = numLine
    # real time is  given_time-timedelta(hours=1
    d["dateTime"] = given_time-timedelta(hours=1)
    if idTT in treedicTTPlus:
        # 63210025  , 64210015  ,63210030  TTSOL no documents
        if sousidTT == '55':
            d["deviceType"] = L3[2]
            temperatureRef0 = 127.6-0.006045 * \
                int(L3[4]) + 1.26*(10**-7)*(int(L3[4]))**2 - \
                1.15*(10**-12)*(int(L3[4]))**3
            temperatureHeat0 = 127.6-0.006045 * \
                int(L3[5]) + 1.26*(10**-7)*(int(L3[5]))**2 - \
                1.15*(10**-12)*(int(L3[5]))**3
            temperatureRef1 = 127.6-0.006045 * \
                int(L3[17]) + 1.26*(10**-7)*(int(L3[17]))**2 - \
                1.15*(10**-12)*(int(L3[17]))**3
            temperatureHeat1 = 127.6-0.006045 * \
                int(L3[18]) + 1.26*(10**-7)*(int(L3[18]))**2 - \
                1.15*(10**-12)*(int(L3[18]))**3
            dTmax = temperatureHeat1-temperatureHeat0
            dTi = temperatureRef1-temperatureRef0
            d["tRef_0"] = temperatureRef0
            d["tHeat_0"] = temperatureHeat0
            d["tRef_1"] = temperatureRef1
            d["tHeat_1"] = temperatureHeat1
            d["sapFluxDensity"] = (((dTmax-dTi)/dTmax)*10.43)-0.52
            d["airTemperature"] = float(int(L3[10])/10)
            d["airHumidity"] = float(L3[9])
            d["batteryVoltage"] = ((2*1100*int(L3[len(L3)-1]))/int(L3[7]))
            d["growthRate"] = ((-30/45000)*float(L3[6]))+66.67
            d["AxOut"] = (float(L3[11])/1096)*(1/0.9)
            d["AyOut"] = (float(L3[13])/1096)*(1/0.9)
            d["AzOut"] = (float(L3[15])/1096)*(1/0.9)
            # (0.000000008*(float(L3[6]))**2)-(0.0016*(float(L3[6]))+89.032)/(-10)
            if idTT == '621B0400':
                tree0TTPlus55.insert_one(d)
            elif idTT == '621B0408':
                tree1TTPlus55.insert_one(d)
            elif idTT == '62190380':
                tree2TTPlus55.insert_one(d)

        else:  # sousidTT==49 or 4C or 4B
            d["deviceType"] = L3[2]
            d["integrationTime"] = int(L3[len(L3)-2])*2.8
            d["gain"] = float(L3[len(L3)-1])
            d["absorbedEnergy"] = ((float(L3[10])*0.4562)+(float(L3[11])*0.6257)+(1.0546*float(
                L3[12]))+(float(L3[13])*1.0462)+(float(L3[14])*0.8654)+(float(L3[15])*0.7829)-2078.88)/28.0
            if idTT == '621B0400':
                tree0TTPlus49.insert_one(d)
            elif idTT == '621B0408':
                tree1TTPlus49.insert_one(d)
            elif idTT == '62190380':
                tree2TTPlus49.insert_one(d)

    if idTT in treedicTTSoil:
        # 10.02.20 13:14:46,52010001;263;4D;1581336000;35316;35135;62750;42514;17;26;210;-3894;0;-76;0;-1319;0;35234;29259;8905;79185

        if sousidTT == '55':  # 4E in the document
            d["deviceType"] = L3[2]  # device type  4D
            d["recordNumber"] = int(L3[1], 16)  # 263
            TDownStream_0 = -7*(10**-11)*(int(L3[5]))**3 + 2*(10**-6)*(
                int(L3[5]))**2-0.0229*int(L3[5])+117.28  # L3[5] = Tref_0 [d.n.] =35316
            d["TDownStream_0"] = TDownStream_0
            TUpStream_0 = -7*(10**-11)*(int(L3[6]))**3 + 2*(10**-6)*(
                int(L3[6]))**2-0.0229*int(L3[6])+117.28  # L3[6] = Theat_0 [d.n.] = 35135
            d["TUpStream_0"] = TUpStream_0
            TDownStream_1 = -7*(10**-11)*(int(L3[12]))**3 + 2*(10**-6)*(
                int(L3[12]))**2-0.0229*int(L3[12])+117.28  # L3[12]= g_z(mean) [d.n.] 376
            d["TDownStream_1"] = TDownStream_1
            TUpStream_1 = -7*(10**-11)*(int(L3[13]))**3 + 2*(10**-6)*(
                int(L3[13]))**2-0.0229*int(L3[13])+117.28  # L3[13]= g_y (mean) [d.n.] 1980
            d["TUpStream_1"] = TUpStream_1
            TDownStreamAvg = -7*(10**-11)*(int(L3[15]))**3 + 2*(10**-6)*(
                int(L3[15]))**2-0.0229*int(L3[15])+117.28  # L3[15]=g_x (mean) [d.n.] 3604
            d["TDownStreamAvg"] = TDownStreamAvg
            TUpStreamAvg = -7*(10**-11)*(int(L3[16]))**3 + 2*(10**-6)*(
                int(L3[16]))**2-0.0229*int(L3[16])+117.28  # L3[16] = g_x (std.dev) [d.n.] 0
            d["TUpStreamAvg"] = TUpStreamAvg
            d["TDownStreamMax"] = -7*(10**-11)*(int(L3[17]))**3 + 2*(10**-6)*(
                int(L3[17]))**2-0.0229*int(L3[17])+117.28  # L3[17]= Tref_1 [d.n.] 35234
            d["TUpStreamMax"] = -7*(10**-11)*(int(L3[18]))**3 + 2*(10**-6)*(
                int(L3[18]))**2-0.0229*int(L3[18])+117.28  # L3[18]=Theat_1 [d.n.] 29259
            timeTdMax = int(L3[19])*0.001
            d['timeTdMax'] = int(L3[19])  # L3[19] StWC [freq (Hz)] 49951
            d["timeTuMax"] = int(L3[20])  # l3[20]= adc_Vbat [d.n.] 79185

            # pythagore
            ΔTd_avg = ((TDownStream_0-TDownStream_1)**2+40**2)**0.5
            # =40 always TUpStream_1=TUpStream_0
            ΔTu_avg = ((TUpStream_0-TUpStream_1)**2+40**2)**0.5
            # (math.log2(ΔTd_avg/ΔTu_avg)/x)**2 k**2 + (4/timeTdMax) k + (0.5/timeTdMax)**2 = 0

            # L3[8] = adc_bandgap [d.n.] 42514
            d["batteryVoltage"] = 650 + 131072*(1100/int(L3[8]))
            d["dataResolution"] = int(L3[9])  # number of bits 17
            # L3[10]=Air relative humidity [%] 26
            d["airRelativeHumidity"] = int(L3[10])
            # L3[11] = Air temperature [10*° C] 210
            d["airTemperature"] = int(L3[11])*0.1
            TSoil_0 = -7 * \
                (10**-11)*(int(L3[4]))**3 + 2*(10**-6) * \
                (int(L3[4]))**2-0.0229*int(L3[4])+117.28
            # L3[11] = Air temperature [10*° C] 210
            TSoil_1 = -7*(10**-11)*(int(L3[11]))**3 + 2*(10**-6) * \
                (int(L3[11]))**2-0.0229*int(L3[11])+117.28
            d["TSoil_0"] = -7*(10**-11)*(int(L3[4]))**3 + 2 * \
                (10**-6)*(int(L3[4]))**2-0.0229*int(L3[4])+117.28
            d["TSoil_1"] = -7*(10**-11)*(int(L3[11]))**3 + 2*(10**-6)*(int(L3[11])
                                                                           )**2-0.0229*int(L3[11])+117.28  # L3[11] = Air temperature [10*° C] 210
            TSoilAvg = (TSoil_0+TSoil_1)/2
            TSoilAvgC = -7*(10**-11)*(TSoilAvg)**3 + 2*(10**-6) * \
                (TSoilAvg)**2-0.0229*TSoilAvg+117.28
            d["TSoilAvg"] = -TSoilAvg
            EcfSoil = int(L3[14])
            d["EcfSoil"] = EcfSoil
            ECf_T = -11.282*TSoilAvgC*2467.3
            ΔECf = EcfSoil-ECf_T
            SVWCAfricanSoil = -4*(10**-12)*(ΔECf)**3+2 * \
                (10**-7)*(ΔECf)**2-0.0026*ΔECf+47.409
            SVWCloamySoil = 2*(10**-12)*(ΔECf)**3+7 * \
                (10**-8)*(ΔECf)**2-0.0039*ΔECf+50.647
            d["SVWCAfricanSoil"] = SVWCAfricanSoil
            d["SVWCloamySoil"] = SVWCloamySoil
            """if idTT=='63210025':
               d["heatVelocityMarshall_Burgess(cm/hr)"]=(thd['63210025']/0.5)*math.log2(ΔTd_avg/ΔTu_avg)
               d["heatVelocityMax(cm/hr)"]=(((0.5**2)-4*thd['63210025']*(timeTdMax/3600))**0.5)/(timeTdMax/3600)
               tree0TTSoil55.insert_one(d) #insert  d in collection tree0ttwine55
               #print(d)
            elif idTT=='63210030':
               d["heatVelocityMarshall_Burgess(cm/hr)"]=(thd['63210030']/0.5)*math.log2(ΔTd_avg/ΔTu_avg)
               d["heatVelocityMax(cm/hr)"]=(((0.5**2)-4*thd['63210030']*(timeTdMax/3600))**0.5)/(timeTdMax/3600)
               #print(d)
               tree1TTSoil55.insert_one(d) #insert  d in collection tree1ttwine55
            elif idTT=='64210015':
               d["heatVelocityMarshall_Burgess(cm/hr)"]=(thd['64210015']/0.5)*math.log2(ΔTd_avg/ΔTu_avg)
               d["heatVelocityMax(cm/hr)"]=(((0.5**2)-4*thd['64210015']*(timeTdMax/3600))**0.5)/(timeTdMax/3600)
               tree2TTSoil55.insert_one(d) #insert  d in collection tree2ttwine55"""
            # print(d)
           # 13:15:02,52010001;264;49;1581336000;3315;2985;10053;12202;12064;12370;7513;9705;11017;9242;6211;4368;50;3

        elif sousidTT == '49':
            d["deviceType"] = L3[2]  # device type 49
            d["recordNumber"] = int(L3[1], 16)
            d["solarEnergy"] = ((float(L3[10])*0.4562)+(float(L3[11])*0.6257)+(1.0546*float(L3[12]))+(
                float(L3[13])*1.0462)+(float(L3[14])*0.8654)+(float(L3[15])*0.7829)-2078.88)/28.0
            """L3[10]      AS7262_450 [d.n.] 50 
               L3[11]      AS7262_500 [d.n.] 67
               L3[12]      AS7262_550 [d.n.] 297
               L3[13]     AS7262_570 [d.n.] 243
               L3[14]     AS7262_600 [d.n.] 362
               L3[15]     AS7262_650 [d.n.] 145"""
            d["integrationTime"] = int(L3[len(L3)-2]) * \
                2.8  # L3[len(L3)-2] integration time 50
            d["gain"] = float(L3[len(L3)-1])  # L3 [len(L3)-1 ] gain 3
            if idTT == '63210025':
                # insert  d in collection tree0TTSoil49
                tree0TTSoil49.insert_one(d)
            elif idTT == '63210030':
                # insert  d in collection tree1TTSoil49
                tree1TTSoil49.insert_one(d)
            elif idTT == '64210015':
                tree2TTSoil49.insert_one(
                    d)  # insert  d in collection tree2TTSoil49"""
    # TTcloud
    # 06.10.19 03:00:23, C1940055; 1BBF6;4B;1570323602; 113653;0;222;88;1;17; 3568;rel.4.9h
    if idTT == 'C0210045':
        if (sousidTT == '4B'):  # 4C !! no document
            d["deviceType"] = L3[2]
            # L3[4] Accumulated records in memory 113653
            d["numberRecords"] = int(L3[4])
            # L[5] Number of records that still needs to be send to the server 0
            d["dataNotSent"] = int(L3[5])
            d["countryCode"] = 216
            # L3[6] MNC telephone operator 88
            d["mobileCountryCODE"] = int(L3[6])
            d["country"] = "Tunisia"
            if (int(L3[8]) == 0):
                d["networkRegistration"] = "NO"
            else:
                d["networkRegistration"] = "YES"
            # L3[9] GSM field level (from 0 to 32) 17
            d["TTCloudSignalStrength"] = int(L3[9])
            # L3[10] Battery level (mv) 3568
            d["batteryLevel"] = int(L3[10])
            d["firmwareVersion"] = L3[11]
            cloud.insert_one(d)  # insert  d in the collection cloud """

generalData.update_one(
    {}, {"$set": {"last line number": len(file)+lastLineNum}})

