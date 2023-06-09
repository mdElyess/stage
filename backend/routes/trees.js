const express = require("express");

const router = express.Router();
const Cloud = require("../models/cloud");

router.get('/ttcloud', (req, res) => {
    
    res.send({
        "_id": 79003,
        "dateTime": {
          "$date": "2023-06-04T11:00:37.000Z"
        },
        "deviceType": "4B",
        "numberRecords": 63714,
        "dataNotSent": 0,
        "countryCode": 216,
        "mobileCountryCODE": 605,
        "country": "Tunisia",
        "networkRegistration": "YES",
        "TTCloudSignalStrength": 26,
        "batteryLevel": 4144,
        "firmwareVersion": "rel.5.1L"
      })
})

router.get('/ttplus', (req, res) => {
    res.send({
        "_id": 79033,
        "dateTime": {
          "$date": "2023-06-04T16:14:39.000Z"
        },
        "deviceType": "55",
        "tRef_0(°C)": 23.93,
        "tHeat_0(°C)": 25.47,
        "tRef_1(°C)": 24.00,
        "tHeat_1(°C)": 28.86,
        "sapFluxDensity": 9.67,
        "airTemperature": 27.8,
        "airHumidity": 61,
        "batteryVoltage": 3117.7,
        "growthRate": 49.06,
        "AxOut(deg)": -3.97,
        "AyOut(deg)": 0.22,
        "AzOut(deg)": -1.27
      })
})

module.exports = router;