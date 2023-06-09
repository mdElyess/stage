const mongoose = require("mongoose");

const ttCloudSchema4B = mongoose.model("Cloud", {

  _id: Number,
  dateTime: String,
  deviceType: String,
  numberRecords: String,
  dataNotSent: String,
  countryCode: String,
  mobileCountryCODE: String,
  country: String,
  networkRegistration: String,
  TTCloudSignalStrength: String,
  batteryLevel: String,
  firmwareVersion: String,
  
});

module.exports = ttCloudSchema4B;
