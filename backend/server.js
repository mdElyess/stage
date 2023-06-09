const express = require("express");
const cors = require('cors');
const { spawn } = require('child_process');

// import API
const userApi = require("./routes/users");
const treeApi = require("./routes/trees");

require("./config/connect");

const pythonScript = spawn('python', ['./ttest.py']);
const app = express();

app.use(cors())
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/tree", treeApi);
app.use("/user", userApi);

pythonScript.stdout.on('data', (data) => {
  console.log(data);
});

pythonScript.on('error', (error) => {
  console.error(`Error executing Python script: ${error.message}`);
});


pythonScript.on('close', (code) => {
  console.log(`Python script exited with code ${code}`);
});


app.listen(4200, () => {
  console.log("Server alive...");
});


