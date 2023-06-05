const mongoose = require("mongoose");

const ttCloudSchema4C = mongoose.model("TTCloud_4C", {
  date: String,
  time: String,
  id: String,
  number_records: String,
  device_type: String,
  timeestamp: String,
  tbl_locked: String,
  num_first_sensor: String,
  rssi_tt1_ttcloud: String,
  rssi_tt2_ttcloud: String,
  rssi_tt3_ttcloud: String,
  rssi_tt4_ttcloud: String,
  rssi_tt5_ttcloud: String,
  rssi_tt6_ttcloud: String,
  rssi_tt7_ttcloud: String,
  rssi_tt8_ttcloud: String,
  rssi_tt9_ttcloud: String,
  rssi_tt11_ttcloud: String,
  rssi_tt12_ttcloud: String,
  rssi_tt13_ttcloud: String,
  rssi_tt14_ttcloud: String,
  rssi_tt15_ttcloud: String,
  rssi_tt16_ttcloud: String,
  rssi_tt17_ttcloud: String,
  rssi_tt18_ttcloud: String,
  rssi_tt19_ttcloud: String,
  rssi_tt20_ttcloud: String,
  rssi_tt21_ttcloud: String,
});

module.exports = ttCloudSchema4C;