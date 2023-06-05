const express = require('express')
const bodyParser = require('body-parser');

// import API
const userApi = require('./routes/users')

require('./config/connect')

const app = express();


app.use('/user' ,userApi)
app.use(bodyParser.json());


app.listen(5000, () => {
    console.log('Server alive...');
})