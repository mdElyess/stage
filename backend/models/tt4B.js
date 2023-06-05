const mongoose = require("mongoose");

const ttCloudSchema4B = mongoose.model("TTCloud_4B", {
  date: String,
  time: String,
  id: String,
  number_records: String,
  device_type: String,
  timeestamp: String,
  line_number: String,
  data_not_sent: String,
  country_code: String,
  mobile_country_code: String,
  network_registration: String,
  ttcloud_signal_strength: String,
  battery_level: String,
  firmware_version: String,
});

module.exports = ttCloudSchema4B;
