const express = require("express");

// import API
const userApi = require("./routes/users");

require("./config/connect");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/user", userApi);

app.listen(4200, () => {
  console.log("Server alive...");
});
