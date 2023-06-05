const mongoose = require("mongoose");

const ttPlusSchema4D = mongoose.model("TTPlus_4D", {
  date: String,
  time: String,
  tt_id: String,
  record_number: String,
  device_type: String,
  timestamp: String,
  tref0: String,
  theat0: String,
  growth_sensor: String,
  adc_badgap: String,
  number_bits: String,
  air_humidity: String,
  air_temperature: String,
  gz_mean: String,
  gz_std: String,
  gy_mean: String,
  gy_std: String,
  gx_mean: String,
  gx_std: String,
  tref1: String,
  theat1: String,
  stwc: String,
  adc_vbat: String,
});

module.exports = ttPlusSchema4D;