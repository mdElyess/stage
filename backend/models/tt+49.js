const mongoose = require("mongoose");

const ttPlusSchema49 = mongoose.model("TTPlus_49", {
  date: String,
  time: String,
  tt_id: String,
  record_number: String,
  device_type: String,
  timestamp: String,
  as7263_610: String,
  as7263_680: String,
  as7263_730: String,
  as7263_760: String,
  as7263_810: String,
  as7263_860: String,
  as7262_450: String,
  as7262_500: String,
  as7262_550: String,
  as7262_570: String,
  as7262_600: String,
  as7262_650: String,
  integration_time: String,
  gain: String,
});

module.exports = ttPlusSchema49;
